"""Crea un paquete de subida sin secretos, entornos, referencias ni datos locales."""
from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / ".local" / "railway-app"
if DEST.exists():
    raise SystemExit("El paquete ya existe; revisarlo antes de regenerar.")
DEST.mkdir(parents=True)
for name in ("Dockerfile", ".dockerignore", "requirements.railway.txt", "manage.py"):
    shutil.copy2(ROOT / name, DEST / name)
shutil.copytree(ROOT / "catalogo", DEST / "catalogo",
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "tests*.py", "README.md"))
(DEST / "config" / "storage").mkdir(parents=True)
for name in ("__init__.py", "settings_base.py", "settings_railway.py", "settings_static_build.py",
             "railway_settings.py", "railway_middleware.py", "runtime_settings.py", "urls.py", "wsgi.py"):
    shutil.copy2(ROOT / "config" / name, DEST / "config" / name)
for name in ("__init__.py", "supabase.py"):
    shutil.copy2(ROOT / "config" / "storage" / name, DEST / "config" / "storage" / name)
(DEST / "ops").mkdir()
shutil.copy2(ROOT / "ops" / "supabase-root-2021.crt", DEST / "ops" / "supabase-root-2021.crt")
(DEST / "scripts").mkdir()
shutil.copy2(ROOT / "scripts" / "railway_start.py", DEST / "scripts" / "railway_start.py")
files = [p for p in DEST.rglob("*") if p.is_file()]
for path in files:
    if path.suffix == ".json":
        json.loads(path.read_text())
    if any(part.startswith(".env") or part in (".local", ".venv", "node_modules")
           for part in path.relative_to(DEST).parts):
        raise SystemExit("Se encontró un archivo excluido; no subir este paquete.")
print(json.dumps({"package": str(DEST), "files": len(files),
                  "bytes": sum(p.stat().st_size for p in files), "uploaded": False}))
