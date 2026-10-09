# Paquete Cloudflare para autorización

Fecha: 8 de octubre de 2026. Estado: preparado y empaquetado localmente; autorizado expresamente por el usuario («Si autorizo») el 8 de octubre, ejecución remota en curso de preparación. Aún sin recursos ni despliegues remotos. P3–P4 Supabase completados desde Django nativo; P5–P7 pendientes. ADR 001 no confirmado.

## Resultado local

`scripts/worker_remote_prepare.py` prepara una carpeta nueva en `.local/worker-remote-review/`, reutiliza las ruedas WebAssembly instaladas y ejecuta Wrangler **solo con --dry-run**. No instala, autentica, configura recursos ni publica. Se excluyen tests, perfiles exclusivos del Mac, cachés y archivos de credenciales. La carpeta original del Worker local no se reemplaza.

Resultado: exit 0, Total Upload 44377.92 KiB (43,34 MiB), gzip de referencia 9872.97 KiB. Assets: 134 archivos, máximo 325171 bytes. Configuración de empaquetado con ID Hyperdrive ficticio y origen revision.invalid: no utilizar para publicar. Evidencia: `.local/worker-remote-review/result.json`, `dry-run.log` y `bundled/`.

El primer intento con pywrangler volvió a resolver dependencias y falló al seleccionar ruedas de Pillow. No se actualizaron versiones: Wrangler instalado realizó el empaquetado directamente con python_modules previamente preparados. No ejecutar pywrangler deploy sin resolver/revisar esa regeneración. El empaquetado exitoso no demuestra arranque remoto, CPU, memoria ni conectividad.

## Cambios remotos concretos solicitados

| Recurso | Acción y alcance |
|---|---|
| Cuenta Cloudflare del usuario | Inspeccionar plan, permisos, ID de cuenta y subdominio workers.dev. Sin aceptar planes de pago ni compras. Si requiere un nuevo token, el usuario lo provisiona por canal seguro con permisos acotados. |
| CA de PostgreSQL | Subir el certificado público recibido desde el dashboard Supabase como `jyz-supabase-prueba-ca` para validar TLS. No es la clave privada del servidor. |
| Hyperdrive `jyz-prueba` | Origen directo `db.kcahxuvfmrzxzlnpezyf.supabase.co:5432`, base postgres, usuario directo `jyz_app`, contraseña ya provisionada para ese rol, máximo inicial de 5 conexiones, cache desactivada y sslmode verify-full con CA. Propuesta revisable en ../../ops/hyperdrive-prueba.propuesto.json. |
| Worker `jyz-prueba` | Desplegar código actual, ruedas fijadas y assets; habilitar únicamente su URL workers.dev de revisión, previews desactivadas. Fecha 2026-10-07 y flag python_workers. Sin dominio comercial ni cambios DNS. |
| Secretos del Worker | Proveer DJANGO_SECRET_KEY nuevo, JYZ_REVIEW_USER, JYZ_REVIEW_PASSWORD aleatoria de al menos 24 caracteres y SUPABASE_STORAGE_KEY actual como secretos de servidor. No copiar credenciales Django/Storage a vars, GitHub, HTML o logs. |
| Prueba y segundo despliegue | Cargar/editar/ocultar productos y fotos sintéticos en el esquema/bucket de prueba autorizados; verificar panel, sesiones, CSRF, permisos, concurrencia, transporte Storage, hash de foto y persistencia tras redespliegue. Sin borrar datos ni recursos. |

Esto comparte con Cloudflare la contraseña del rol limitado PostgreSQL y la clave secreta de Storage para ejecutar la aplicación. La clave Storage es privilegiada a nivel de proyecto; no afirmar que está restringida al bucket. El backend limita sus operaciones al bucket de prueba, pero esa restricción de código no reduce los privilegios de la clave.

La protección Basic del Worker se evalúa antes de Django y assets. Falta de secretos devuelve 503; falta de credencial de revisión devuelve 401. Django Admin conserva su login independiente. Proveer los cuatro secretos en la misma primera versión antes de habilitar la URL de revisión; no desplegar primero una versión abierta. Fijar JYZ_REVIEW_ORIGIN al origen HTTPS real y habilitar workers_dev solo en la configuración final autorizada. El ejemplo actual mantiene workers_dev=false como cierre previo.

Hyperdrive usa conexión directa, distinta del pooler de sesión empleado desde el Mac. Allí el usuario es jyz_app, sin sufijo del proyecto. La resolución IPv6 directa falló desde el Mac; la conexión desde Cloudflare aún no fue probada. Si falla, registrar y detener esa etapa: no cambiar silenciosamente a Supavisor, comprar IPv4 o debilitar TLS.

