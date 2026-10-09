"""Verifica galería y permisos por HTTPS sin cambiar fotos, textos, datos o usuarios."""
from io import BytesIO
from pathlib import Path
import html
import json
import re
import sys
import httpx
from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '.local/railway-prueba'
runtime = json.loads((OUT / 'runtime-secrets.json').read_text())
editor = json.loads((ROOT / '.local/supabase-prueba/editor.json').read_text())
origin = runtime['JYZ_REVIEW_ORIGIN']
assert origin == 'https://jyz-web-production.up.railway.app'
checks = {}

with httpx.Client(base_url=origin, timeout=40, follow_redirects=False) as client:
    for path, expected in [('/',200),('/inicio/',200),('/productos/4/',200),('/admin/login/',401),('/catalogo/',401),('/healthz/',200)]:
        response = client.get(path)
        checks[path] = response.status_code == expected
        if path == '/':
            inicio = response.text
    gallery = inicio.split('id="trabajos"',1)[-1].split('</section>',1)[0]
    sources = [html.unescape(src) for src in re.findall(r'<img[^>]+src="([^"]+)"', gallery)] if 'id="trabajos"' in inicio else []
    checks['tres_fotos'] = len(sources) == 3
    checks['sin_referencias'] = 'Pexels' not in gallery and 'Referencia de prueba' not in gallery
    for index, url in enumerate(sources):
        # No solicitar destinos ajenos ni imprimir URLs firmadas.
        trusted = url.startswith('https://kcahxuvfmrzxzlnpezyf.supabase.co/storage/v1/object/sign/jyz-prueba-fotos/')
        checks[f'foto_{index}_privada'] = trusted
        if not trusted:
            continue
        try:
            response = client.get(url)
            response.raise_for_status()
            with Image.open(BytesIO(response.content)) as image:
                valid = image.format == 'WEBP' and max(image.size) <= 1600
            checks[f'foto_{index}_webp'] = valid and len(response.content) <= 500 * 1024 and response.headers.get('content-type','').startswith('image/webp')
        except (httpx.HTTPError, UnidentifiedImageError, OSError):
            checks[f'foto_{index}_webp'] = False

with httpx.Client(base_url=origin, auth=(runtime['JYZ_REVIEW_USER'],runtime['JYZ_REVIEW_PASSWORD']),
                  timeout=40, follow_redirects=False, headers={'Referer':origin+'/admin/'}) as client:
    response = client.get('/admin/login/')
    response = client.post('/admin/login/', data={**editor,'csrfmiddlewaretoken':client.cookies.get('csrftoken'),'next':'/admin/'})
    checks['login_editor'] = response.status_code == 302
    response = client.get('/admin/')
    checks['galeria_en_panel'] = response.status_code == 200 and '/admin/catalogo/galeriaimagen/' in response.text
    response = client.get('/admin/catalogo/galeriaimagen/')
    checks['lista_editable'] = response.status_code == 200 and 'id_form-0-orden' in response.text and 'id_form-0-activo' in response.text
    ids = sorted(set(re.findall(r'/admin/catalogo/galeriaimagen/(\d+)/change/',response.text)))
    checks['tres_registros_en_admin'] = len(ids) == 3
    response = client.get('/admin/catalogo/galeriaimagen/add/')
    checks['formulario_nueva_foto'] = response.status_code == 200 and all(f'name="{name}"' in response.text for name in ['titulo','descripcion','foto','orden','activo']) and 'WebP' in response.text
    for pk in ids:
        response = client.get(f'/admin/catalogo/galeriaimagen/{pk}/change/')
        checks[f'editar_{pk}'] = response.status_code == 200 and 'jyz-photo-preview' in response.text
        checks[f'borrar_{pk}_rechazado'] = client.get(f'/admin/catalogo/galeriaimagen/{pk}/delete/').status_code == 403
    checks['usuarios_rechazados'] = client.get('/admin/auth/user/').status_code == 403
    checks['logout'] = client.post('/admin/logout/',data={'csrfmiddlewaretoken':client.cookies.get('csrftoken')}).status_code in (200,302)

result = {'checks':checks,'datos_modificados':False,'alcance':'Lectura HTTPS y sesión del editor; edición remota requiere verificación separada autorizada.'}
(OUT / 'galeria-admin-http.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
sys.exit(0 if all(checks.values()) else 1)
