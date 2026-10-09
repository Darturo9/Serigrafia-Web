"""Arranque de servidor; no aplica migraciones ni crea usuarios."""
import os

port = int(os.environ.get("PORT", "8080"))
if not 1 <= port <= 65535:
    raise SystemExit("PORT inválido.")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings_railway")
os.execvp("gunicorn", ["gunicorn", "config.wsgi:application", "--bind", f"0.0.0.0:{port}",
                       "--workers", "1", "--worker-class", "sync", "--timeout", "60",
                       "--max-requests", "1000", "--max-requests-jitter", "100",
                       "--error-logfile", "-"])
