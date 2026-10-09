"""Verifica presentación/permisos por HTTPS; no modifica productos ni usuarios."""
from pathlib import Path
import json,re
import httpx
root=Path(__file__).resolve().parent.parent
out=root/'.local/railway-prueba'
v=json.loads((out/'runtime-secrets.json').read_text())
a=json.loads((root/'.local/supabase-prueba/editor.json').read_text())
checks={};origin=v['JYZ_REVIEW_ORIGIN']
assert origin=='https://jyz-web-production.up.railway.app'
with httpx.Client(base_url=origin,timeout=40,follow_redirects=False) as c:
    checks['salud']=c.get('/healthz/').status_code==200
    checks['revision_restringida']=c.get('/admin/').status_code==401
with httpx.Client(base_url=origin,auth=(v['JYZ_REVIEW_USER'],v['JYZ_REVIEW_PASSWORD']),timeout=40,follow_redirects=False,headers={'Referer':origin+'/admin/'}) as c:
    r=c.get('/admin/login/')
    checks['entrada_jyz']=r.status_code==200 and 'Panel JYZ' in r.text and 'Catálogo local' not in r.text
    css=re.search(r'href="([^"]*admin-jyz[^\"]*\.css)"',r.text).group(1)
    r=c.get(css)
    # collectstatic reescribe las fuentes a nombres con hash; validar contenido normalizado.
    normalized=re.sub(r'(fonts/[^"/]+)\.[a-f0-9]{12}(\.ttf)',r'\1\2',r.text)
    checks['css_vigente']=r.status_code==200 and normalized==(root/'catalogo/static/catalogo/admin-jyz.css').read_text()
    checks['fuente_local']=c.get('/static/catalogo/fonts/Barlow-Regular.ttf').status_code==200
    r=c.post('/admin/login/',data={**a,'csrfmiddlewaretoken':c.cookies.get('csrftoken'),'next':'/admin/'})
    checks['login']=r.status_code==302
    r=c.get('/admin/');checks['portada_jyz']=r.status_code==200 and 'Prendas con tu sello.' in r.text
    r=c.get('/admin/catalogo/producto/');checks['lista_y_estados']=r.status_code==200 and all(t in r.text for t in ['jyz-thumbnail','Publicado','Oculto','Contenido'])
    r=c.get('/admin/catalogo/producto/3/change/');checks['edicion_agrupada']=r.status_code==200 and all(t in r.text for t in ['Información del producto','Tallas y opciones','Fotografía','Publicación','jyz-photo-preview','WebP'])
    checks['usuarios_restringidos']=c.get('/admin/auth/user/').status_code==403
    r=c.post('/admin/logout/',data={'csrfmiddlewaretoken':c.cookies.get('csrftoken')});checks['logout']=r.status_code in (200,302)
assert all(checks.values()),checks
(out/'admin-jyz-http.json').write_text(json.dumps({'checks':checks,'products_modified':False,'scope':'HTTP protegido; revisión visual local separada'},indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False))
