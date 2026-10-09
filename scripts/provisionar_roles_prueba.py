"""Genera secretos locales aislados y verificadores SCRAM, sin mostrar contraseñas."""
from pathlib import Path
import base64,hashlib,hmac,json,os,secrets
ROOT=Path(__file__).resolve().parent.parent
folder=ROOT/'.local'/'supabase-prueba'
folder.mkdir(mode=0o700,exist_ok=True)
statements=[]
for role in ('jyz_migrator','jyz_app'):
    target=folder/(role+'.json')
    if target.exists():
        raise SystemExit('Ya existe material local de roles; no rotar ni sobrescribir automáticamente.')
    password=secrets.token_urlsafe(48)
    salt=secrets.token_bytes(16)
    salted=hashlib.pbkdf2_hmac('sha256',password.encode(),salt,4096)
    client=hmac.new(salted,b'Client Key','sha256').digest()
    stored=hashlib.sha256(client).digest()
    server=hmac.new(salted,b'Server Key','sha256').digest()
    b64=lambda v:base64.b64encode(v).decode()
    verifier=f'SCRAM-SHA-256$4096:{b64(salt)}${b64(stored)}:{b64(server)}'
    values={'host':'aws-1-us-west-2.pooler.supabase.com','port':5432,'database':'postgres',
            'user':role+'.kcahxuvfmrzxzlnpezyf','password':password,
            'schema':'jyz_prueba','project':'kcahxuvfmrzxzlnpezyf','secret_key':secrets.token_urlsafe(64)}
    fd=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'w') as stream:json.dump(values,stream)
    statements.append(f"ALTER ROLE {role} LOGIN PASSWORD '{verifier}';")
fd=os.open(folder/'roles-scram.sql',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
with os.fdopen(fd,'w') as stream:stream.write('BEGIN;\n'+'\n'.join(statements)+'\nCOMMIT;\n')
print('Material de conexión local creado con permisos 0600; contraseñas no mostradas.')
