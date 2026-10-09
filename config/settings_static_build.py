"""Solo collectstatic: no importa credenciales ni se conecta a Supabase."""
from .settings_base import *  # noqa: F403

SECRET_KEY = "solo-recoleccion-estaticos-no-utilizar-como-servidor"
DEBUG = False
ALLOWED_HOSTS = []
STATIC_ROOT = BASE_DIR / "staticfiles"
DATABASES = {"default": {"ENGINE": "django.db.backends.dummy"}}
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.InMemoryStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
