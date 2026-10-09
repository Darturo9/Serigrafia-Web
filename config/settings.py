"""Configuración de prueba local; no es configuración de publicación."""
import os
from django.core.exceptions import ImproperlyConfigured
from .settings_base import *  # noqa: F403

LOCAL_DIR = BASE_DIR / ".local"
LOCAL_DIR.mkdir(exist_ok=True)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "solo-prueba-local-no-publicar-esta-configuracion")
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
backend = os.environ.get("DB_BACKEND", "sqlite")
if backend == "sqlite":
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": LOCAL_DIR / "db.sqlite3"}}
elif backend == "postgres":
    required = ["PGDATABASE", "PGUSER", "PGPASSWORD", "PGHOST"]
    if any(not os.environ.get(key) for key in required):
        raise ImproperlyConfigured("La configuración PostgreSQL requiere PGDATABASE, PGUSER, PGPASSWORD y PGHOST.")
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["PGDATABASE"], "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"], "HOST": os.environ["PGHOST"],
        "PORT": os.environ.get("PGPORT", "5432"), "CONN_MAX_AGE": 0,
        "OPTIONS": {"sslmode": os.environ.get("PGSSLMODE", "require"), "connect_timeout": 5},
    }}
else:
    raise ImproperlyConfigured("DB_BACKEND debe ser sqlite o postgres.")
MEDIA_URL = "/media/"
MEDIA_ROOT = LOCAL_DIR / "media"