## Límites y costos consultados

Documentación oficial consultada el 8 de octubre; cuenta Cloudflare del usuario todavía sin inspeccionar. No garantizar costo cero ni aprobar cambios de plan.

- Workers: 64 MiB sin comprimir en Free/Paid, sin límite de tamaño comprimido; nuestro paquete queda por debajo. Memoria 128 MB e inicio 1 segundo: pendientes de medir en despliegue. [Límites](https://developers.cloudflare.com/workers/platform/limits/).
- Free: 100000 peticiones/día y 10 ms CPU por petición. Django, PBKDF2 y Pillow requieren comprobar CPU real; no se reducirá seguridad del login para ajustarse al plan. [Precio Workers](https://developers.cloudflare.com/workers/platform/pricing/).
- Hyperdrive incluido en Free con 100000 consultas/día; transacciones y escrituras también consumen consultas. Paid sin esa cuota diaria. [Precio Hyperdrive](https://developers.cloudflare.com/hyperdrive/platform/pricing/).
- Workers Paid tiene mínimo de USD 5/mes por cuenta y cargos por exceso. No se contratará; si Free falla y hace falta pagar, presentar resultados y presupuesto para autorización separada. Sin compra de dominio, IPv4 u otros servicios.
- Todos los assets de esta prueba pasan por el Worker para aplicar protección; no asumir que disfrutan la exención de peticiones de assets servidos directamente.

## Evidencia y recuperación necesarias

Antes del primer despliegue: comprobar cuenta, plan actual, revocación de clave anterior según confirmación del usuario, CA y origen Hyperdrive real, secrets presentes y ausencia de datos comerciales ficticios. No ejecutar migraciones en Worker ni repetir las 19 ya aplicadas.

Registrar por A02–A06/A11/A13 parcial: entorno, versión desplegada, respuesta sin autorización, login/logout, permisos negativos, edición/ocultación, validación de formatos, fallo de Storage conservando referencia, sesiones concurrentes, consumo/errores y segunda versión con mismos ID/nombre de foto/bytes. Comparar hashes sin guardar URLs firmadas o valores secretos en evidencia.

Si falla una versión, conservar evidencia y recursos de prueba; usar rollback a una versión válida si existe. No borrar esquema/bucket ni inventar recuperación probada. Respaldo de base y copia de fotos, capacitación y aceptación comercial siguen pendientes antes de publicación.

Fuentes adicionales: [Hyperdrive y Supabase](https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/supabase/), [TLS Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/).

## Puerta de autorización

AGENTS.md exige: «Compras, publicación y modificaciones de servicios externos necesitan autorización explícita aplicable a la acción concreta». La autorización de Supabase y la URL GitHub no cubren crear Hyperdrive, transferir secretos a Cloudflare o desplegar. Solicitar aprobación del paquete anterior, sin compras, cambios de plan, dominio/DNS, commit/push ni lanzamiento comercial.

## Corrección posterior del transporte Storage

Lectura Storage comprobada desde workerd local: GET de metadatos, bytes privados, URL firmada y rechazo público, con hash idéntico al nativo. exists dejó de utilizar HEAD por un error getReader del transporte jsfetch ante cuerpo nulo. El paquete incorpora la corrección y supera un nuevo dry-run, registro dry-run-storage-fix.log. No cambia el alcance de autorización: upload sintético desde WASM local se comprobó posteriormente; Hyperdrive/despliegues continúan pendientes.

Carga posterior desde WASM local aprobada para PNG/JPEG/WebP, imagen corrupta rechazada y lectura de hashes desde otro proceso tras terminar workerd. Ver evidencia-supabase-prueba.md. No cambia la puerta de autorización Cloudflare ni sustituye P5/P6.

## Autorización recibida

El usuario respondió «Si autorizo» a la solicitud de este paquete. Se puede proceder con inspección de cuenta/plan, CA, Hyperdrive, secretos y dos despliegues de prueba protegidos dentro del plan gratuito. No cubre compras, cambio de plan, dominio/DNS, lanzamiento comercial, eliminaciones ni commit/push. La puerta pendiente anterior se conserva como historial; ya no pedir de nuevo esta aprobación.

## Resultado de ejecución autorizada

CA, Hyperdrive y primera versión del Worker aplicados. Cuenta Free verificada, acceso anónimo 401. Django falla por CpuLimitExceeded/exceededCpu en peticiones autorizadas; segundo despliegue y aceptación suspendidos. No se contrató ni cambió plan. Ver [evidencia Cloudflare](evidencia-cloudflare-prueba.md). Se requiere nueva decisión de presupuesto/alojamiento; la autorización previa no cubre Paid.
