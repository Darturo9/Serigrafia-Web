"""ADR 019: altas nuevas autorizadas; no migra, borra ni cambia productos previos."""
import os, sys, json, hashlib, argparse
from pathlib import Path
from io import BytesIO
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--apply', action='store_true', required=True)
args = parser.parse_args()
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_supabase_test'
os.environ['JYZ_REMOTE_ROLE'] = 'jyz_app'
import django
django.setup()
from django.db import transaction
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from catalogo.models import Producto, ProductoImagen, GaleriaImagen
from PIL import Image, ImageOps
folder = ROOT / '.local/catalogo-real'
manifest = json.loads((ROOT / 'assets/catalogo-recibido/seleccion.json').read_text())
selected = [i for i in manifest if i['publicar']]
assert len(selected) == 11
control = folder / 'carga.json'
result = json.loads(control.read_text()) if control.exists() else []
baseline_file = folder / 'baseline.json'
if not baseline_file.exists():
    baseline_file.write_text(json.dumps({'productos': list(Producto.objects.values()),
        'imagenes': list(ProductoImagen.objects.values()), 'galeria': list(GaleriaImagen.objects.values())}, default=str, indent=2))
baseline = json.loads(baseline_file.read_text())
for order, item in enumerate(selected, 1):
    previous = next((r for r in result if r['source_sha256'] == item['sha256']), None)
    if previous:
        p = Producto.objects.get(pk=previous['product_id'])
        assert p.nombre == item['nombre'] and p.publicado and not p.es_ejemplo
        continue
    assert not Producto.objects.filter(nombre=item['nombre']).exists(), 'Revisar ficha existente antes de duplicar'
    path = ROOT / 'assets/catalogo-recibido' / item['file']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']
    # Copia de transporte para respetar el límite de entrada del backend; no mejora IA.
    with Image.open(path) as source:
        photo = ImageOps.exif_transpose(source).convert('RGB')
        photo.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
        stream = BytesIO(); photo.save(stream, format='PNG')
    with transaction.atomic():
        p = Producto(nombre=item['nombre'], descripcion=item['descripcion'], categoria=item['categoria'],
            tallas=['Todas las tallas'], publicado=False, es_ejemplo=False, orden=order)
        p.full_clean(); p.save()
        image = ProductoImagen(producto=p, descripcion=item['descripcion'].split(' Todas las tallas')[0], orden=0, activo=True)
        image.foto.save('catalogo.png', ContentFile(stream.getvalue()), save=False)
        image.full_clean(); image.save()
        p.portada=image; p.publicado=True; p.full_clean(); p.save()
    stored = default_storage.open(image.foto.name).read()
    with Image.open(BytesIO(stored)) as im:
        assert im.format=='WEBP' and max(im.size)<=1600 and len(stored)<=500*1024
        dimensions=im.size
    result.append({'product_id':p.pk,'image_id':image.pk,'nombre':p.nombre,'source':item['file'],
        'source_sha256':item['sha256'],'object':image.foto.name,'bytes':len(stored),'dimensions':dimensions,
        'stored_sha256':hashlib.sha256(stored).hexdigest()})
    control.write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps({'creado':p.pk,'nombre':p.nombre,'webp_bytes':len(stored)}), flush=True)
for model, key in [(Producto,'productos'), (ProductoImagen,'imagenes'), (GaleriaImagen,'galeria')]:
    current = list(model.objects.filter(pk__in=[r['id'] for r in baseline[key]]).values())
    assert json.loads(json.dumps(current,default=str)) == baseline[key], f'Datos previos cambiados: {key}'
assert Producto.objects.filter(publicado=True,es_ejemplo=False).count() == 11
(folder/'preservacion.json').write_text(json.dumps({'registros_previos_identicos':True,'productos_nuevos':11,'fotos_nuevas':11,'excluidas':5,'duplicados_omitidos':1}))
print('11 fichas publicadas y leídas; registros anteriores y galería idénticos.')
