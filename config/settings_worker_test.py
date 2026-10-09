"""Configuración nativa para migrar/probar SOLO esquema local de Workers."""
from .settings import *  # noqa: F403
from django.core.exceptions import ImproperlyConfigured

if DATABASES["default"]["ENGINE"] != "django.db.backends.postgresql" or DATABASES["default"]["HOST"] != "127.0.0.1" or str(DATABASES["default"]["PORT"]) != "55439":
    raise ImproperlyConfigured("La prueba Workers solo puede preparar el PostgreSQL Docker de este proyecto.")
DATABASES["default"]["OPTIONS"]["options"] = "-c search_path=jyz_worker_local"
