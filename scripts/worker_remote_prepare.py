#!/usr/bin/env python3
"""Preparar y medir el paquete remoto sin instalar, autenticar ni publicar."""
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / '.local' / 'worker-remote-review'
LOCAL = ROOT / '.local' / 'worker-app'
WRANGLER = LOCAL / 'node_modules' / '.bin' / 'wrangler'
if not WRANGLER.exists() or not (LOCAL / 'python_modules').is_dir():
    raise SystemExit('Falta el entorno Workers ya autorizado; no se instalará automáticamente.')
if BUILD.exists():
    raise SystemExit('El paquete ya existe. Inspeccionarlo antes de preparar otra copia.')
BUILD.mkdir(parents=True)
excluded = shutil.ignore_patterns('__pycache__', '*.pyc', 'tests*.py',
    'settings.py', 'settings_supabase_test.py', 'settings_worker_test.py',
    'local_probe.py', 'local_media.py')
for module in ('config', 'catalogo'):
    shutil.copytree(ROOT / module, BUILD / 'src' / module, ignore=excluded)
shutil.copyfile(ROOT / 'worker.py', BUILD / 'src' / 'entry.py')
for name in ('pyproject.toml', 'pylock.toml', 'package.json', 'package-lock.json'):
    shutil.copyfile(ROOT / 'workers' / name, BUILD / name)
shutil.copytree(LOCAL / 'python_modules', BUILD / 'python_modules',
                ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
shutil.copytree(ROOT / '.local' / 'staticfiles', BUILD / 'assets' / 'static')
manifest = json.loads((ROOT / 'workers' / 'wrangler.remote.example.jsonc').read_text())
# Valores ficticios exclusivamente para validar el empaquetado sin recursos reales.
manifest['hyperdrive'][0]['id'] = '0' * 32
manifest['vars']['JYZ_REVIEW_ORIGIN'] = 'https://revision.invalid'
(BUILD / 'wrangler.jsonc').write_text(json.dumps(manifest, indent=2) + '\n')
for path in BUILD.rglob('*'):
    if path.is_file() and (path.name.startswith('.env') or path.name.startswith('.dev.vars')
                          or path.name in {'storage-key', 'jyz_app.json', 'jyz_migrator.json'}):
        raise SystemExit('Archivo local sensible detectado; no se ejecutó el empaquetado.')
env = dict(os.environ, WRANGLER_SEND_METRICS='false')
with (BUILD / 'dry-run.log').open('w') as log:
    result = subprocess.run([str(WRANGLER), 'deploy', '--dry-run', '--outdir', 'bundled'],
                            cwd=BUILD, env=env, stdout=log, stderr=subprocess.STDOUT)
assets = [p for p in (BUILD / 'assets').rglob('*') if p.is_file()]
summary = {'status': 'passed' if result.returncode == 0 else 'failed',
           'dry_run_only': True, 'remote_resources_created': False,
           'assets_count': len(assets), 'largest_asset_bytes': max(p.stat().st_size for p in assets),
           'secrets_copied': False, 'origin_and_hyperdrive_are_placeholders': True}
for line in (BUILD / 'dry-run.log').read_text().splitlines():
    if 'Total Upload:' in line:
        summary['bundle_size_output'] = line.strip()
(BUILD / 'result.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
raise SystemExit(result.returncode)
