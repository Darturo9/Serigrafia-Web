"""Prueba Workers, con bindings obligatorios; no usar para migrate/collectstatic."""
from workers import env
from .settings_base import *  # noqa: F403
from .runtime_settings import build_worker_settings

globals().update(build_worker_settings(env))

PASSWORD_HASHERS = ["config.worker_hashers.WorkerPBKDF2PasswordHasher"]
