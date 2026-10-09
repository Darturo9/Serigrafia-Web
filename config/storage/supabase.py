"""Backend privado de fotos; API HTTP de Storage, nunca SQL sobre sus tablas."""
from io import BytesIO
import json
from pathlib import PurePosixPath
from urllib.parse import quote, urlsplit
from uuid import uuid4
import warnings

from django.core.exceptions import ImproperlyConfigured, SuspiciousFileOperation
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from PIL import Image, ImageOps, UnidentifiedImageError

from config.runtime_settings import PROJECT_URL

MAX_BYTES = 5 * 1024 * 1024
MAX_PIXELS = 16_000_000
MAX_WEBP_BYTES = 500 * 1024
MAX_WEBP_EDGE = 1600
WEBP_QUALITY = 80
FORMATS = {"JPEG": ("jpg", "image/jpeg"), "PNG": ("png", "image/png"), "WEBP": ("webp", "image/webp")}


class PhotoStorageError(Exception):
    """Error recuperable sin URLs, credenciales ni respuestas del proveedor."""


class SupabasePrivateStorage(Storage):
    def __init__(self, base_url, bucket, key, expires_in=300, client=None):
        if base_url != PROJECT_URL or bucket != "jyz-prueba-fotos" or not key:
            raise ImproperlyConfigured("Configurar el proyecto y bucket privados de la prueba JYZ.")
        if not 60 <= expires_in <= 3600:
            raise ImproperlyConfigured("Caducidad de fotos entre 60 y 3600 segundos.")
        self.base_url = base_url
        self.bucket = bucket
        self._key = key
        self.expires_in = expires_in
        self._client = client

    def __repr__(self):
        return f"<SupabasePrivateStorage bucket={self.bucket!r}>"

    def _path(self, name):
        path = PurePosixPath(name)
        if not name or path.is_absolute() or ".." in path.parts or "\\" in name or name.startswith("/"):
            raise SuspiciousFileOperation("Ruta de foto inválida.")
        return quote(self.bucket, safe="") + "/" + quote(name, safe="/")

    def _request(self, method, path, *, data=None, content_type=None, missing_ok=False):
        import httpx
        headers = {"apikey": self._key, "Authorization": "Bearer " + self._key}
        if content_type:
            headers["Content-Type"] = content_type
        if method == "POST" and path.startswith("object/") and not path.startswith("object/sign/"):
            headers["x-upsert"] = "false"
        try:
            if self._client is None:
                with httpx.Client(timeout=15, follow_redirects=False) as client:
                    response = client.request(method, self.base_url + "/storage/v1/" + path, content=data, headers=headers)
            else:
                response = self._client.request(method, self.base_url + "/storage/v1/" + path,
                                                content=data, headers=headers)
        except httpx.HTTPError:
            raise PhotoStorageError("No se pudo conectar al almacenamiento. Intente de nuevo.") from None
        if missing_ok and response.status_code == 404:
            return None
        if not 200 <= response.status_code < 300:
            raise PhotoStorageError("El almacenamiento no pudo completar la operación. Intente de nuevo.") from None
        return response

    def get_available_name(self, name, max_length=None):
        # _save genera un UUID nuevo; no reutilizar ni sobrescribir un objeto existente.
        self._path(name)
        return name

    def _save(self, name, content):
        data = content.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise PhotoStorageError("La foto debe pesar como máximo 5 MB.")
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error", Image.DecompressionBombWarning)
                with Image.open(BytesIO(data)) as image:
                    fmt = image.format
                    if fmt not in FORMATS or image.width * image.height > MAX_PIXELS:
                        raise PhotoStorageError("Use JPEG, PNG o WebP de hasta 16 megapíxeles.")
                    if getattr(image, "n_frames", 1) != 1:
                        raise PhotoStorageError("Use una foto estática, sin animación.")
                    image.verify()
                with Image.open(BytesIO(data)) as image:
                    image = ImageOps.exif_transpose(image)
                    mode = "RGBA" if "A" in image.getbands() or "transparency" in image.info else "RGB"
                    optimized = image.convert(mode)
                    optimized.thumbnail((MAX_WEBP_EDGE, MAX_WEBP_EDGE), Image.Resampling.LANCZOS)
                    while True:
                        stream = BytesIO()
                        optimized.save(stream, format="WEBP", quality=WEBP_QUALITY, method=4,
                                       exif=b"", xmp=b"", icc_profile=b"")
                        encoded = stream.getvalue()
                        if len(encoded) <= MAX_WEBP_BYTES:
                            break
                        if max(optimized.size) <= 320:
                            raise PhotoStorageError("La foto no pudo optimizarse. Pruebe otra imagen.")
                        dimensions = tuple(max(1, int(side * 0.8)) for side in optimized.size)
                        optimized = optimized.resize(dimensions, Image.Resampling.LANCZOS)
        except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning):
            raise PhotoStorageError("La foto no pudo validarse u optimizarse. Pruebe otra imagen.") from None
        stored_name = f"productos/{uuid4().hex}.webp"
        self._request("POST", "object/" + self._path(stored_name), data=encoded, content_type="image/webp")
        return stored_name

    def _open(self, name, mode="rb"):
        if mode not in ("r", "rb"):
            raise ValueError("El almacenamiento de fotos solo admite lectura.")
        response = self._request("GET", "object/" + self._path(name))
        if len(response.content) > MAX_BYTES:
            raise PhotoStorageError("La foto excede el límite permitido.")
        return ContentFile(response.content, name=name)

    def exists(self, name):
        # jsfetch del runtime WASM intenta leer un body en HEAD (que es null).
        # Los metadatos permiten comprobar existencia sin descargar la foto.
        return self._request("GET", "object/info/" + self._path(name), missing_ok=True) is not None

    def size(self, name):
        response = self._request("GET", "object/info/" + self._path(name))
        try:
            size = int(response.json()["size"])
            if size < 0:
                raise ValueError
            return size
        except (ValueError, KeyError, TypeError):
            raise PhotoStorageError("No se pudo obtener el tamaño de la foto.") from None

    def url(self, name):
        response = self._request("POST", "object/sign/" + self._path(name),
                                 data=json.dumps({"expiresIn": self.expires_in}).encode(),
                                 content_type="application/json")
        try:
            signed = response.json()["signedURL"]
            parsed = urlsplit(signed)
            expected = "/object/sign/" + self._path(name)
            if parsed.scheme or parsed.netloc or parsed.path != expected or not parsed.query or parsed.fragment:
                raise ValueError
            return self.base_url + "/storage/v1" + signed
        except (ValueError, KeyError, TypeError):
            raise PhotoStorageError("No se pudo preparar el acceso temporal a la foto.") from None

    def delete(self, name):
        raise NotImplementedError("La eliminación de objetos requiere un procedimiento autorizado.")
