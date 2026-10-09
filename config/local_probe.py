"""Diagnóstico exclusivo del runtime local. No se registra en la prueba remota."""
from io import BytesIO
import platform
from uuid import uuid4
from django.conf import settings
from django.db import transaction
from django.http import Http404, JsonResponse
from PIL import Image
from catalogo.models import Producto


class RollbackProbe(Exception):
    pass


def local_probe(request):
    if not getattr(settings, "JYZ_WORKER_LOCAL", False):
        raise Http404
    marker = "__probe__" + uuid4().hex
    try:
        with transaction.atomic():
            Producto.objects.create(nombre=marker, descripcion="Diagnóstico local reversible")
            assert Producto.objects.filter(nombre=marker).exists()
            raise RollbackProbe
    except RollbackProbe:
        pass
    formats = []
    for fmt in ("JPEG", "PNG", "WEBP"):
        stream = BytesIO()
        Image.new("RGB", (8, 8), "orange").save(stream, format=fmt)
        with Image.open(BytesIO(stream.getvalue())) as image:
            image.verify()
            formats.append(image.format)
    return JsonResponse({"rollback": not Producto.objects.filter(nombre=marker).exists(),
                         "formats": formats, "python": platform.python_version()})
