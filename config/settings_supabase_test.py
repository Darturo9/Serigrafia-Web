"""Perfil limitado al Supabase y esquema de prueba autorizados."""
import json,os
from django.core.exceptions import ImproperlyConfigured
from .settings_base import *
role=os.environ.get('JYZ_REMOTE_ROLE','jyz_migrator')
if role not in {'jyz_migrator','jyz_app'}: raise ImproperlyConfigured('Rol de prueba inválido.')
access=json.loads((BASE_DIR/'.local'/'supabase-prueba'/(role+'.json')).read_text())
if access['project']!='kcahxuvfmrzxzlnpezyf' or access['schema']!='jyz_prueba' or access['user']!=role+'.kcahxuvfmrzxzlnpezyf' or access['host']!='aws-1-us-west-2.pooler.supabase.com':
    raise ImproperlyConfigured('Destino fuera de la prueba autorizada.')
SECRET_KEY=access['secret_key']
DEBUG=False
ALLOWED_HOSTS=['127.0.0.1','localhost']
DATABASES={'default':{'ENGINE':'django.db.backends.postgresql','NAME':access['database'],
    'USER':access['user'],'PASSWORD':access['password'],'HOST':access['host'],'PORT':access['port'],
    'CONN_MAX_AGE':0,'DISABLE_SERVER_SIDE_CURSORS':True,
    'OPTIONS':{'sslmode':'verify-full','sslrootcert':str(BASE_DIR/'.local'/'supabase-prueba'/'prod-ca-2021.crt'),'connect_timeout':10,
               'options':'-c search_path=jyz_prueba','prepare_threshold':None}}}
MEDIA_ROOT=BASE_DIR/'.local'/'supabase-prueba'/'media'
MEDIA_URL='/media/'
storage_key_path=BASE_DIR/'.local'/'supabase-prueba'/'storage-key'
if storage_key_path.exists() and storage_key_path.read_text().strip():
    STORAGES={'default':{'BACKEND':'config.storage.supabase.SupabasePrivateStorage',
        'OPTIONS':{'base_url':'https://kcahxuvfmrzxzlnpezyf.supabase.co','bucket':'jyz-prueba-fotos',
                   'key':storage_key_path.read_text().strip()}},
        'staticfiles':{'BACKEND':'django.contrib.staticfiles.storage.StaticFilesStorage'}}
