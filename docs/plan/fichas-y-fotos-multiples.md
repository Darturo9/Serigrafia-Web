# Fichas y fotos múltiples — paquete para revisión

Fecha: 8 de octubre de 2026. Implementación y paquete remoto aprobados; migraciones, permisos y despliegue protegido verificados (ADR 009). R02/R03/R07/R08/R09, A03/A05/A06/A07/A10/A11/A12.

## Comportamiento implementado

- Catálogo: portada y «Ver producto»; productos reales tienen «Quiero este producto».
- Ficha `/productos/<id>/`: descripción, tallas/opciones confirmadas, portada y miniaturas; hasta seis fotos visibles. Sin fotos se muestra un aviso; con una no hay selector. Las miniaturas funcionan con teclado y como enlaces a imagen si JavaScript está desactivado.
- «Quiero este producto» lleva a cantidades/opciones en la ficha. El mensaje incorpora el producto de la ruta, aunque se manipule un ID enviado, y usa el WhatsApp confirmado. No guarda pedidos ni envía mensajes.
- Ocultos e IDs inexistentes: 404. Ejemplos: solo visibles en revisión; aviso explícito y sin compra/cotización.
- Admin: edición inline de fotos, descripción, orden y estado visible; portada elegida entre fotos activas del propio producto después de guardarlas. Máximo seis activas; conservar desactivadas y archivos. Permisos de foto: ver/agregar/cambiar, sin borrar ni administrar usuarios.
- Nueva tabla ProductoImagen y referencia nullable Producto.portada. Se conserva Producto.foto. Migración de datos registra cada referencia anterior como imagen/portada sin copiar, sobrescribir ni eliminar objetos Storage. Reemplazos del campo anterior actualizan su referencia registrada; si existen fotos relacionadas, estas gobiernan la presentación. Sin portada explícita se usa la primera activa por orden/ID.
- Misma validación y backend WebP existentes. Un fallo de carga revierte la transacción del Admin y conserva referencias anteriores. Archivos subidos antes del fallo pueden quedar sin referencia; sus nombres se registran en logs para revisión, sin borrado automático.

## Evidencia local

51 pruebas pasan en SQLite y PostgreSQL local: 43 anteriores y ocho de ficha/datos/permisos. Cobertura 0/1/6 fotos, límite de seis, fotos inactivas, portada ajena/inactiva, ocultos/ejemplos, validación de cantidades, manipulación de ID, migración que conserva referencia/bytes y rollback de carga. `makemigrations --check --dry-run` y `check` aprobados.

Fixture aislada y claramente rotulada: `scripts/producto_demo_local.py`, SQLite/fotos/credencial exclusivamente en `.local/producto-demo/`, sin datos remotos. Ensaya migración desde el modelo antiguo con una foto real local y añade referencias Pexels de prueba. Navegador: miniatura cambia imagen/texto; selección y mensaje con M/L verificados sin abrir/enviar chat; sin desbordamiento en escritorio/390 px. Capturas `.local/design-review/ficha-producto.png` y `ficha-producto-movil.png`. Fotos de fixture no son productos/trabajos de JYZ.

## Paquete remoto autorizado y ejecutado

Destino exclusivo: Supabase `kcahxuvfmrzxzlnpezyf`, esquema `jyz_prueba`; Railway `jyz-revision` / `jyz-web`. No intervenir `vibrant-perfection`.

1. Aplicar únicamente `catalogo.0002_productoimagen_producto_portada` y `catalogo.0003_registrar_fotos_actuales`, mediante Django y rol migrador existente. SQL de estructura revisable: `ops/catalogo-0002-fotos.revision.sql`. La segunda migración usa ORM y registra las referencias existentes. Inspección de solo lectura: tres productos, tres fotos previas; columna portada y tabla de imágenes todavía ausentes. No crear productos de prueba adicionales remotos ni subir nuevas fotos para esta aplicación.
2. Preparar los permisos de imágenes en el grupo existente «Responsable de catálogo» usando el rol de aplicación. No convertir usuarios en superusuarios, no conceder borrado ni gestión de usuarios. Las reglas existentes de privilegios por defecto ya cubren tablas/secuencias nuevas del migrador; no crear roles, buckets ni servicios.
3. Redesplegar únicamente el servicio de revisión JYZ con el código nuevo, conservando Basic/noindex y los secretos actuales. No hay `migrate` automático en arranque. Verificar antes/después que las referencias antiguas no cambiaron y tienen portada relacionada.
4. Verificar HTTPS, ficha del ejemplo visible sin compra, ocultos 404, portada servida por URL firmada, Admin inline con el acceso limitado y logout. El recorrido comercial completo se prueba localmente porque aún no hay catálogo real; no convertir el ejemplo remoto en producto real para probar compra.

