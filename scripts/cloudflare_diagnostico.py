#!/usr/bin/env python3
"""Registrar diagnóstico acotado de la prueba autorizada, sin headers ni secretos."""
import base64
import json
import os
from pathlib import Path
import subprocess
import threading
import time
import httpx

ROOT=Path(__file__).resolve().parent.parent
FOLDER=ROOT/'.local/cloudflare-prueba'
access=json.loads((FOLDER/'worker-secrets.json').read_text())
role=json.loads((ROOT/'.local/supabase-prueba/jyz_app.json').read_text())
hidden=list(access.values())+[role['password'],base64.b64encode(
    (access['JYZ_REVIEW_USER']+':'+access['JYZ_REVIEW_PASSWORD']).encode()).decode()]
def sanitize(text):
    for secret in hidden:
        text=text.replace(secret,'[oculto]')
    return text[:2500]
events=[]
process=subprocess.Popen([str(ROOT/'.local/worker-app/node_modules/.bin/wrangler'),
    'tail','jyz-prueba','--format','json'],env=dict(os.environ,WRANGLER_SEND_METRICS='false',
    CLOUDFLARE_ACCOUNT_ID='bdc73f4bbbc036a160e49f5f9cc86b62'),
    stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
def read():
    buffer=''
    for line in process.stdout:
        if not buffer and not line.lstrip().startswith('{'):
            continue
        buffer+=line
        try:
            record=json.loads(buffer)
        except json.JSONDecodeError:
            continue
        buffer=''
        events.append({'outcome':record.get('outcome'),'cpuTime':record.get('cpuTime'),
            'wallTime':record.get('wallTime'),
            'exceptions':[{'name':e.get('name'),'message':sanitize(str(e.get('message','')))}
                          for e in record.get('exceptions',[])],
            'logs':[{'level':e.get('level'),'message':sanitize(str(e.get('message','')))}
                    for e in record.get('logs',[])]})
thread=threading.Thread(target=read,daemon=True)
thread.start()
timer=threading.Timer(35,process.terminate)
timer.start()
responses=[]
try:
    time.sleep(3)
    with httpx.Client(auth=(access['JYZ_REVIEW_USER'],access['JYZ_REVIEW_PASSWORD']),timeout=25) as c:
        for path in ['/inicio/','/admin/login/']:
            r=c.get('https://jyz-prueba.giron605.workers.dev'+path)
            responses.append({'path':path,'status':r.status_code})
    time.sleep(2)
finally:
    process.terminate()
    process.wait(timeout=10)
    timer.cancel()
    thread.join(timeout=2)
output={'responses':responses,'events':events}
(FOLDER/'diagnostico.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
