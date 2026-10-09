#!/usr/bin/env python3
"""Preparar y ejecutar exclusivamente Worker local, sin comandos de publicación."""
import argparse
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / ".local" / "worker-app"
CLI = ROOT / ".local" / "workers-venv" / "bin" / "pywrangler"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("command", choices=["prepare", "sync", "dev"])
args = parser.parse_args()
if not CLI.exists():
    parser.error("Falta el entorno Workers autorizado. Consulte la guía.")
BUILD.mkdir(parents=True, exist_ok=True)
for module in ("config", "catalogo"):
    # Staging reproducible; los archivos fuente originales permanecen en ROOT.
    shutil.copytree(ROOT / module, BUILD / "src" / module, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
for src, dest in [("worker.py", "src/entry.py"), ("workers/pyproject.toml", "pyproject.toml"),
                  ("workers/wrangler.local.jsonc", "wrangler.jsonc"), ("workers/package.json", "package.json"),
                  ("workers/package-lock.json", "package-lock.json"), ("workers/pylock.toml", "pylock.toml")]:
    shutil.copyfile(ROOT / src, BUILD / dest)
static = ROOT / ".local" / "staticfiles"
if not static.is_dir():
    parser.error("Ejecutar collectstatic con el entorno Django local antes de preparar Workers.")
shutil.copytree(static, BUILD / "assets" / "static", dirs_exist_ok=True)
vars_file = BUILD / ".dev.vars"
if not vars_file.exists():
    descriptor = os.open(vars_file, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w") as stream:
        stream.write("DJANGO_SECRET_KEY=" + secrets.token_urlsafe(64) + "\n")
if args.command == "prepare":
    print("Worker local preparado en .local/worker-app; sin recursos remotos.")
    raise SystemExit(0)
secret_file = ROOT / ".local" / "postgres.env"
if not secret_file.exists():
    parser.error("Primero iniciar el PostgreSQL de prueba local.")
password = secret_file.read_text().strip().partition("=")[2]
from urllib.parse import quote
local_uri = "postgresql://serigrafia_local:" + quote(password, safe="") + "@127.0.0.1:55439/serigrafia_local"
env = dict(os.environ)
env["PATH"] = str(CLI.parent) + os.pathsep + env.get("PATH", "")
env["CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_HYPERDRIVE"] = local_uri
env["WRANGLER_SEND_METRICS"] = "false"
command = [str(CLI), args.command]
if args.command == "dev":
    command += ["--local", "--ip", "127.0.0.1", "--port", "8787"]
raise SystemExit(subprocess.call(command, cwd=BUILD, env=env))
