#!/usr/bin/env python3
"""Storage desde workerd local; lectura por defecto y carga sintética explícita."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--upload-synthetic', action='store_true',
                    help='Carga tres fotos sintéticas al bucket de prueba Supabase autorizado.')
args = parser.parse_args()
BUILD = ROOT / '.local' / 'worker-storage-read'
attempt_number = 1
while BUILD.exists():
    attempt_number += 1
    BUILD = ROOT / '.local' / f'worker-storage-read-{attempt_number}'
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_supabase_test'
os.environ['JYZ_REMOTE_ROLE'] = 'jyz_app'
import sys
sys.path.insert(0, str(ROOT))
import django
django.setup()
from catalogo.models import Producto
from django.core.files.storage import default_storage
from django.db import connections
product = Producto.objects.get(pk=1)
assert product.es_ejemplo and not product.publicado
with default_storage.open(product.foto.name, 'rb') as photo:
    native_bytes = photo.read()
name = product.foto.name
connections.close_all()
BUILD.mkdir(parents=True)
shutil.copytree(ROOT / 'config', BUILD / 'src' / 'config',
    ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'tests*.py', 'settings*.py', 'local_*.py'))
for directory in ('python_modules', 'node_modules'):
    (BUILD / directory).symlink_to(ROOT / '.local' / 'worker-app' / directory, target_is_directory=True)
manifest = {'name': 'jyz-storage-read-local', 'main': 'src/entry.py',
            'compatibility_date': '2026-10-07', 'compatibility_flags': ['python_workers'],
            'workers_dev': False, 'preview_urls': False,
            'vars': {'PHOTO_NAME': name, 'UPLOAD_SYNTHETIC': str(args.upload_synthetic).lower()},
            'python_modules': {'exclude': ['**/*.pyc', '**/__pycache__/**', 'node_modules/**']}}
(BUILD / 'wrangler.jsonc').write_text(json.dumps(manifest, indent=2))
(BUILD / 'src' / 'entry.py').write_text('''import hashlib, json, secrets, traceback
from urllib.parse import urlsplit
from workers import Response, WorkerEntrypoint
class Default(WorkerEntrypoint):
    async def fetch(self, request):
        if urlsplit(str(request.url)).hostname != '127.0.0.1':
            return Response('Restringido', status=403)
        if not secrets.compare_digest(request.headers.get('X-Probe-Token') or '', self.env.PROBE_TOKEN):
            return Response('Restringido', status=403)
        try:
            from config.storage.supabase import SupabasePrivateStorage
            storage=SupabasePrivateStorage('https://kcahxuvfmrzxzlnpezyf.supabase.co',
                'jyz-prueba-fotos', self.env.SUPABASE_STORAGE_KEY)
            exists=storage.exists(self.env.PHOTO_NAME)
            size=storage.size(self.env.PHOTO_NAME)
            with storage.open(self.env.PHOTO_NAME, 'rb') as photo:
                data=photo.read()
            import httpx
            signed=storage.url(self.env.PHOTO_NAME)
            signed_response=httpx.get(signed,timeout=15,follow_redirects=False)
            public_response=httpx.get(storage.base_url+'/storage/v1/object/public/'+
                storage._path(self.env.PHOTO_NAME),timeout=15,follow_redirects=False)
            result={'status':'passed', 'exists':exists, 'bytes':len(data),
                'size_matches':size==len(data), 'sha256':hashlib.sha256(data).hexdigest(),
                'signed_read_matches':signed_response.status_code==200 and signed_response.content==data,
                'public_denied':not 200 <= public_response.status_code < 300}
            if self.env.UPLOAD_SYNTHETIC=='true':
                from io import BytesIO
                from PIL import Image
                from django.conf import settings
                from django.core.files.base import ContentFile
                from config.storage.supabase import PhotoStorageError
                if not settings.configured:
                    settings.configure()
                uploads=[]
                for fmt in ('PNG','JPEG','WEBP'):
                    stream=BytesIO()
                    Image.new('RGB',(16,16),(240,80,20)).save(stream,format=fmt)
                    original=stream.getvalue()
                    stored=storage.save('prueba.'+fmt.lower(),ContentFile(original))
                    with storage.open(stored,'rb') as photo:
                        recovered=photo.read()
                    signed_result=httpx.get(storage.url(stored),timeout=15,follow_redirects=False)
                    uploads.append({'format':fmt,'object':stored,'bytes':len(recovered),
                        'same_bytes':recovered==original,
                        'sha256':hashlib.sha256(recovered).hexdigest(),
                        'exists':storage.exists(stored),
                        'size_matches':storage.size(stored)==len(original),
                        'signed_read_matches':signed_result.status_code==200 and signed_result.content==original})
                result['uploads']=uploads
                try:
                    storage.save('corrupta.png',ContentFile(b'No es una imagen'))
                    result['corrupt_rejected']=False
                except PhotoStorageError:
                    result['corrupt_rejected']=True
            return Response(json.dumps(result),headers={'Content-Type':'application/json'})
        except Exception as error:
            return Response(json.dumps({'status':'failed','error_type':type(error).__name__,
                'attribute':getattr(error,'name',None),
                'frames':[{'file':frame.filename.rsplit('/',1)[-1], 'line':frame.lineno,
                    'function':frame.name} for frame in traceback.extract_tb(error.__traceback__)]}),
                status=500,headers={'Content-Type':'application/json'})
''')
token = secrets.token_urlsafe(32)
key = (ROOT / '.local' / 'supabase-prueba' / 'storage-key').read_text().strip()
fd = os.open(BUILD / '.dev.vars', os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
with os.fdopen(fd, 'w') as stream:
    stream.write('SUPABASE_STORAGE_KEY='+key+'\nPROBE_TOKEN='+token+'\n')
env = dict(os.environ, WRANGLER_SEND_METRICS='false')
import httpx
with (BUILD / 'dev.log').open('w') as log:
    process = subprocess.Popen([str(BUILD / 'node_modules' / '.bin' / 'wrangler'),
        'dev','--local','--ip','127.0.0.1','--port','8788'], cwd=BUILD,env=env,
        stdout=log, stderr=subprocess.STDOUT)
    try:
        for attempt in range(40):
            if process.poll() is not None:
                raise RuntimeError('El proceso local terminó; revisar dev.log sin exponer secretos.')
            try:
                response=httpx.get('http://127.0.0.1:8788/',headers={'X-Probe-Token':token},timeout=60)
                break
            except httpx.ConnectError:
                time.sleep(0.5)
        else:
            raise RuntimeError('No se pudo iniciar el puerto local de la prueba.')
        result=response.json()
        result['http_status']=response.status_code
        result['read_only']=not args.upload_synthetic
        result['runtime']='workerd local WebAssembly; no Hyperdrive ni despliegue'
        if result.get('status')=='passed':
            result['same_native_hash']=result['sha256']==hashlib.sha256(native_bytes).hexdigest()
            assert result['same_native_hash'] and result['exists'] and result['size_matches']
            assert result['signed_read_matches'] and result['public_denied']
            if args.upload_synthetic:
                assert len(result['uploads'])==3 and result['corrupt_rejected']
                assert all(photo['same_bytes'] and photo['exists'] and photo['size_matches']
                           and photo['signed_read_matches'] for photo in result['uploads'])
        (BUILD / 'result.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result))
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
raise SystemExit(0 if result.get('status')=='passed' else 1)
