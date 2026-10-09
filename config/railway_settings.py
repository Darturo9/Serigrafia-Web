"""Configuración validada para la prueba Railway; sin lecturas de secretos locales."""
from pathlib import Path
import re
from urllib.parse import urlsplit

from django.core.exceptions import ImproperlyConfigured

from .runtime_settings import PROJECT_URL

POOLER = "aws-1-us-west-2.pooler.supabase.com"
APP_USER = "jyz_app.kcahxuvfmrzxzlnpezyf"


def build_railway_settings(env, base_dir):
    def required(name, minimum=1):
        value = env.get(name, "")
        if len(value) < minimum:
            raise ImproperlyConfigured(f"Configurar {name} para la prueba Railway.")
        return value

    origin = required("JYZ_REVIEW_ORIGIN")
    parsed = urlsplit(origin)
    if (parsed.scheme != "https" or not parsed.hostname
            or not re.fullmatch(r"[a-z0-9]+(?:[a-z0-9.-]*[a-z0-9])?", parsed.hostname)
            or parsed.username or parsed.password
            or parsed.port or parsed.path not in ("", "/") or parsed.query or parsed.fragment):
        raise ImproperlyConfigured("El origen de revisión requiere HTTPS y un host concreto.")
    for name, expected in (("PGHOST", POOLER), ("PGUSER", APP_USER), ("PGDATABASE", "postgres"),
                           ("PGPORT", "5432"), ("JYZ_DB_SCHEMA", "jyz_prueba"),
                           ("SUPABASE_URL", PROJECT_URL)):
        if required(name) != expected:
            raise ImproperlyConfigured(f"{name} no coincide con el destino autorizado.")
    ca_path = Path(required("PGSSLROOTCERT"))
    if not ca_path.is_file():
        raise ImproperlyConfigured("Falta la CA pública para verificar PostgreSQL.")
    review_user = required("JYZ_REVIEW_USER")
    if ":" in review_user or "\n" in review_user:
        raise ImproperlyConfigured("Usuario de revisión inválido.")
    launch = env.get("JYZ_PUBLIC_LAUNCH", "0")
    if launch not in {"0", "1"}:
        raise ImproperlyConfigured("JYZ_PUBLIC_LAUNCH debe ser 0 o 1.")
    return {
        "JYZ_PUBLIC_LAUNCH": launch == "1",
        "SECRET_KEY": required("DJANGO_SECRET_KEY", 50), "DEBUG": False,
        "ALLOWED_HOSTS": [parsed.hostname, "healthcheck.railway.app"],
        "CSRF_TRUSTED_ORIGINS": [origin.rstrip("/")],
        "JYZ_REVIEW_USER": review_user, "JYZ_REVIEW_PASSWORD": required("JYZ_REVIEW_PASSWORD", 24),
        "SESSION_COOKIE_SECURE": True, "CSRF_COOKIE_SECURE": True,
        "SESSION_COOKIE_HTTPONLY": True, "SESSION_COOKIE_SAMESITE": "Lax",
        "SECURE_SSL_REDIRECT": True, "SECURE_REDIRECT_EXEMPT": [r"^healthz/$"],
        "SECURE_PROXY_SSL_HEADER": ("HTTP_X_FORWARDED_PROTO", "https"),
        "SECURE_CONTENT_TYPE_NOSNIFF": True, "SECURE_REFERRER_POLICY": "same-origin",
        "SECURE_HSTS_SECONDS": 3600, "SECURE_HSTS_INCLUDE_SUBDOMAINS": False,
        "SECURE_HSTS_PRELOAD": False,
        "STATIC_ROOT": Path(base_dir) / "staticfiles", "MEDIA_URL": "/media/",
        "MEDIA_ROOT": "/tmp/jyz-media-unused",
        "STORAGES": {
            "default": {"BACKEND": "config.storage.supabase.SupabasePrivateStorage", "OPTIONS": {
                "base_url": PROJECT_URL, "bucket": "jyz-prueba-fotos",
                "key": required("SUPABASE_STORAGE_KEY")}},
            "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
        },
        "DATABASES": {"default": {
            "ENGINE": "django.db.backends.postgresql", "NAME": "postgres", "HOST": POOLER,
            "USER": APP_USER, "PASSWORD": required("PGPASSWORD"), "PORT": "5432",
            "CONN_MAX_AGE": 0, "DISABLE_SERVER_SIDE_CURSORS": True,
            "OPTIONS": {"sslmode": "verify-full", "sslrootcert": str(ca_path), "connect_timeout": 10,
                        "options": "-c search_path=jyz_prueba", "prepare_threshold": None},
        }},
    }
