"""Entrada de prueba: acceso protegido y operaciones Django serializadas."""
import base64
import os
import secrets
import time
from urllib.parse import urlsplit

from workers import Response, WorkerEntrypoint, wsgi

_busy = False
_application = None


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        local = getattr(self.env, "JYZ_WORKER_LOCAL", "false") == "true"
        host = urlsplit(str(request.url)).hostname
        if local:
            if host not in {"localhost", "127.0.0.1", "::1"}:
                return Response("Prueba local restringida.", status=403)
        else:
            user = getattr(self.env, "JYZ_REVIEW_USER", "")
            password = getattr(self.env, "JYZ_REVIEW_PASSWORD", "")
            if not user or not password:
                return Response("Prueba sin configurar.", status=503)
            expected = "Basic " + base64.b64encode((user + ":" + password).encode()).decode()
            actual = request.headers.get("Authorization") or ""
            if not secrets.compare_digest(str(actual).encode(), expected.encode()):
                return Response("Acceso de revisión requerido.", status=401,
                                headers={"WWW-Authenticate": 'Basic realm="Revision JYZ", charset="UTF-8"',
                                         "Cache-Control": "no-store", "X-Robots-Tag": "noindex, nofollow"})
        if urlsplit(str(request.url)).path.startswith("/static/"):
            return await self.env.ASSETS.fetch(request)
        # Un solo contexto síncrono del ORM por isolate; no compartir transacciones simultáneas.
        global _busy, _application
        # Cada espera debe tener un timer del contexto de esta petición. Un
        # asyncio.Lock compartido dejó peticiones canceladas como "hung" en workerd.
        from js import scheduler
        start = time.monotonic()
        while _busy:
            if time.monotonic() - start > 5:
                return Response("La prueba está ocupada. Intente de nuevo.", status=503,
                                headers={"Retry-After": "1", "Cache-Control": "no-store"})
            await scheduler.wait(5)
        _busy = True
        try:
            if _application is None:
                os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings_workers"
                # WSGI vive en el event loop de Workers (sin threads). El lock abarca
                # todas las operaciones Django: ORM, sesiones, transacciones y cierre.
                os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
                from django.core.wsgi import get_wsgi_application
                _application = get_wsgi_application()
            from django.db import connections
            try:
                return await wsgi.fetch(_application, request, self.env)
            finally:
                connections.close_all()
        finally:
            _busy = False
