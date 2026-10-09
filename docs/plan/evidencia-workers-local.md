# Evidencia de Workers local

Fecha: 7 de octubre de 2026, Guatemala. No hay despliegue remoto.

La autorización inicial de preparación se amplió con «avanza con la implementación» y con autorización explícita para instalación local aislada. El entorno Django original se conserva.

## Entornos

- Django original: Python 3.11.16, Django 5.2.18, Pillow 12.3.0, psycopg 3.3.6.
- Herramientas aisladas: Python 3.13.12, workers-py 1.17.7, SDK 1.9.3, uv 0.12.23 y Wrangler 4.148.0. La copia de uv es local; no se actualizó la global.
- Worker ejecutado por workerd: Python **3.14.2 en WebAssembly**, fecha de compatibilidad 2026-10-07. Django 5.2.18, Pillow 12.2.0, psycopg/psycopg-binary 3.3.5, httpx 0.28.1 y tzdata 2026.5. `workers/pylock.toml` conserva el lock de ruedas PyEmscripten; `workers/uv.lock` corresponde al entorno nativo.
- PostgreSQL Docker existente, esquema separado `jyz_worker_local`, editor y productos sintéticos. No se trasladaron ni alteraron productos de la prueba original en public.
- Fotos del Worker local: InMemoryStorage. Pueden desaparecer al reiniciar el runtime. Esto NO cumple A06 para fotos ni demuestra Supabase Storage.

## Resultados

21 pruebas automatizadas pasaron en el entorno nativo aislado contra PostgreSQL local: las 10 existentes y 11 nuevas de configuración, API Storage simulada, errores, permisos y conservación de la foto anterior. No son consultas a Supabase.

25 comprobaciones HTTP pasaron contra `http://127.0.0.1:8787/`, sin usar el cliente de pruebas de Django:

- catálogo HTTP 200 desde Workers.
- revisión sin indexación.
- panel anónimo restringido.
- plantilla de login disponible.
- login Django y sesión guardada.
- sesión válida en otra petición.
- assets CSS del Admin.
- editor sin acceso a usuarios.
- POST sin CSRF rechazado.
- producto y PNG creados por el Admin Workers.
- producto persistente visible en petición posterior.
- foto en memoria servida por Worker local.
- reemplazo JPEG desde Workers.
- reemplazo WEBP desde Workers.
- imagen corrupta rechazada por Workers.
- ocultación guardada.
- producto oculto no aparece en catálogo.
- republicación guardada.
- producto republicado visible.
- rollback ORM y codecs verificados en WebAssembly.
- 8 peticiones concurrentes sin mezclar transacciones.
- sesiones autenticadas y anónimas aisladas en 8 peticiones concurrentes.
- editor sin permiso de borrado.
- logout completado.
- sesión cerrada no permite editar.

La prueba concurrente incluye 8 transacciones con rollback y 8 peticiones alternando sesión administrativa y acceso anónimo. Es un ejercicio pequeño de concurrencia, no una prueba de capacidad bajo carga ni de comportamiento entre regiones.

## Fallos detectados y correcciones

- Pillow 12.3.0 sin rueda usable para ese runtime: perfil Workers usa rueda 12.2.0. psycopg requiere la rueda psycopg-binary 3.3.5 de WebAssembly, no el binario del Mac.
- El empaquetado inicial incluyó entornos de herramientas y agotó observadores. El staging separa `src/` del entorno y de node_modules. Plantillas .html se declaran como módulos de texto.
- Login sin datos de zona horaria: dependencia tzdata explícita.
- ORM síncrono rechazado dentro del event loop: ejecución WSGI serializada y habilitación del modo síncrono solo en esa entrada; ADR 003 explica la condición.
- Login sin hashlib.pbkdf2_hmac: adaptador PBKDF2-SHA256 mediante Web Crypto, mismo formato y coste de Django. El login con contraseña creada por Django nativo pasó.
- asyncio.Lock compartido cancelaba peticiones como hung: exclusión mediante bandera y espera `scheduler.wait` perteneciente a cada petición, con límite de 5 segundos y respuesta 503 si se satura. La concurrencia se volvió a probar y pasó.

## Límites pendientes

Sin migración, bucket, upload ni escritura remotos; sin Hyperdrive remoto, prueba protegida en Cloudflare o nuevo despliegue. La aceptación A02–A06 en alojamiento final permanece pendiente. A11 y A13 tampoco quedan completos. La prueba HTTP no es una revisión visual en navegador ni una comprobación móvil.

El bundle local informó aproximadamente 44 MiB de módulos sin comprimir. Falta medir el tamaño que cuenta para límites del despliegue, arranque, memoria y CPU en la cuenta real; no garantizar plan gratuito.

Archivos de evidencia local: `.local/worker-smoke-result.json` y `.local/worker-dev.log` (sin contraseñas en resultados). Credenciales locales sintéticas en archivos con permisos restringidos, excluidos de versiones. No reproducirlas en documentos o capturas.
