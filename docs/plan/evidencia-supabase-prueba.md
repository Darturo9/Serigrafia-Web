# Prueba autorizada en Supabase

Fecha: 8 de octubre de 2026. Proyecto verificado: kcahxuvfmrzxzlnpezyf, JYZ, región us-west-2. Autorización directa del usuario para el paquete de esquema, roles, migraciones, bucket y datos sintéticos. Cloudflare y despliegues excluidos.

## Aplicado y verificado

- Esquema jyz_prueba propietario jyz_migrator. Roles separados, sin superusuario/creación de bases/roles/BYPASSRLS. Credenciales SCRAM y archivos de conexión locales con permisos 0600; sin valores en código/documentos. Roles activados con login para la prueba autorizada.
- La primera transacción falló por SET ROLE y revirtió todo. La segunda falló por default privileges y también revirtió. Se corrigió ejecutando los permisos como propietario, con membresía temporal de postgres retirada al terminar. Verificación posterior corrigió USAGE de jyz_app mediante otra transacción.
- Conexión del Mac por pooler de sesión aws-1-us-west-2.pooler.supabase.com:5432, obtenido del dashboard del proyecto. La conexión directa IPv6 no resolvió en el Mac. No se compró IPv4 ni se cambió el origen propuesto de Hyperdrive.
- Primer intento TLS falló con CA del sistema. Se descargó la CA mediante el enlace oficial del dashboard y se configuró sslmode=verify-full con ese certificado. No se desactivó validación TLS.
- migrate de Django ejecutado como jyz_migrator, fuera del Worker: las 19 migraciones aplicadas correctamente. Historial Django confirmado por MCP: 19 filas, 11 tablas, todas propiedad de jyz_migrator.
- ACL: jyz_app tiene SELECT/INSERT/UPDATE/DELETE de tablas; USAGE del esquema, sin CREATE. anon/authenticated sin USAGE del esquema ni SELECT de tablas. Sin Supabase Auth incorporado.
- ORM de Django usando jyz_app creó/editó/releyó producto sintético ID 1, es_ejemplo=True y publicado=False. Consulta posterior desde otro proceso confirma lectura y 19 migraciones. No son materiales comerciales ni evidencia de Workers/Hyperdrive remoto.
- Bucket creado mediante dashboard: jyz-prueba-fotos, public=False, file_size_limit=5242880 y MIME image/jpeg,image/png,image/webp, comprobado por SELECT MCP. Sin INSERT manual en tablas internas Storage.

## Fotos y panel verificados

El usuario confirmó la provisión de la clave en el archivo local el 8 de octubre. Se comprobó que está presente, no vacía y con permisos 0600, sin imprimir su valor. La clave funcionó contra el proyecto autorizado; no está en el navegador ni en esta documentación. El usuario informó que reemplazó la clave. Su lectura privada se verificó nuevamente sin modificar datos; no se verificó la revocación de la clave anterior.

- `scripts/supabase_fotos_prueba.py`: carga PNG, JPEG y WebP mediante el backend Django; existencia, tamaño, lectura privada y URL firmada comprobados comparando bytes/hashes. La lectura pública sin autorización fue rechazada. Una imagen inválida conserva la referencia anterior.
- Lectura desde un segundo proceso confirma persistencia de la foto y su hash. Esto no equivale a reiniciar o redesplegar Workers.
- `scripts/supabase_admin_prueba.py`: 14 comprobaciones aprobadas con Django Client nativo, PostgreSQL y Storage reales: acceso anónimo restringido, login/logout, panel, permisos limitados, CSRF, edición, publicación temporal, carga de foto, rechazo de imagen corrupta, conservación de foto anterior y ocultación. El producto de ejemplo queda excluido del inicio comercial.
- Estado final confirmado mediante SELECT MCP: 19 migraciones, 11 tablas con RLS habilitado, cuatro objetos sintéticos en el bucket y producto de prueba oculto. No se eliminaron las fotos reemplazadas.
- Política de servidor `jyz_app_servidor` para el rol `jyz_app`; `anon` y `authenticated` sin USAGE del esquema. El acceso de la aplicación sigue funcionando con RLS. La cuenta migradora conserva propiedad para migrar fuera del Worker.
- Dashboard Data API consultado sin guardar cambios: solo `public` y `graphql_public` seleccionados; `jyz_prueba` sin seleccionar, 0 de 11 tablas expuestas. La opción global de exponer nuevas tablas continúa activada; no crear tablas comerciales en esquemas expuestos sin revisar permisos.
- Asesor de seguridad MCP devolvió `lints: []` tras las modificaciones. No sustituye una auditoría integral.

