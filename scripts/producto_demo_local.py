"""Ficha de prueba aislada. No conecta a Supabase ni a Railway."""
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ['DB_BACKEND'] = 'sqlite'
import django
django.setup()
from django.conf import settings
from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.contrib.auth.models import User
from catalogo.models import Producto, ProductoImagen

local = ROOT / '.local' / 'producto-demo'
local.mkdir(parents=True, exist_ok=True)
settings.DATABASES['default']['NAME'] = local / 'demo.sqlite3'
connection.settings_dict['NAME'] = settings.DATABASES['default']['NAME']
settings.MEDIA_ROOT = local / 'media'
settings.MEDIA_ROOT.mkdir(exist_ok=True)
settings.JYZ_SHOW_REVIEW_EXAMPLES = True
assets = ROOT / 'catalogo' / 'static' / 'catalogo' / 'galeria-referencias'
for archivo in assets.glob('*.webp'):
    shutil.copy2(archivo, settings.MEDIA_ROOT / archivo.name)
# Ensayo real: foto antigua -> migraciones nuevas, sin alterar su archivo.
executor = MigrationExecutor(connection)
if ('catalogo', '0002_productoimagen_producto_portada') not in executor.loader.applied_migrations:
    executor.migrate([('catalogo', '0001_initial')])
    modelos = executor.loader.project_state([('catalogo', '0001_initial')]).apps
    modelos.get_model('catalogo', 'Producto').objects.get_or_create(nombre='Fixture local · prueba de recorrido', defaults={'descripcion':'Datos ficticios exclusivamente locales para comprobar fotos, tallas y WhatsApp. No es un producto de JYZ.', 'categoria':'Prueba local', 'foto':'playeras-perchas.webp', 'texto_foto':'Playeras en perchas, referencia Pexels', 'publicado':True, 'tallas':['M','L']})
call_command('migrate', verbosity=0)
p = Producto.objects.get(nombre='Fixture local · prueba de recorrido')
if p.imagenes.count() == 1:
    for n, nombre in enumerate(['playeras-colores.webp', 'gorra-referencia.webp', 'playeras-perchas.webp', 'playeras-colores.webp', 'gorra-referencia.webp'], 1):
        ProductoImagen.objects.create(producto=p, foto=nombre, descripcion=f'Vista de prueba {n+1}, referencia Pexels', orden=n)
call_command('preparar_rol_catalogo', verbosity=0)
# Usuario de prueba solo local; contraseña aleatoria en archivo privado, sin imprimirla.
from django.contrib.auth.models import Group
import secrets
import json
acceso = local / 'editor.json'
if not acceso.exists():
    cred = {'username':'editor-local','password':secrets.token_urlsafe(24)}
    acceso.write_text(json.dumps(cred));acceso.chmod(0o600)
    editor = User.objects.create_user(cred['username'], password=cred['password'], is_staff=True)
    editor.groups.add(Group.objects.get(name='Responsable de catálogo'))
print(f'Fixture aislada: http://127.0.0.1:8002/productos/{p.pk}/')
call_command('runserver', '127.0.0.1:8002', use_reloader=False)
