# ADR 003. Adaptación local a Python Workers

Estado: implementado y probado localmente, sujeto a validación remota. No confirma ADR 001 ni cambia proveedor. No reemplaza el historial del ADR 002.

## Contexto y autorización

El usuario autorizó avanzar con la implementación e instalar herramientas localmente en un entorno aislado. Se conserva el Django Admin, las plantillas, el catálogo y la prueba original. No se autorizaron cambios remotos ni publicación. El usuario confirmó +502 para el WhatsApp recibido.

## Decisión de esta etapa

Separar settings compartidos, locales y Workers, con validación obligatoria de bindings/secretos. Usar WSGI y psycopg a través del binding Hyperdrive. Separar herramientas y paquetes del runtime mediante staging reproducible en `.local/worker-app/src/` y versiones fijadas en `workers/`.

Para la fecha de compatibilidad requerida el runtime utiliza Python 3.14.2. Se probaron Django 5.2.18, Pillow 12.2.0, psycopg/psycopg-binary 3.3.5 en ruedas de WebAssembly, httpx 0.28.1 y tzdata 2026.5. El entorno original no se actualiza a estas versiones.

El ORM síncrono necesita desactivar su rechazo de contexto async en esta entrada. La condición es que todas las operaciones Django se ejecuten una por vez dentro de cada isolate, con cierre de conexiones y sin generadores de respuesta que consulten el ORM fuera de esa sección. La bandera de exclusión usa timers de la propia petición; asyncio.Lock compartido falló en el ejercicio real. Se devuelve 503 tras 5 segundos de espera si hay saturación. Esta limitación exige probar capacidad y comportamiento remoto antes de confirmar viabilidad.

El hasher Workers implementa PBKDF2-SHA256 de Django usando Web Crypto donde falta OpenSSL en CPython/WASM. Conserva algoritmo, formato, sal e iteraciones. Se verificó el login con una contraseña generada por Django nativo. No usar un algoritmo más débil para resolver compatibilidad.

El backend remoto preparado usa la API HTTP de Supabase Storage y bucket privado, con nombres UUID, validación de imágenes, sin sobrescritura ni borrado automático y URLs firmadas. La escritura se hace solo desde Django. El acceso exacto de servidor y sus privilegios requieren revisión y provisión segura antes de prueba remota; no asumir que una clave del proyecto tiene permisos limitados al bucket. OAuth MCP no sustituye ese secreto.

La prueba local de Worker utiliza un esquema separado y fotos en memoria. No convertir ese backend temporal en el almacenamiento definitivo. La aplicación devuelve un error comprensible si falla Storage; una carga nueva fallida conserva la referencia anterior. Una transacción SQL no puede revertir la carga HTTP: falta política de objetos huérfanos.

## Evidencia y límites

Ver [evidencia](../plan/evidencia-workers-local.md): 21 pruebas nativas y 25 comprobaciones HTTP del runtime real local. No hay prueba contra Supabase/Hyperdrive remoto, aceptación de fotos persistentes, revisión visual de marca ni publicación. El bundle y el coste en cuenta real siguen por verificar. Si la prueba remota falla, registrar la evidencia y consultar antes de cambiar stack.

Fuentes: [Django en Workers](https://developers.cloudflare.com/workers/languages/python/packages/django/), [Hyperdrive/Python](https://developers.cloudflare.com/hyperdrive/examples/python-workers/), [Web Crypto](https://developers.cloudflare.com/workers/runtime-apis/web-crypto/), [API Python de Storage](https://github.com/supabase/supabase-py/blob/main/src/storage/src/storage3/_sync/file_api.py), [metadatos de objetos](https://github.com/supabase/storage/blob/master/src/storage/renderer/info.ts).

## Evidencia adicional del 8 de octubre

Lectura HTTP de Storage real probada en workerd local, con URL firmada y verificación de bytes/hash. HEAD falló en jsfetch por body nulo; exists usa metadatos GET. 31 pruebas nativas con regresión aprobadas. No confirma upload WASM, Hyperdrive ni alojamiento remoto; ver ../plan/evidencia-supabase-prueba.md.
