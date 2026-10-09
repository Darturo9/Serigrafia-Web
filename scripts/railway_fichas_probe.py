"""Comprobación HTTPS del paquete de fichas. No cambia catálogo ni usuarios."""
from pathlib import Path
import json,re,hashlib,html
import httpx
root=Path(__file__).resolve().parent.parent
out=root/'.local/railway-prueba'
v=json.loads((out/'runtime-secrets.json').read_text())
a=json.loads((root/'.local/supabase-prueba/editor.json').read_text())
before=json.loads((out/'fichas-antes.json').read_text())
origin=v['JYZ_REVIEW_ORIGIN'];assert origin=='https://jyz-web-production.up.railway.app'
checks={}
with httpx.Client(base_url=origin,timeout=40) as c:
 checks['revision_restringida']=c.get('/productos/3/').status_code==401
 checks['salud']=c.get('/healthz/').status_code==200
with httpx.Client(base_url=origin,auth=(v['JYZ_REVIEW_USER'],v['JYZ_REVIEW_PASSWORD']),timeout=40,follow_redirects=False,headers={'Referer':origin+'/admin/'}) as c:
 r=c.get('/inicio/')
 checks['catalogo_ficha']=r.status_code==200 and 'href="/productos/3/"' in r.text and 'Ver producto' in r.text
 r=c.get('/productos/3/')
 checks['ficha_ejemplo']=r.status_code==200 and 'no disponible para venta' in r.text and 'Quiero este producto' not in r.text and 'id="foto-principal"' in r.text
 checks['sin_selector_unica_foto']='class="miniaturas"' not in r.text
 checks['noindex']='noindex' in r.headers.get('x-robots-tag','')
 foto=html.unescape(re.search(r'id="foto-principal"[^>]*src="([^"]+)"',r.text).group(1))
 photo=httpx.get(foto,timeout=30);photo.raise_for_status()
 checks['foto_bytes_conservados']=hashlib.sha256(photo.content).hexdigest()==next(x['sha256'] for x in before if x['id']==3)
 for file in ('producto.css','producto.js'):
  asset=re.search(r'(?:href|src)="([^"]*'+file.replace('.',r'(?:\.[a-f0-9]{12})?\.')+r')"',r.text).group(1)
  response=c.get(asset)
  checks[file]=response.status_code==200 and response.content==(root/'catalogo/static/catalogo'/file).read_bytes()
 for item in before:
  if not item['publicado']:
   checks['oculto_'+str(item['id'])]=c.get('/productos/'+str(item['id'])+'/').status_code==404
 checks['inexistente_404']=c.get('/productos/999999/').status_code==404
 r=c.get('/admin/login/')
 checks['login']=c.post('/admin/login/',data={**a,'csrfmiddlewaretoken':c.cookies.get('csrftoken'),'next':'/admin/'}).status_code==302
 r=c.get('/admin/catalogo/producto/3/change/')
 checks['admin_inline']=r.status_code==200 and 'imagenes-TOTAL_FORMS' in r.text and 'name="portada"' in r.text
 checks['inline_sin_borrado']='name="imagenes-0-DELETE"' not in r.text
 checks['usuarios_restringidos']=c.get('/admin/auth/user/').status_code==403
 checks['logout']=c.post('/admin/logout/',data={'csrfmiddlewaretoken':c.cookies.get('csrftoken')}).status_code in (200,302)
(out/'fichas-http.json').write_text(json.dumps({'checks':checks,'productos_modificados':False},indent=2))
print(checks);assert all(checks.values())
