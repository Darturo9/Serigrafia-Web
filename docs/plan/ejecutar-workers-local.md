# Ejecutar la prueba Workers local

Estado: prueba de runtime local ejecutada. Ver `evidencia-workers-local.md` y ADR 003. No configura ni despliega servicios externos.

## Preparación

La instalación aislada ya fue autorizada y realizada. Para reproducirla, desde la raíz del proyecto:

```sh
UV_PROJECT_ENVIRONMENT=/Users/danilo/Documents/Serigrafia-Web/.local/workers-venv uv sync --project workers --python 3.13
.venv/bin/python manage.py collectstatic --noinput
.local/workers-venv/bin/python scripts/worker_database.py
.venv/bin/python scripts/worker_local.py prepare
npm ci --prefix .local/worker-app --ignore-scripts --no-audit --no-fund
.venv/bin/python scripts/worker_local.py sync
.venv/bin/python scripts/worker_local.py dev
```

El staging copia código y plantillas actuales sin editar originales. `worker_database.py` prepara exclusivamente el esquema `jyz_worker_local` dentro del PostgreSQL Docker existente en 127.0.0.1:55439. Contiene migraciones y datos sintéticos independientes del catálogo original.

El wrapper `worker_local.py` solo admite prepare/sync/dev, fija conexión local e IP loopback y no admite deploy ni --remote. La conexión se pasa por variable de entorno, sin imprimir contraseña. Los secretos sintéticos de revisión local se guardan con permisos 0600 bajo `.local/`; no compartidos por chat ni incluidos en Git.

Abrir http://127.0.0.1:8787/ . La pantalla es un catálogo técnico, no el diseño comercial. El editor sintético sirve al ejercicio HTTP; no entregar su acceso como cuenta del negocio. Fotos de la prueba Workers están en memoria y no tienen persistencia garantizada tras reinicio. El panel original sigue en 127.0.0.1:8000 si ese servidor está iniciado.

## Verificar

En otra terminal:

```sh
.local/workers-venv/bin/python scripts/local.py runtime-test
.local/workers-venv/bin/python scripts/worker_smoke.py
.venv/bin/python scripts/migration_review.py
```

El primero ejecuta 21 pruebas nativas en una base de prueba PostgreSQL; el segundo 25 comprobaciones HTTP en el Worker real local, con editor/productos de ejemplo. No borrar el esquema o productos originales. La prueba deja sus productos sintéticos identificados en el esquema separado y escribe evidencia sin claves en `.local/worker-smoke-result.json`.

El último genera inventario de 19 migraciones de Django y SQL de catálogo para revisión en `ops/`; no aplica migraciones ni modifica una base remota. Los SQL con sufijo propuesto/revision no son scripts de aplicación automática.

Ctrl+C en la terminal del Worker detiene solo ese proceso. No borrar volúmenes, bases o fotos para cerrar la prueba.

## Paquete remoto preparado

- `ops/01-esquema-y-roles.propuesto.sql`: esquema jyz_prueba, propietario/migrador y rol de ejecución sin login inicial; requiere confirmar no exposición a Data API y activar login/secretos por un canal seguro posteriormente.
- `ops/migraciones-django.md`: grafo de las migraciones que deben ejecutarse con Django en un entorno autorizado externo al Worker.
- `ops/catalogo-0001.revision.sql`: SQL generado, informativo; el ciclo de migraciones se gestiona con migrate.
- `ops/storage-bucket.propuesto.json`: bucket privado jyz-prueba-fotos, máximo 5 MB y tres formatos permitidos. Crear mediante API/Dashboard, sin INSERT directo a tablas internas Storage.
- `workers/wrangler.remote.example.jsonc`: configuración incompleta a propósito, sin ID Hyperdrive, origen de prueba ni secretos. No desplegarla todavía.

Falta autorización específica de recursos y escrituras en Supabase, secreto de Storage y acceso seguro de migración/ejecución. Cloudflare, Hyperdrive y despliegues necesitan autorización propia. No ejecutar migraciones en peticiones o al arrancar el Worker. El alojamiento final y la recuperación de datos/fotos siguen pendientes.
