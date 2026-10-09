"""Prueba nativa Django+Storage autorizada, sin borrar objetos ni mostrar claves/URLs."""
from pathlib import Path
import os,sys,json,hashlib
from io import BytesIO
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
os.environ['DJANGO_SETTINGS_MODULE']='config.settings_supabase_test'
os.environ['JYZ_REMOTE_ROLE']='jyz_app'
import django
django.setup()
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from catalogo.models import Producto
from config.storage.supabase import PhotoStorageError
from PIL import Image
import httpx

def main():
    product=Producto.objects.get(pk=1,es_ejemplo=True,publicado=False)
    results=[]
    for fmt in ('PNG','JPEG','WEBP'):
        stream=BytesIO()
        Image.new('RGB',(40,40),(238,120,24)).save(stream,format=fmt)
        data=stream.getvalue()
        product.foto.save('foto-sintetica.'+fmt.lower(),ContentFile(data),save=True)
        product.refresh_from_db()
        name=product.foto.name
        assert default_storage.exists(name)
        assert default_storage.size(name)==len(data)
        assert default_storage.open(name).read()==data
        signed=default_storage.url(name)
        response=httpx.get(signed,timeout=15,follow_redirects=False)
        assert response.status_code==200 and response.content==data
        public='https://kcahxuvfmrzxzlnpezyf.supabase.co/storage/v1/object/public/jyz-prueba-fotos/'+name
        assert httpx.get(public,timeout=15).status_code != 200
        results.append({'format':fmt,'object':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'signed_read':True,'public_denied':True})
    old=product.foto.name
    try:
        product.foto.save('corrupta.png',ContentFile(b'not an image'),save=True)
    except PhotoStorageError:
        pass
    else:
        raise AssertionError('Imagen corrupta aceptada')
    product.refresh_from_db()
    assert product.foto.name==old
    assert len({r['object'] for r in results})==3
    output={'status':'passed','product_id':product.pk,'files':results,'invalid_preserves_previous':True,
            'environment':'Django nativo + PostgreSQL y Storage Supabase; no Workers remoto'}
    (ROOT/'.local/supabase-prueba/fotos-result.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output))
try:
    main()
except Exception as exc:
    print(json.dumps({'status':'failed','error_type':type(exc).__name__,'details':'Error omitido para no exponer claves o URLs firmadas.'}))
    raise SystemExit(1)
