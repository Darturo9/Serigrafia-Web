"""Ejercita HTTP Admin y fotos sinteticas en el proyecto Railway JYZ autorizado."""
from pathlib import Path
from io import BytesIO
import os,sys,json,re,hashlib,uuid
root=Path(__file__).resolve().parent.parent;sys.path.insert(0,str(root))
if '--write-synthetic' not in sys.argv: raise SystemExit('Requiere --write-synthetic y autorizacion de prueba remota.')
os.environ['DJANGO_SETTINGS_MODULE']='config.settings_supabase_test';os.environ['JYZ_REMOTE_ROLE']='jyz_app'
import django;django.setup()
import httpx
from PIL import Image
from catalogo.models import Producto
out=root/'.local/railway-prueba';v=json.loads((out/'runtime-secrets.json').read_text());editor=json.loads((root/'.local/supabase-prueba/editor.json').read_text())
checks=[];name='PRUEBA Railway - no comercial '+uuid.uuid4().hex[:8];product=None
fields={'nombre':name,'descripcion':'Producto sintetico, prueba Railway','categoria':'PRUEBA','tallas':'["M"]','texto_foto':'Foto sintetica para verificar almacenamiento','orden':'0','es_ejemplo':'on','publicado':'on','_save':'Guardar'}
def check(label,condition):
 if not condition:raise AssertionError(label)
 checks.append(label);print(label,flush=True)
def image(fmt):
 stream=BytesIO();Image.new('RGB',(16,16),(28,50,80)).save(stream,format=fmt);return stream.getvalue()
def foto_webp_valida(product):
 data=product.foto.open().read()
 with Image.open(BytesIO(data)) as saved:
  return saved.format=='WEBP' and saved.size==(16,16) and len(data)<=500*1024

with httpx.Client(base_url=v['JYZ_REVIEW_ORIGIN'],auth=(v['JYZ_REVIEW_USER'],v['JYZ_REVIEW_PASSWORD']),timeout=40,follow_redirects=False,headers={'Referer':v['JYZ_REVIEW_ORIGIN']+'/admin/'}) as c:
 def post(path,files=None,with_csrf=True):
  data=dict(fields)
  if with_csrf:data['csrfmiddlewaretoken']=c.cookies.get('csrftoken')
  return c.post(path,data=data,files=files)
 try:
  check('anonimo Django restringido',c.get('/admin/catalogo/producto/').status_code==302)
  login=c.get('/admin/login/');check('formulario login',login.status_code==200)
  r=c.post('/admin/login/',data={**editor,'csrfmiddlewaretoken':c.cookies.get('csrftoken'),'next':'/admin/'})
  check('login HTTP real',r.status_code==302)
  check('sesion segura','Secure' in r.headers.get('set-cookie','') and 'HttpOnly' in r.headers.get('set-cookie',''))
  check('editor sin acceso usuarios',c.get('/admin/auth/user/').status_code==403)
  path='/admin/catalogo/producto/add/';check('panel agregar',c.get(path).status_code==200)
  check('CSRF exigido',post(path,with_csrf=False).status_code==403)
  data=image('PNG');r=post(path,{'foto':('sintetica.png',data,'image/png')});check('crear por Admin HTTP',r.status_code==302)
  product=Producto.objects.get(nombre=name,es_ejemplo=True)
  check('foto PNG persistida',foto_webp_valida(product))
  check('ejemplo visible solo en catalogo tecnico',name in c.get('/').text and name not in c.get('/inicio/').text)
  path=f'/admin/catalogo/producto/{product.pk}/change/';check('panel editar',c.get(path).status_code==200)
  fields['descripcion']='Edicion sintetica verificada desde Railway'
  for fmt,suffix,mime in [('JPEG','jpg','image/jpeg'),('WEBP','webp','image/webp')]:
   data=image(fmt);check('guardar foto '+fmt,post(path,{'foto':('sintetica.'+suffix,data,mime)}).status_code==302)
   product.refresh_from_db();check('bytes persistidos '+fmt,foto_webp_valida(product))
  check('edicion ORM verificada',product.descripcion==fields['descripcion'])
  previous=product.foto.name;digest=hashlib.sha256(data).hexdigest()
  check('imagen corrupta rechazada',post(path,{'foto':('corrupta.png',b'broken','image/png')}).status_code==200)
  product.refresh_from_db();check('foto anterior conservada',product.foto.name==previous)
  check('sin permiso borrar producto',c.get(f'/admin/catalogo/producto/{product.pk}/delete/').status_code==403)
  del fields['publicado'];check('ocultar por Admin',post(path).status_code==302)
  product.refresh_from_db();check('oculto en datos y vistas',not product.publicado and name not in c.get('/').text and name not in c.get('/inicio/').text)
  token=c.cookies.get('csrftoken');r=c.post('/admin/logout/',data={'csrfmiddlewaretoken':token})
  check('logout',r.status_code in (200,302) and c.get(path).status_code==302)
  result={'status':'passed','environment':'HTTP HTTPS Railway + PostgreSQL/Storage Supabase','checks':checks,'product_id':product.pk,'product_name':name,'hidden':True,'example':True,'photo_name':previous,'photo_sha256':digest}
  (out/'admin-http.json').write_text(json.dumps(result,indent=2)+'\n')
 except Exception as exc:
  (out/'admin-http-failure.json').write_text(json.dumps({'error_type':type(exc).__name__,'checks':checks,'product_id':product.pk if product else None},indent=2)+'\n')
  print('Fallo:',type(exc).__name__)
  if product is not None:
   fields.pop('publicado',None);post(f'/admin/catalogo/producto/{product.pk}/change/')
  raise SystemExit(1)
