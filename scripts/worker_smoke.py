#!/usr/bin/env python3
"""Ejercicio HTTP real contra Worker LOOPBACK y esquema de prueba separado."""
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import json
from pathlib import Path
import re
from uuid import uuid4

import httpx
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "http://127.0.0.1:8787"
credential = json.loads((ROOT / ".local" / "worker-smoke-access.json").read_text())
results = []

def check(condition, label):
    if not condition:
        raise AssertionError(label)
    results.append(label)


def csrf(response):
    return re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)[1]


def image(fmt):
    stream = BytesIO()
    Image.new("RGB", (16, 16), "orange").save(stream, format=fmt)
    return stream.getvalue()

with httpx.Client(base_url=ORIGIN, timeout=30, follow_redirects=False) as client:
    response = client.get("/catalogo/")
    check(response.status_code == 200, "catálogo HTTP 200 desde Workers")
    check(response.headers["X-Robots-Tag"] == "noindex, nofollow", "revisión sin indexación")
    check(client.get("/admin/catalogo/producto/add/").status_code == 302, "panel anónimo restringido")
    response = client.get("/admin/login/")
    check(response.status_code == 200, "plantilla de login disponible")
    response = client.post("/admin/login/", data={**credential, "csrfmiddlewaretoken": csrf(response), "next": "/admin/"},
                           headers={"Referer": ORIGIN + "/admin/login/"})
    check(response.status_code == 302, "login Django y sesión guardada")
    check(client.get("/admin/").status_code == 200, "sesión válida en otra petición")
    check(client.get("/static/admin/css/base.css").status_code == 200, "assets CSS del Admin")
    check(client.get("/admin/auth/user/").status_code == 403, "editor sin acceso a usuarios")
    check(client.post("/admin/catalogo/producto/add/", data={"nombre":"rechazar"}).status_code == 403,
          "POST sin CSRF rechazado")
    unique = "Prenda sintética Workers " + uuid4().hex[:8]
    data = {"nombre": unique, "descripcion": "Solo prueba local; no producto comercial", "tallas": '["S", "M"]',
            "orden": "0", "publicado": "on", "es_ejemplo": "on", "texto_foto": "Imagen sintética"}
    add = client.get("/admin/catalogo/producto/add/")
    response = client.post("/admin/catalogo/producto/add/", data={**data,"csrfmiddlewaretoken":csrf(add)},
                           files={"foto":("prueba.png",image("PNG"),"image/png")})
    check(response.status_code == 302, "producto y PNG creados por el Admin Workers")
    catalog = client.get("/catalogo/")
    check(unique in catalog.text, "producto persistente visible en petición posterior")
    card = next(card for card in re.findall(r"<article>(.*?)</article>", catalog.text, re.S) if unique in card)
    photo_url = re.search(r'<img src="([^"]+)"', card)[1]
    check(client.get(photo_url).status_code == 200, "foto en memoria servida por Worker local")
    listing = client.get("/admin/catalogo/producto/", params={"q":unique})
    change_path = re.search(r'href="(/admin/catalogo/producto/[0-9]+/change/)"', listing.text)[1]
    for fmt, filename, mime in [("JPEG", "segunda.jpg", "image/jpeg"), ("WEBP", "tercera.webp", "image/webp")]:
        page = client.get(change_path)
        response = client.post(change_path, data={**data,"csrfmiddlewaretoken":csrf(page)},
                               files={"foto":(filename,image(fmt),mime)})
        check(response.status_code == 302, "reemplazo " + fmt + " desde Workers")
    page = client.get(change_path)
    response = client.post(change_path, data={**data,"csrfmiddlewaretoken":csrf(page)},
                           files={"foto":("rota.png",b"invalid","image/png")})
    check(response.status_code == 200 and "errorlist" in response.text, "imagen corrupta rechazada por Workers")
    page = client.get(change_path)
    hidden = {**data,"csrfmiddlewaretoken":csrf(page)}
    hidden.pop("publicado")
    check(client.post(change_path,data=hidden).status_code == 302, "ocultación guardada")
    check(unique not in client.get("/catalogo/").text, "producto oculto no aparece en catálogo")
    page = client.get(change_path)
    check(client.post(change_path, data={**data,"csrfmiddlewaretoken":csrf(page)}).status_code == 302, "republicación guardada")
    check(unique in client.get("/catalogo/").text, "producto republicado visible")
    runtime = client.get("/__prueba__/runtime/").json()
    check(runtime["rollback"] and runtime["formats"]==["JPEG","PNG","WEBP"], "rollback ORM y codecs verificados en WebAssembly")
    with ThreadPoolExecutor(max_workers=4) as pool:
        responses = list(pool.map(lambda _: httpx.get(ORIGIN+"/__prueba__/runtime/", timeout=30).json(), range(8)))
    check(all(r["rollback"] for r in responses), "8 peticiones concurrentes sin mezclar transacciones")
    session_cookies = dict(client.cookies)
    def session_probe(index):
        response = httpx.get(ORIGIN + "/admin/catalogo/producto/add/", timeout=30,
                             cookies=session_cookies if index % 2 == 0 else {})
        return response.status_code == (200 if index % 2 == 0 else 302)
    with ThreadPoolExecutor(max_workers=4) as pool:
        isolated = list(pool.map(session_probe, range(8)))
    check(all(isolated), "sesiones autenticadas y anónimas aisladas en 8 peticiones concurrentes")
    check(client.get(change_path.replace("/change/", "/delete/")).status_code == 403, "editor sin permiso de borrado")
    page = client.get("/admin/")
    check(client.post("/admin/logout/", data={"csrfmiddlewaretoken":csrf(page)}).status_code in (200,302), "logout completado")
    check(client.get("/admin/catalogo/producto/add/").status_code == 302, "sesión cerrada no permite editar")
evidence = {"environment":"Worker local workerd/WebAssembly, PostgreSQL Docker jyz_worker_local",
            "results": results, "runtime":runtime, "limits":["Storage remoto no probado", "fotos en memoria no persistentes tras reinicio", "no despliegue remoto"],
            "synthetic_product":unique}
(ROOT / ".local" / "worker-smoke-result.json").write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"checks":len(results),"runtime":runtime,"status":"passed"},ensure_ascii=False))
