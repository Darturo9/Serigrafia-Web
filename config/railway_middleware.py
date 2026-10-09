from config.publicacion import pagina_indexable
"""Protección de revisión antes de Django Admin y WhiteNoise."""
import base64
import secrets

from django.conf import settings
from django.db import DatabaseError, connection
from django.http import HttpResponse, JsonResponse

# ADR 020: el panel usa login Django; el catálogo técnico conserva Basic.
RUTAS_PROTEGIDAS = ("/catalogo/",)


class ReviewAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        credentials = settings.JYZ_REVIEW_USER + ":" + settings.JYZ_REVIEW_PASSWORD
        self.expected = b"Basic " + base64.b64encode(credentials.encode())

    def __call__(self, request):
        # Validar host incluso cuando se responde antes de CommonMiddleware.
        host = request.get_host().split(":", 1)[0]
        if request.path == "/healthz/" and request.method in ("GET", "HEAD"):
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
                response = JsonResponse({"status": "ok"})
            except DatabaseError:
                response = JsonResponse({"status": "unavailable"}, status=503)
        elif host == "healthcheck.railway.app":
            response = HttpResponse(status=404)
        elif not request.is_secure():
            # No aceptar Basic sobre HTTP, aunque se cambie SecurityMiddleware.
            response = HttpResponse(status=400)
        elif request.path.startswith(RUTAS_PROTEGIDAS) and not secrets.compare_digest(request.headers.get("Authorization", "").encode(), self.expected):
            response = HttpResponse("Acceso de revisión requerido.", status=401)
            response["WWW-Authenticate"] = 'Basic realm="Revision JYZ", charset="UTF-8"'
        else:
            response = self.get_response(request)
        if not pagina_indexable(request, response):
            response["X-Robots-Tag"] = "noindex, nofollow"
        elif "X-Robots-Tag" in response:
            del response["X-Robots-Tag"]
        response["Cache-Control"] = "no-store"
        return response
