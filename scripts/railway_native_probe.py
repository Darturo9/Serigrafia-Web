"""Prueba nativa local de solo lectura: Gunicorn, TLS PostgreSQL y assets.

Ejecutar con el Python aislado de Railway tras autorizar su instalación.
No despliega, aplica migraciones, crea sesiones ni carga fotos.
"""
import base64
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import sys
import time

import httpx

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / ".local" / "railway-prueba"
EVIDENCE.mkdir(parents=True, exist_ok=True)
access = json.loads((ROOT / ".local" / "supabase-prueba" / "jyz_app.json").read_text())
if access["project"] != "kcahxuvfmrzxzlnpezyf" or access["schema"] != "jyz_prueba":
    raise SystemExit("Credenciales fuera de la prueba autorizada.")
review_password = secrets.token_urlsafe(32)
env = dict(os.environ, DJANGO_SETTINGS_MODULE="config.settings_railway",
           DJANGO_SECRET_KEY=secrets.token_urlsafe(64), JYZ_REVIEW_ORIGIN="https://127.0.0.1",
           JYZ_REVIEW_USER="jyz-revision", JYZ_REVIEW_PASSWORD=review_password,
           PGDATABASE=access["database"], PGHOST=access["host"], PGUSER=access["user"],
           PGPASSWORD=access["password"], PGPORT=str(access["port"]), JYZ_DB_SCHEMA=access["schema"],
           PGSSLROOTCERT=str(ROOT / "ops" / "supabase-root-2021.crt"),
           SUPABASE_URL="https://kcahxuvfmrzxzlnpezyf.supabase.co",
           SUPABASE_STORAGE_KEY=(ROOT / ".local" / "supabase-prueba" / "storage-key").read_text().strip())
build_env = dict(os.environ, DJANGO_SETTINGS_MODULE="config.settings_static_build")
with (EVIDENCE / "collectstatic.log").open("w") as output:
    subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], cwd=ROOT,
                   env=build_env, stdout=output, stderr=subprocess.STDOUT, check=True)
auth = "Basic " + base64.b64encode(("jyz-revision:" + review_password).encode()).decode()
result = {"scope": "Gunicorn local y Supabase solo lectura", "checks": {}, "remote_deployment": False}
process = None
try:
    with (EVIDENCE / "gunicorn-local.log").open("w") as output:
        process = subprocess.Popen([sys.executable, "-m", "gunicorn", "config.wsgi:application",
                                    "--bind", "127.0.0.1:8790", "--workers", "1", "--timeout", "60"],
                                   cwd=ROOT, env=env, stdout=output, stderr=subprocess.STDOUT)
        with httpx.Client(base_url="http://127.0.0.1:8790", timeout=30, follow_redirects=False,
                          headers={"X-Forwarded-Proto": "https"}) as client:
            for _ in range(100):
                if process.poll() is not None:
                    raise RuntimeError("El servidor terminó antes de la comprobación.")
                try:
                    response = client.get("/healthz/")
                    break
                except httpx.ConnectError:
                    time.sleep(.1)
            else:
                raise RuntimeError("El servidor no inició a tiempo.")
            assert response.status_code == 200 and response.json() == {"status": "ok"}
            result["checks"]["postgres_tls_health"] = True
            for path in ("/inicio/", "/admin/login/", "/static/admin/css/base.css"):
                response = client.get(path)
                assert response.status_code == 401 and "noindex" in response.headers["X-Robots-Tag"]
            result["checks"]["anonymous_pages_admin_assets_denied"] = True
            response = client.get("/inicio/", headers={"Authorization": auth})
            assert response.status_code == 200 and "JYZ" in response.text
            result["checks"]["catalogue_native_orm_read"] = True
            response = client.get("/admin/login/", headers={"Authorization": auth})
            assert response.status_code == 200 and "csrfmiddlewaretoken" in response.text
            assert "Secure" in response.headers.get("set-cookie", "")
            result["checks"]["admin_login_and_secure_csrf_cookie"] = True
            match = re.search(r'href="(/static/admin/css/base\.[^"/]+\.css)"', response.text)
            assert match, "El Admin no usó el manifest de estáticos."
            response = client.get(match.group(1), headers={"Authorization": auth})
            assert response.status_code == 200 and "text/css" in response.headers["content-type"]
            result["checks"]["authenticated_whitenoise_manifest_asset"] = True
            response = client.get("/inicio/", headers={"Authorization": "Basic incorrect"})
            assert response.status_code == 401
            result["checks"]["invalid_review_denied"] = True
            response = client.get("/inicio/", headers={"Authorization": auth, "X-Forwarded-Proto": "http"})
            assert response.status_code == 301 and response.headers["location"].startswith("https://")
            result["checks"]["https_redirect"] = True
finally:
    if process is not None and process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
    result["server_stopped"] = process is not None and process.poll() is not None
    result["passed"] = len(result["checks"]) == 7 and all(result["checks"].values())
    (EVIDENCE / "native-readonly.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
