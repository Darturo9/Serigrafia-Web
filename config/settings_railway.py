"""Servidor nativo Railway: falla al arrancar si falta configuración segura."""
import os
from .settings_base import *  # noqa: F403
from .railway_settings import build_railway_settings

globals().update(build_railway_settings(os.environ, BASE_DIR))
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "config.railway_middleware.ReviewAccessMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE[1:],
]

# Solo /admin/ exige acceso de revisión (ADR 014); los ejemplos nunca son cotizables.
JYZ_SHOW_REVIEW_EXAMPLES = False
