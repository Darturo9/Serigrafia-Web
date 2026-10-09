#!/usr/bin/env python3
"""Comandos limitados a PostgreSQL local de este proyecto; no cargan .env externos."""
import argparse
import os
from pathlib import Path
import secrets
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".local" / "postgres.env"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("command", choices=["db-start", "db-stop", "migrate", "check", "test", "runtime-test", "role", "admin", "serve", "demo", "persistencia"])
args = parser.parse_args()
if args.command == "db-start":
    if not ENV_FILE.exists():
        ENV_FILE.parent.mkdir(exist_ok=True)
        descriptor = os.open(ENV_FILE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w") as stream:
            stream.write("POSTGRES_PASSWORD=" + secrets.token_urlsafe(32) + "\n")
    # Esta imagen ya estaba instalada. No usar contenedores de otros proyectos.
    command = ["docker", "compose", "--env-file", str(ENV_FILE), "-f", str(ROOT / "compose.local.yaml"), "up", "-d", "--wait", "--pull", "never"]
elif args.command == "db-stop":
    command = ["docker", "compose", "--env-file", str(ENV_FILE), "-f", str(ROOT / "compose.local.yaml"), "stop"]
else:
    if not ENV_FILE.exists():
        parser.error("Primero ejecutar db-start. No se conectará a una base alternativa.")
    password = ENV_FILE.read_text().strip().partition("=")[2]
    env = dict(os.environ)
    env.update(DB_BACKEND="postgres", PGHOST="127.0.0.1", PGPORT="55439", PGDATABASE="serigrafia_local", PGUSER="serigrafia_local", PGPASSWORD=password, PGSSLMODE="disable")
    mapping = {"runtime-test": ["test", "catalogo", "config.tests_runtime", "--verbosity", "1"], "migrate": ["migrate"], "check": ["check"], "test": ["test", "catalogo", "--verbosity", "1"], "role": ["preparar_rol_catalogo"], "admin": ["createsuperuser"], "serve": ["runserver", "127.0.0.1:8000", "--noreload"], "demo": ["crear_demo_local"], "persistencia": ["verificar_persistencia_local"]}
    command = [sys.executable, str(ROOT / "manage.py"), *mapping[args.command]]
    raise SystemExit(subprocess.call(command, env=env, cwd=ROOT))
raise SystemExit(subprocess.call(command, cwd=ROOT))