## Pendiente

Se comprobó lectura del backend contra Storage desde WebAssembly en workerd local; posteriormente se comprobó carga sintética desde ese runtime; Workers/Hyperdrive remoto sigue sin ejecutar. Faltan autorización específica y configuración de esos recursos, transporte HTTP del runtime, prueba de reinicio/redespliegue, recuperación, cuotas y costo en la cuenta real. ADR 001 continúa propuesto. La org figura FREE en dashboard, sin garantía de costo cero.

## Evidencia local

Registros sin claves: `.local/supabase-prueba/migrate.log`, `orm.log`, `fotos-result.json`, `persistencia-foto.log`, `admin-result.json` y `admin-test.log`. Las pruebas de fotos y panel se ejecutan explícitamente; no repetirlas como una inspección, pues escriben datos sintéticos. config/settings_supabase_test.py restringe rol/proyecto/host/esquema y verifica TLS. Credenciales y verificadores locales excluidos de versiones; no entregarlos como documentación pública.

Captura sin claves: .local/design-review/supabase-bucket.jpg. SQL base en ops/01-esquema-y-roles.propuesto.sql se conserva con estado aplicado y correcciones; no ejecutarlo nuevamente sin inspección, porque los roles/esquema ya existen.

Fuentes: https://supabase.com/docs/guides/database/connecting-to-postgres y https://supabase.com/docs/guides/platform/ssl-enforcement.

## Comprobación posterior al reemplazo de clave

8 de octubre: el usuario confirmó reemplazo del archivo. Django nativo con jyz_app comprobó existencia y lectura de la foto actual del producto sintético oculto; 137 bytes. Sin cargar, editar ni borrar datos. Archivo con permisos 0600. Evidencia sin secretos: `.local/supabase-prueba/key-replacement-check.json`. La prueba confirma que la credencial actual funciona; no acredita que la anterior esté revocada.

## Transporte Storage desde WebAssembly local

8 de octubre: scripts/worker_storage_read_probe.py ejecutado en workerd local con ruedas fijadas y credencial guardada únicamente en .dev.vars local 0600, excluido de Git. Endpoint loopback protegido por token aleatorio; proceso terminado al concluir. No incorpora ruta de diagnóstico al Worker comercial ni realiza cargas/ediciones/borrados remotos.

Primeros dos intentos: fallo AttributeError getReader en jsfetch al procesar HEAD sin cuerpo. Corregido config/storage/supabase.py: exists consulta GET object/info para comprobar metadatos sin descargar imagen. Tercer intento: existencia, tamaño y lectura privada aprobados. Cuarto intento amplía evidencia a generación/lectura de URL firmada y acceso público rechazado; no almacena URL ni token firmado en el resultado. Foto actual: 137 bytes, mismo SHA256 que lectura nativa.

Evidencia: .local/worker-storage-read-4/result.json, anteriores conservados; .local/storage-wasm-regression-tests.log confirma 31 pruebas nativas aprobadas, incluida regresión para no volver a HEAD. Paquete remoto actualizado y dry-run aprobado: 44377.92 KiB. Esto no prueba upload desde WASM, Hyperdrive, CPU/memoria en Cloudflare, ni persistencia tras redespliegue.

## Carga de fotos desde WebAssembly local

8 de octubre: `scripts/worker_storage_read_probe.py --upload-synthetic` amplía la prueba explícitamente dentro de la autorización Supabase ya recibida. La ejecución local crea tres fotos sintéticas de 16 × 16 píxeles mediante Pillow WASM y las guarda a través del backend Storage actual: PNG 82 bytes, JPEG 633 bytes y WebP 68 bytes. Verificados existencia, tamaño, bytes privados, SHA256 y lectura mediante URL firmada en los tres casos. Imagen corrupta rechazada antes de cargar.

Resultado aprobado en `.local/worker-storage-read-5/result.json`. Los tres objetos adicionales se conservan sin borrado; ninguna referencia de producto fue modificada. Tras terminar workerd, otro proceso Django nativo releyó los tres objetos y comprobó sus hashes: `.local/worker-storage-read-5/persistence.json`. Producto ID 1 sigue siendo ejemplo oculto. No equivale a redespliegue de Workers ni demuestra conexión Hyperdrive.

Esta comprobación utiliza PostgreSQL nativo únicamente para identificar/confirmar el producto existente, y Storage desde WASM para cargar/leer fotos; el ORM no se ejecutó contra Hyperdrive remoto. Sin recursos Cloudflare, cambios de cuenta/plan, compras, commit ni push.