Comandos preparados, ejecutar solo después de esa autorización:

```sh
JYZ_REMOTE_ROLE=jyz_migrator DJANGO_SETTINGS_MODULE=config.settings_supabase_test .local/workers-venv/bin/python manage.py migrate catalogo 0003
JYZ_REMOTE_ROLE=jyz_app DJANGO_SETTINGS_MODULE=config.settings_supabase_test .local/workers-venv/bin/python manage.py preparar_rol_catalogo
```

Antes de ejecutar, confirmar nuevamente que el plan contiene solo estas dos migraciones. Después, comprobar referencias/filas y permisos con el rol de aplicación antes del despliegue. Si falla el build, conservar el esquema aditivo y volver a la versión anterior de la aplicación: el campo de foto viejo sigue presente. No revertir/eliminar la tabla de fotos como recuperación automática.

## Pendientes

Revisión visual humana y teléfono físico. Paquete remoto autorizado y verificado. Apertura humana de WhatsApp, fotos/productos reales y entrega del dueño continúan pendientes. Esta etapa no autoriza lanzamiento comercial, compra/DNS, limpieza de Storage, commit/push ni nuevas instalaciones.

Verificación adicional: ocho pruebas nuevas, 51 totales aprobadas en SQLite y PostgreSQL. Carga múltiple parcialmente fallida revierte cambios y registra el archivo subido sin referencia, sin borrarlo. Navegador: miniatura activada con Enter cambia foto/estado. Siete comprobaciones HTTP del Admin local: inline, sin borrado, selector de portada, usuarios 403, guardar portada/reflejo en ficha/restauración; evidencia .local/producto-demo/admin-http.json. Servidor demo local activo en 8002.

## Resultado remoto

Usuario confirma «autorizo» el 8 de octubre. Plan de Django contiene solo 0002/0003; ambas aplicadas con jyz_migrator. Tres fotos registradas, tres productos conservados; comparación de referencias y SHA-256 de bytes antes/después aprobada para cada foto. Grupo de catálogo contiene seis permisos (ver/agregar/cambiar productos e imágenes), sin borrado ni usuarios; danilo conserva acceso limitado. Evidencia .local/railway-prueba/fichas-migracion.json y snapshot privado fichas-antes.json.

Railway fbda1822-3da5-4f22-b1a7-827aa344600a SUCCESS, únicamente jyz-revision/jyz-web. Diecisiete comprobaciones HTTPS aprobadas: salud, revisión protegida/noindex, enlace del catálogo, ficha de ejemplo sin compra, ausencia de selector con una foto, foto con mismos bytes, CSS/JS exactos, dos ocultos/ID inexistente 404, login, inline/portada, sin borrado de fotos, usuarios 403 y logout. Script scripts/railway_fichas_probe.py y evidencia .local/railway-prueba/fichas-http.json / deployment-fichas.json. Sin productos nuevos ni nuevas subidas remotas.

Captura ficha-producto-actual.png corresponde al navegador local con los mismos datos Supabase/código desplegado. El navegador remoto no pudo superar la autenticación Basic en esta sesión; verificación remota es HTTP autenticado, sin afirmar revisión visual remota. Recorrido comercial y seis fotos comprobados con fixture local, porque los productos remotos siguen siendo ejemplos. Sin compras, DNS, commit/push ni cambios en vibrant-perfection. Implementación técnica completada; aceptación humana/contenido comercial siguen pendientes.
