"""Ejercita Admin nativo con datos/fotos sintéticos en Supabase autorizado."""
from pathlib import Path
import os,sys,json
from io import BytesIO
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
os.environ['DJANGO_SETTINGS_MODULE']='config.settings_supabase_test'
os.environ['JYZ_REMOTE_ROLE']='jyz_app'
import django
django.setup()
from django.test import Client,override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from catalogo.models import Producto
from PIL import Image
checks=[]
def check(label,condition):
    if not condition: raise AssertionError(label)
    checks.append(label)
access=json.loads((ROOT/'.local/supabase-prueba/editor.json').read_text())
try:
    with override_settings(ALLOWED_HOSTS=['testserver']):
        c=Client(enforce_csrf_checks=True)
        path='/admin/catalogo/producto/1/change/'
        check('anónimo restringido',c.get(path).status_code==302)
        check('login verificado',c.login(**access))
        check('panel disponible',c.get(path).status_code==200)
        check('sin gestión de usuarios',c.get('/admin/auth/user/').status_code==403)
        p=Producto.objects.get(pk=1,es_ejemplo=True)
        fields={'nombre':p.nombre,'descripcion':'Producto sintético para prueba de Admin remoto',
                'categoria':'PRUEBA','tallas':'["M"]','texto_foto':'Imagen sintética de prueba',
                'orden':'0','es_ejemplo':'on','publicado':'on','_save':'Guardar'}
        check('CSRF exigido',c.post(path,fields).status_code==403)
        fields['csrfmiddlewaretoken']=c.cookies['csrftoken'].value
        stream=BytesIO();Image.new('RGB',(40,40),(21,30,44)).save(stream,format='PNG')
        fields['foto']=SimpleUploadedFile('prueba.png',stream.getvalue(),content_type='image/png')
        check('edición y foto guardadas',c.post(path,fields).status_code==302)
        p.refresh_from_db()
        check('publicación guardada',p.publicado)
        check('bytes en Storage correctos',p.foto.open().read()==stream.getvalue())
        old=p.foto.name
        fields['foto']=SimpleUploadedFile('corrupta.png',b'not-an-image',content_type='image/png')
        check('imagen corrupta rechazada',c.post(path,fields).status_code==200)
        p.refresh_from_db();check('foto anterior conservada',p.foto.name==old)
        del fields['foto'];del fields['publicado']
        check('ocultación guardada',c.post(path,fields).status_code==302)
        p.refresh_from_db();check('producto queda oculto',not p.publicado)
        check('ejemplo excluido del inicio',p.nombre.encode() not in c.get('/inicio/').content)
        c.logout();check('logout',c.get(path).status_code==302)
    output={'status':'passed','checks':checks,'environment':'Django Client nativo + PostgreSQL/Storage Supabase; no HTTP Workers remoto'}
    (ROOT/'.local/supabase-prueba/admin-result.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output))
except Exception as exc:
    print(json.dumps({'status':'failed','error_type':type(exc).__name__,'checks_completed':checks}))
    raise SystemExit(1)
