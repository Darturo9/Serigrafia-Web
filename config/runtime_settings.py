"""Construye settings desde bindings, sin leer credenciales de otros proyectos."""
import re
from urllib.parse import urlsplit
from django.core.exceptions import ImproperlyConfigured

PROJECT_URL = "https://kcahxuvfmrzxzlnpezyf.supabase.co"
LOCAL_HOSTS = {"127.0.0.1", "localhost", "[::1]"}


def required(env, name):
    value = getattr(env, name, None)
    if not value or not isinstance(value, str):
        raise ImproperlyConfigured(f"Falta configurar {name} para la prueba Workers.")
    return value


def build_worker_settings(env):
    local = getattr(env, "JYZ_WORKER_LOCAL", "false") == "true"
    secret = required(env, "DJANGO_SECRET_KEY")
    if len(secret) < 50:
        raise ImproperlyConfigured("DJANGO_SECRET_KEY debe tener al menos 50 caracteres.")
    origin = required(env, "JYZ_REVIEW_ORIGIN")
    parsed = urlsplit(origin)
    if parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in ("", "/"):
        raise ImproperlyConfigured("JYZ_REVIEW_ORIGIN debe ser un origen sin ruta ni credenciales.")
    if local:
        if parsed.scheme != "http" or parsed.hostname not in {"localhost", "127.0.0.1", "::1"}:
            raise ImproperlyConfigured("La prueba local Workers solo admite origen HTTP de loopback.")
    elif parsed.scheme != "https" or not parsed.hostname or parsed.hostname in {"localhost", "127.0.0.1", "::1"}:
        raise ImproperlyConfigured("La prueba remota requiere un origen HTTPS concreto.")
    hd = getattr(env, "HYPERDRIVE", None)
    if hd is None:
        raise ImproperlyConfigured("Falta binding HYPERDRIVE.")
    db = {name: getattr(hd, name, None) for name in ("host", "port", "user", "password", "database")}
    if any(not v for v in db.values()):
        raise ImproperlyConfigured("Binding HYPERDRIVE incompleto.")
    schema = getattr(env, "JYZ_DB_SCHEMA", "jyz_worker_local" if local else "jyz_prueba")
    if not re.fullmatch(r"[a-z][a-z0-9_]{0,62}", schema) or (not local and schema != "jyz_prueba"):
        raise ImproperlyConfigured("La prueba remota solo admite el esquema jyz_prueba.")
    if not local:
        required(env, "JYZ_REVIEW_USER")
        if len(required(env, "JYZ_REVIEW_PASSWORD")) < 24:
            raise ImproperlyConfigured("La contraseña de revisión requiere al menos 24 caracteres.")
        if required(env, "SUPABASE_URL") != PROJECT_URL:
            raise ImproperlyConfigured("SUPABASE_URL no corresponde al proyecto autorizado.")
        required(env, "SUPABASE_STORAGE_KEY")
    storage = {"BACKEND": "django.core.files.storage.InMemoryStorage"} if local else {
        "BACKEND": "config.storage.supabase.SupabasePrivateStorage",
        "OPTIONS": {"base_url": PROJECT_URL, "bucket": "jyz-prueba-fotos",
                    "key": required(env, "SUPABASE_STORAGE_KEY")},
    }
    return {
        "SECRET_KEY": secret, "DEBUG": False,
        "ALLOWED_HOSTS": [parsed.hostname], "CSRF_TRUSTED_ORIGINS": [origin.rstrip("/")],
        "SESSION_COOKIE_SECURE": not local, "CSRF_COOKIE_SECURE": not local,
        "SESSION_COOKIE_HTTPONLY": True, "SESSION_COOKIE_SAMESITE": "Lax",
        "SECURE_CONTENT_TYPE_NOSNIFF": True, "SECURE_REFERRER_POLICY": "same-origin",
        "JYZ_WORKER_LOCAL": local, "DEBUG_PROPAGATE_EXCEPTIONS": local,
        "MEDIA_URL": "/media/", "MEDIA_ROOT": "/tmp/jyz-media",
        "STORAGES": {"default": storage,
                     "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"}},
        "DATABASES": {"default": {
            "ENGINE": "django.db.backends.postgresql", "NAME": str(db["database"]),
            "USER": str(db["user"]), "PASSWORD": str(db["password"]), "HOST": str(db["host"]),
            "PORT": str(db["port"]), "CONN_MAX_AGE": 0, "DISABLE_SERVER_SIDE_CURSORS": True,
            # Hyperdrive termina TLS al origen; este tramo conecta al binding interno.
            "OPTIONS": {"sslmode": "disable", "connect_timeout": 5,
                        "options": f"-c search_path={schema}", "prepare_threshold": None},
        }},
    }
