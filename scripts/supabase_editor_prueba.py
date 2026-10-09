"""Crea solo un editor sintético en el esquema/proyecto autorizados."""
import json,os,secrets,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
os.environ['DJANGO_SETTINGS_MODULE']='config.settings_supabase_test'
os.environ['JYZ_REMOTE_ROLE']='jyz_app'
import django
django.setup()
from django.contrib.auth.models import User,Group,Permission
from django.test import Client,override_settings
from django.db import transaction
folder=ROOT/'.local'/'supabase-prueba'
target=folder/'editor.json'
if target.exists():
    access=json.loads(target.read_text())
else:
    access={'username':'jyz-editor-prueba','password':secrets.token_urlsafe(40)}
    fd=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'w') as stream:json.dump(access,stream)
with transaction.atomic():
    group,_=Group.objects.get_or_create(name='Responsable de catálogo')
    group.permissions.set(Permission.objects.filter(content_type__app_label='catalogo',content_type__model='producto',codename__in=['view_producto','add_producto','change_producto']))
    user,created=User.objects.get_or_create(username=access['username'],defaults={'is_staff':True,'is_superuser':False})
    if created:
        user.set_password(access['password']);user.save()
        user.groups.add(group)
    elif not user.check_password(access['password']):
        raise SystemExit('No reemplazar una credencial existente; revisar estado.')
with override_settings(ALLOWED_HOSTS=['testserver']):
    c=Client()
    assert c.login(**access)
    assert c.get('/admin/catalogo/producto/').status_code==200
    assert c.get('/admin/auth/user/').status_code==403
    assert not user.has_perm('catalogo.delete_producto')
    c.logout()
print(json.dumps({'editor_sintetico':True,'admin_catalogo':200,'usuarios':403,'borrar_producto':False,'entorno':'Django nativo con PostgreSQL Supabase; no Workers remoto'}))
