"""Media de prueba en memoria; ruta habilitada únicamente para Worker loopback."""
import mimetypes
from django.core.files.storage import default_storage
from django.http import FileResponse, Http404
from django.conf import settings


def local_media(request, name):
    if not getattr(settings, "JYZ_WORKER_LOCAL", False) or not name.startswith("productos/"):
        raise Http404
    try:
        stream = default_storage.open(name, "rb")
    except FileNotFoundError:
        raise Http404 from None
    return FileResponse(stream, content_type=mimetypes.guess_type(name)[0] or "application/octet-stream")
