#!/usr/bin/env python3
"""Prepara únicamente esquema local separado para la prueba Workers; no remoto."""
import json
import os
from pathlib import Path
import secrets
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
password = (ROOT / ".local" / "postgres.env").read_text().strip().partition("=")[2]
import psycopg
with psycopg.connect(host="127.0.0.1", port=55439, user="serigrafia_local", password=password,
                     dbname="serigrafia_local", sslmode="disable", connect_timeout=5) as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS jyz_worker_local AUTHORIZATION serigrafia_local")
os.environ.update(DJANGO_SETTINGS_MODULE="config.settings_worker_test", DB_BACKEND="postgres",
                  PGHOST="127.0.0.1", PGPORT="55439", PGDATABASE="serigrafia_local",
                  PGUSER="serigrafia_local", PGPASSWORD=password, PGSSLMODE="disable")
import django
django.setup()
from django.contrib.auth.models import User, Group
from django.core.management import call_command
call_command("migrate", verbosity=0)
call_command("preparar_rol_catalogo", verbosity=0)
credential_path = ROOT / ".local" / "worker-smoke-access.json"
if credential_path.exists():
    credential = json.loads(credential_path.read_text())
else:
    credential = {"username": "worker-smoke-editor", "password": secrets.token_urlsafe(32)}
    fd = os.open(credential_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as stream:
        json.dump(credential, stream)
user, _ = User.objects.get_or_create(username=credential["username"], defaults={"is_staff": True})
user.set_password(credential["password"])
user.save()
user.groups.add(Group.objects.get(name="Responsable de catálogo"))
print("Esquema jyz_worker_local, migraciones y editor sintético listos. Acceso no mostrado.")
