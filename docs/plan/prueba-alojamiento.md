# Plan de prueba de alojamiento

**Plan histórico Workers:** reemplazado para la próxima prueba por [prueba-railway.md](prueba-railway.md) y ADR 004, tras elección expresa del usuario el 8 de octubre. Se conservan resultados, recursos e historial; no continuar Workers automáticamente.

Fecha: 7 de octubre de 2026, Guatemala. Estado vigente al 8 de octubre: **P0–P2 completados localmente; P3–P4 verificados con Django nativo/Supabase; P5–P7 pendientes**. El planteamiento del 7 de octubre se conserva como historial. Continúa ADR 001; las configuraciones siguientes son propuestas, no decisiones definitivas ni autorización remota.

## Objetivo y punto de partida

Validar la aplicación existente: Django 5.2.18 con plantillas y Admin, PostgreSQL, sesiones y fotos. No reiniciar el proyecto ni construir la web comercial antes de comprobar alojamiento y datos. Ver [inspección MCP](inspeccion-supabase.md): acceso al proyecto correcto verificado, PostgreSQL 17.11, sin tablas de aplicación ni buckets.

La prueba local anterior usa Python 3.11.16, PostgreSQL 16.14 y fotos en disco; sus 10 pruebas y la confirmación humana del panel se conservan como evidencia local, no se convierten en evidencia remota.

## Viabilidad documental y diferencias del código actual

