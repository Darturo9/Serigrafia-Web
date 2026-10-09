# Respaldo y recuperación — primera prueba ejecutada

Fecha: 8 de octubre de 2026. Relacionado con R10/A13. La persistencia tras redespliegue ya se verificó; todavía no existe evidencia de restauración. Este documento no ejecuta copias, SQL ni cambios remotos.

## Qué conservar

- Código y dependencias fijadas del paquete Railway; commit/push pendientes de autorización.
- Datos del esquema jyz_prueba y referencias de las fotos, incluyendo configuración/usuarios Django. Las copias contienen datos sensibles: acceso restringido, cifrado y entrega por canal seguro; nunca dentro del repositorio o evidencias públicas.
- Objetos del bucket privado jyz-prueba-fotos, con nombres/rutas exactos y hashes. Un respaldo de PostgreSQL no contiene los archivos Storage.
- Inventario de proyecto/servicio Railway, versión activa, nombres de variables, CA pública, ruta de salud, protección de revisión y permisos. Credenciales únicamente en el canal seguro acordado, separadas del inventario.

## Primera prueba propuesta

1. Confirmar con el dueño quién conserva las copias, dónde, frecuencia, retención y plazo de recuperación esperado. No asumir que el mínimo Hobby o un plan Supabase incluyen el respaldo requerido.
2. Obtener autorización para exportar datos y fotos del proyecto de prueba hacia un destino privado acordado. Registrar fecha, tamaño, hashes y conteos sin imprimir secretos. Comprobar que el rol de lectura puede exportar las tablas bajo sus políticas RLS; no ampliar permisos automáticamente si falla.
3. Solicitar autorización específica para un destino de restauración aislado. Nunca restaurar sobre el esquema activo ni sobre vibrant-perfection. No crear otra base, bucket, servicio o plan por el solo hecho de existir este documento.
4. Restaurar tablas y objetos con sus rutas, comprobar conteos/hashes y probar login, catálogo y lectura de foto usando un servidor de revisión aislado. Confirmar opciones de restauración para no trasladar propietarios/permisos privilegiados del origen.
5. Registrar el tiempo real y cualquier pérdida o inconsistencia. Solo una restauración ejecutada y comprobada acredita recuperación. Conservar las fuentes y no borrar recursos/copias sin autorización.

## Incidentes

Si falla una nueva versión del código, revisar salud/registros y proponer volver a una versión Railway verificada. Un rollback del servidor no restaura datos ni fotos. Si se pierde una foto o un registro, usar la copia verificada y autorizar explícitamente su restauración. Si se compromete una clave, el dueño debe revocarla/reemplazarla por el canal seguro; comprobar sus consumidores sin exponer valores.

## Estado

Pendientes: responsables, destino/frecuencia/retención, autorización de exportación/restauración y prueba real. No prometer pérdida cero ni recuperación inmediata. La clave Storage anterior fue reemplazada, pero su revocación aún debe confirmarse por el titular.

## Resultado vigente — ADR 017

Exportación y recuperación autorizadas por el usuario. Supabase confirma PostgreSQL 17.11; se usó pg_dump/pg_restore 17.11 del contenedor exclusivo jyz-recuperacion-20261008, sin instalar dependencias nuevas. Dump lógico de las 13 tablas de jyz_prueba, --no-owner/--no-acl; copia de los 15 objetos completos del bucket privado (incluidos reemplazos) y originales JYZ. Conexión remota SSL verify-full mediante rol limitado jyz_migrator, sin exportar esquemas ajenos. Roles/secretos se reconstruyen por separado, no se asumen incluidos en el dump.

Cifrado AES-256-CBC/PBKDF2 con 200000 iteraciones y HMAC-SHA256 externo; clave aleatoria separada en archivo 0600. Descifrado y archivo tar comparados por SHA-256, 15 objetos comparados por hash y 13 conteos coincidentes antes de login. Restauración exclusivamente PostgreSQL 17 local, 127.0.0.1:55441; nunca sobre Supabase activo. Rol local acotado, políticas RLS restauradas y permiso DELETE exclusivo para django_session por necesidad de login/logout; productos/galería mantienen prohibición de borrado en Admin. Mryoan restaurado inició sesión; panel/galería accesibles, usuarios/borrado rechazados, catálogo vacío renderizado y tres fotos WebP locales leídas.

Incidencias corregidas solo en destino local: pg_hba inicial no admitía la dirección del bridge Docker; se habilitó ese acceso con contraseña SCRAM y puerto ligado exclusivamente a loopback. La copia Docker del dump requirió cambiar propietario a postgres. Se añadió DELETE de sesiones al reconstruir grants para el ciclo de sesión Django. Ninguna incidencia alteró producción. Medición de 0,11 s corresponde solo al tramo final pg_restore/conteos, no a exportación, correcciones, descifrado ni tiempo garantizado de recuperación.

Evidencia sin secretos: .local/entrega-jyz/respaldo-recuperacion.json. Archivo cifrado 1157152 bytes; dump 49838 bytes. Copia en /Users/danilo/Documents/JYZ-respaldos/2026-10-08; contraseña/clave por separado en .local/entrega-jyz. Datos intermedios locales de la prueba se limpian una vez comprobados; el contenedor de recuperación se detiene, conservando su estado para inspección. Copia original cifrada y fuentes remotas permanecen.

Pendientes operativos: custodia por el negocio, copia cifrada fuera del equipo, frecuencia aplicada por su responsable y retención efectiva. No hay respaldo periódico automatizado ni restauración en otro proveedor comprobados. Consultar entrega-operativa.md. La revocación de la clave Storage anterior sigue sin evidencia de revocación; la clave vigente carga/lee correctamente, lo que no prueba la revocación anterior.