- Cloudflare documenta adaptadores WSGI/ASGI para Django. Se propone comenzar por WSGI, coherente con `config/wsgi.py`. [Django en Workers](https://developers.cloudflare.com/workers/languages/python/packages/django/).
- Hyperdrive documenta psycopg para Python Workers, fecha de compatibilidad mínima `2026-09-08` y precauciones de concurrencia de operaciones síncronas. Proponer `2026-10-07` y flag `python_workers`, sujetos a prueba del runtime y del ORM. [Python/Hyperdrive](https://developers.cloudflare.com/hyperdrive/examples/python-workers/).
- El empaquetado admite paquetes Python puros y ruedas compatibles con PyEmscripten/Pyodide; las ruedas nativas del Mac no prueban compatibilidad. Validar Django, psycopg/libpq, Pillow, formatos de imagen y hashing de contraseñas; no copiar `psycopg-binary` del entorno local como si fuera compatible. Fijar versiones y lock tras resolver el runtime. [Paquetes](https://developers.cloudflare.com/workers/languages/python/packages/).
- La guía para Supabase recomienda conexión directa de PostgreSQL como origen de Hyperdrive. Confirmar hostname, puerto, región, TLS y conectividad antes de crearlo. No copiar el ejemplo que concede el rol `postgres`: se propone un rol limitado. [Hyperdrive/Supabase](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/supabase/).
- La guía de desarrollo permite Worker local con conexión a PostgreSQL local; ese modo no prueba pooling ni caché de Hyperdrive. `--remote` ejecuta en Cloudflare y requiere autorización. [Desarrollo local](https://developers.cloudflare.com/hyperdrive/configuration/local-development/).

Código a adaptar posteriormente: separar settings locales y de prueba Workers; retirar creación de `.local` del arranque remoto; `DEBUG=False`, hosts/CSRF concretos, secreto obligatorio, cookies seguras y sesiones en PostgreSQL. Obtener conexión del binding por el mecanismo documentado del runtime, con `CONN_MAX_AGE=0`; resolver aislamiento entre peticiones, cierre de conexiones y transacciones del ORM. No sustituir Django ORM por consultas de un ejemplo de asyncpg.

`config/urls.py` sirve media mediante el helper de desarrollo. La prueba remota necesitará un backend Django Storage y assets estáticos del Admin generados con `collectstatic`, servidos como assets del Worker. Conservar `noindex`, añadir protección de acceso de la prueba y excluir cualquier acción WhatsApp provisional.

Se consultó el changelog de Supabase por HTTP y la nota de PostgreSQL 15.19/17.11. El modelo local no utiliza ltree, cifrado PGP, índices btree_gist ni operadores propios; no se propone reparación por esos cambios. No constituye auditoría de las extensiones internas. [Nota del proveedor](https://supabase.com/changelog/postgres-15-19-17-11-breaking-changes).

## Secuencia con puntos de control

| Paso | Trabajo | Evidencia requerida | Autorización |
|---|---|---|---|
| P0 | Lectura MCP del proyecto y documentación | URL coincidente e inventario | Completado dentro de autorización actual |
| P1 | Preparar adaptador/settings/manifest separados; obtener plan y SQL de migraciones sin ejecutar en remoto | Archivos revisables, lista de dependencias y cambios | Implementado localmente; ver ADR 003 |
| P2 | Ejecutar Worker local contra PostgreSQL Docker y almacenamiento local | Importación, plantillas, login/sesiones, ORM, transacción/rollback y validación JPEG/PNG/WebP | Instalación aislada autorizada; 25 checks HTTP y 21 pruebas nativas aprobadas |
| P3 | Preparar esquema/roles y aplicar migraciones Django en Supabase | Plan aprobado, tablas correctas y grants revisados | Autorización remota específica pendiente |
| P4 | Probar backend de fotos contra bucket privado de prueba desde entorno local | Carga, lectura, reemplazo, archivo inválido y fallo de Storage | Creación/configuración de bucket y escrituras pendientes de autorización |
| P5 | Crear Hyperdrive y Worker de prueba protegido, registrar secretos y desplegar | SELECT 1, ORM, sesiones, Admin/estáticos y fotos desde Worker | Recursos externos y despliegue de prueba pendientes de autorización |
| P6 | Pruebas funcionales, concurrencia y segundo despliegue | A02–A06; parte de A11/A13; IDs, claves de objetos y hash persistentes | Escrituras de prueba y segundo despliegue incluidos en autorización concreta futura |
| P7 | Registrar resultado y confirmar ADR 001 o proponer reemplazo | Resultado por criterio, límites y costos reales | No cambia proveedor sin decisión acordada |

P2 superó el filtro local; ver [evidencia](evidencia-workers-local.md) y [guía](ejecutar-workers-local.md). P3–P5 siguen pendientes de autorización remota. Las herramientas están instaladas en un entorno aislado. El SQL de roles/esquema, inventario de migraciones y bucket están preparados en `ops/`; no se ejecutaron en Supabase.

## Paquete remoto propuesto, pendiente de autorización

| Recurso | Cambio concreto propuesto | Límites |
|---|---|---|
| PostgreSQL, proyecto `kcahxuvfmrzxzlnpezyf` | Crear esquema `jyz_prueba`, rol migrador propietario y rol de ejecución limitado; fijar search_path y grants/default privileges | Confirmar esquema no expuesto a Data API; sin grants a anon/authenticated, sin modificar esquemas de Supabase |
| Migraciones Django | Ejecutar `migrate` desde entorno controlado externo al Worker, después de revisar `migrate --plan` y SQL | Solo esquema acordado; ninguna migración en peticiones o al arrancar Worker |
| Datos de prueba | Grupo Responsable de catálogo (ver/agregar/editar), administrador de prueba y producto sintético `es_ejemplo=True` | Credenciales por canal seguro; no copiar usuarios/productos locales ni materiales comerciales automáticamente |
| Storage | Crear bucket privado `jyz-prueba-fotos`, máximo 5 MB, MIME JPEG/PNG/WebP; conservar límite de 16 MP en Django | Sin acceso anónimo de escritura; fotos sintéticas, sin imágenes del PDF |
| Credencial Storage | Elegir y provisionar acceso de servidor compatible con backend probado | OAuth MCP no sustituye credenciales de ejecución; no generar ni extraer claves ahora |
| Hyperdrive | Crear configuración `jyz-prueba` con origen directo Supabase y rol limitado; binding `HYPERDRIVE` | TLS al origen y caché de consultas desactivada al principio para validar ocultación/sesiones sin lecturas atrasadas |
| Worker | Crear `jyz-prueba`, assets de Admin, secretos y protección de acceso antes de exponer prueba | Sin dominio comercial, DNS, compra ni publicación comercial; también el despliegue de prueba necesita autorización |

Tablas previstas por las apps actuales (confirmar en el plan de migraciones): `catalogo_producto`, `django_migrations`, `django_content_type`, `django_admin_log`, `django_session`, `auth_user`, `auth_group`, `auth_permission`, `auth_user_groups`, `auth_user_user_permissions`, `auth_group_permissions`. `auth_user` de Django es distinta de `auth.users` de Supabase; no se incorpora Supabase Auth.

El rol de ejecución requiere USAGE del esquema, operaciones de filas y secuencias utilizadas por Django; no CREATE de esquema/tabla, administración de roles ni privilegios del propietario. RLS de tablas propias se evaluará como defensa adicional; antes de aprobar SQL comprobar que el esquema no esté expuesto. No modificar permisos globales de tablas del proveedor.

## Fotos: ruta a validar antes de elegir backend

Propuesta inicial: backend Django Storage por HTTP de Supabase, probado en Workers, con claves de objetos UUID y URLs de lectura firmadas para el bucket privado. Conservar interfaz de `ImageField` y validar `save`, `open`, `exists`, `url` y lectura desde plantilla; no persistir URLs firmadas que caducan como valor de la foto.

Comparar esta ruta con S3/django-storages solo si la primera resulta incompatible. Los access keys S3 generados otorgan acceso amplio y omiten RLS; no asumir que son credenciales restringidas al bucket. La sesión del Admin de Django tampoco equivale a un JWT de Supabase. Elegir método de servidor, revisar su alcance y documentarlo antes de emitir secretos. [Autenticación S3](https://supabase.com/docs/guides/storage/s3/authentication).

La foto nueva debe cargarse antes de guardar su referencia. Si carga o guardado falla, conservar la anterior y registrar cualquier objeto huérfano. No borrar automáticamente archivos anteriores en esta prueba; documentar la limpieza y pedir autorización separada para eliminar recursos. Una transacción SQL no revierte una carga HTTP. El bucket privado evita exposición directa de fotos de productos ocultos; probar caducidad de URLs y asumir que una URL ya emitida puede seguir funcionando hasta caducar. [Buckets](https://supabase.com/docs/guides/storage/buckets/fundamentals).

## Comprobaciones y criterio de salida

- **A02 / R07:** anónimo bloqueado, sesión autorizada persistente, cierre de sesión, CSRF y rol sin borrar productos ni administrar usuarios. Probar usuarios concurrentes para detectar cruce de sesiones o conexiones.
- **A03–A04 / R02, R08:** alta, edición, ocultación y republicación visibles en siguiente petición, incluyendo peticiones concurrentes y otra sesión. Confirmar commit/rollback sin mezclar transacciones.
- **A05 / R08:** JPEG/PNG/WebP válidos, límite de 5 MB y 16 MP, archivo corrupto y reemplazo inválido conservan foto anterior. Fallo simulado de Storage no deja producto apuntando a archivo inexistente.
- **A06 / R02, R08:** registrar ID de producto, nombre de objeto y hash; desplegar de nuevo, iniciar nueva sesión y comprobar mismos datos y bytes. No basta recargar página.
- **A11 parcial:** catálogo vacío, ocultación y error de Storage. **A13 parcial:** secretos no presentes en HTML/JS/logs, esquema privado, permisos y protección de prueba; inventariar respaldo de base y archivos por separado.
- Registrar versiones reales de runtime/paquetes, fecha de compatibilidad, entorno, pasos y resultado de cada comprobación. Registrar latencia, errores, consumo/límites y plan de cuentas antes de comprometer costos.

**A07 es WhatsApp**, fuera de esta prueba: +502 confirmado, recorrido aún sin implementar/verificar. A01, A07–A10, A12 y A13 completo siguen pendientes; esta prueba no autoriza el lanzamiento ni aprueba diseño. Si falla ORM, sesiones, Pillow o Storage, detener esa etapa, conservar evidencia y presentar alternativas sin cambiar silenciosamente el proveedor.

Antes de P3: entregar SQL/plan exacto, configuración sin secretos, backend elegido, recursos, presupuesto y pruebas. Antes de P5: aprobar explícitamente el entorno y su protección. Recuperación propuesta: volver a versión anterior del Worker y preservar esquema/bucket; cualquier eliminación posterior requiere autorización. No garantizar costo cero ni fecha mientras falten estas verificaciones.

## Resultado de P1–P2

La adaptación descrita como propuesta se implementó localmente con ADR 003. Ruedas y versiones fijadas en workers/; configuración compartida/local/Workers separada; backend privado REST preparado y probado con simulaciones. Las fotos del Worker local utilizan memoria. Ninguna afirmación de este plan convierte esa prueba en persistencia de Supabase ni valida costos o límites remotos.

## Paquete Cloudflare preparado — 8 de octubre

P3 y P4 autorizados y ejecutados: ver evidencia-supabase-prueba.md. P5 tiene ahora paquete revisable y dry-run local aprobado: 43,34 MiB, 134 assets, sin secretos copiados ni recursos externos. Ver [paquete para autorización](paquete-cloudflare-prueba.md). P6/P7 continúan pendientes; no confirma ADR 001 ni permite despliegue por sí solo.
