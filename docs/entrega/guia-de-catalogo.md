# Guía para administrar el catálogo JYZ

Versión de revisión Railway, 8 de octubre de 2026. Cubre R07, R08 y preparación de R10. **No acredita entrega ni capacitación completada (A12).** Alojamiento de revisión verificado; Mryoan creado y verificado; práctica de galería confirmada por el usuario. Práctica con productos comerciales después de la entrega. El usuario confirmó que el dueño administrará el panel.

## Entrar al panel

Abra [el panel JYZ](https://jyzgt.com/admin/). Solo necesita el usuario y contraseña de Django (cuenta Mryoan). La protección HTTP Basic anterior fue retirada por instrucción del usuario (ADR 020); ya no aparece una primera ventana de acceso. El panel conserva sesión privada, HTTPS y permisos acotados.

El perfil **Responsable de catálogo** permite ver, agregar y editar productos. No permite borrar productos ni administrar usuarios. Si no aparecen Productos o Agregar, solicite al responsable técnico que revise su acceso; no use una cuenta de otra persona. Las credenciales de prueba técnica no se entregan como acceso definitivo del negocio.

## Agregar un producto

Entre en **Productos** y seleccione **Agregar producto**. Complete los campos con información confirmada del negocio:

| Campo | Qué escribir |
|---|---|
| Nombre | Nombre real, hasta 160 caracteres. |
| Descripción | Información confirmada, hasta 2000 caracteres. No agregar precios, disponibilidad ni promesas que el negocio no haya confirmado. |
| Categoría | Clasificación opcional, hasta 100 caracteres. |
| Tallas | Lista de las opciones reales de ese producto. El campo actual usa formato JSON; consulte el ejemplo siguiente. |
| Foto | Fotografía autorizada del producto; JPEG, PNG o WebP. |
| Descripción de la foto | Texto breve que explique lo que muestra, hasta 200 caracteres. |
| Publicado | Marcar para mostrarlo en el catálogo; dejar sin marcar mientras se revisa. |
| Orden | Entero no negativo; los valores menores aparecen primero. A igual orden, se ordena por nombre y luego por identificador. |
| Dato de ejemplo | Exclusivo de pruebas. Los productos reales deben quedar sin esta marca; no convertir datos inventados en reales cambiando solo la casilla. |

Ejemplo **de formato**, no de tallas disponibles del negocio:

```json
["S", "M", "L"]
```

Use comillas dobles, comas entre valores y corchetes. Para no declarar opciones use `[]`. No deduzca las tallas por el texto general “todas las tallas”: confirme cuáles corresponde ofrecer en cada producto. Se permiten hasta 30 opciones únicas, de hasta 20 caracteres cada una; no agregue cantidades de inventario.

Pulse **Guardar**. Si aparecen errores, corrija los campos señalados y vuelva a guardar. Después abra el catálogo en otra pestaña y compruebe nombre, descripción, foto y opciones. Si lo guardó como oculto, no debe aparecer allí.

## Editar y cambiar la foto

Busque el producto por nombre o descripción en **Productos** y abra su nombre. Cambie los campos necesarios. Para reemplazar su foto, seleccione el nuevo archivo y pulse **Guardar**. Compruebe el resultado en el catálogo.

La foto debe ser JPEG, PNG o WebP estático, pesar como máximo 5 MB y no superar 16 megapíxeles (ancho × alto). En Supabase, las nuevas cargas se optimizan automáticamente: orientación correcta, WebP calidad 80 y máximo 1600 píxeles sin recortar ni ampliar. Si sigue pesada, se reduce proporcionalmente hasta cumplir 500 KB. Se conservan transparencias y se eliminan metadatos de la copia web. No necesita convertirla manualmente; conserve el original para trabajos de impresión. Un archivo corrupto o de otro formato se rechaza. Un reemplazo inválido conserva la foto anterior; las comprobaciones locales y HTTP en Railway lo verificaron. Las imágenes de referencia recibidas no son automáticamente fotos autorizadas del catálogo.

Si aparece “No se guardaron los cambios porque la foto no pudo almacenarse”, los cambios de esa operación no se guardaron. La foto anterior se conserva. Revise el producto y vuelva a seleccionar el archivo al reintentar. Si se repite, comuníquelo al responsable técnico; no cambie permisos de almacenamiento ni comparta claves.

En el backend remoto verificado, reemplazar una foto no elimina físicamente el archivo anterior. La limpieza requiere un procedimiento autorizado del responsable técnico. Esta guía no ordena borrar archivos.

## Ocultar y volver a mostrar

Abra el producto, desmarque **Publicado** y guarde. Compruebe en el catálogo que desapareció. Para volver a mostrarlo, marque **Publicado**, guarde y revise otra vez. Ocultar es la operación disponible al responsable de catálogo; no necesita borrar el producto.

Ocultar no modifica inventario ni cancela conversaciones o pedidos. En Storage privado se generan enlaces firmados temporales. Ocultar el producto lo retira del catálogo; no revoca inmediatamente un enlace de foto ya emitido.

## Al terminar

Use **Cerrar sesión** en el panel, especialmente en equipos compartidos. No comparta contraseñas, claves de Supabase o accesos de Cloudflare por capturas o mensajes públicos. El restablecimiento de acceso debe gestionarlo la persona responsable de usuarios; no hay recuperación por correo configurada ni verificada.

El panel administra productos y galería. Cotizaciones, diseños y consultas se atienden por WhatsApp; la web no guarda pedidos ni estados de producción. El formulario de idea y las fichas comerciales preparan mensajes para revisar y abrir WhatsApp; el visitante debe enviarlos en el chat. Las fichas sintéticas quedaron ocultas en la entrega ADR 017.

## Comprobación de capacitación pendiente

La persona designada deberá completar, con su propio acceso definitivo:

1. Crear un producto oculto con información y foto autorizadas.
2. Publicarlo y comprobarlo desde otra sesión del navegador.
3. Editar descripción/opciones y reemplazar la foto; verificar el resultado.
4. Ocultarlo y volver a publicarlo.
5. Cerrar sesión y confirmar que el panel exige volver a entrar.

Registrar fecha, entorno, responsable y resultado sin contraseñas. Solo entonces podrá darse por completado A12. La confirmación humana del panel anterior se conserva, pero no sustituye esta capacitación con la guía y acceso definitivo.

## Base de esta guía

Campos y límites revisados en `catalogo/models.py`, `catalogo/forms.py`, `catalogo/admin.py` y el comando `preparar_rol_catalogo`. Verificación: suite nativa y 22 comprobaciones HTTP reales del Admin en Railway, incluyendo sesiones, CSRF, permisos, creación/edición/ocultación y fotos PNG/JPEG/WebP. Persistencia tras redespliegue verificada. Ver ../plan/evidencia-railway-prueba.md. Esto no sustituye la práctica del dueño en A12.

Las fotos del Worker local están en memoria; no conservarlas allí como único original. La prueba Django original guarda fotos en disco local. Ninguna prueba local sustituye respaldo, recuperación o persistencia remota. Conserve sus archivos originales y espere las instrucciones definitivas de entrega.

## Ejemplo autorizado en la revisión

El producto «Prenda de prueba · referencia Unsplash» conserva la marca Dato de ejemplo. Solo se muestra en el perfil protegido de revisión Railway, con aviso de no venta. No cambie esa marca para convertirlo en oferta real: cree la ficha comercial con datos y foto aprobados cuando estén disponibles.

La recuperación tiene un [plan separado](respaldo-y-recuperacion.md), todavía sin exportación ni restauración ejecutadas.

Las fotos existentes no se convierten ni borran en lote. Al reemplazar una foto se guarda una nueva copia WebP; los errores de conversión/carga conservan la referencia anterior.

## Panel con identidad JYZ

Lista: miniaturas, nombre, categoría, visibilidad y tipo de contenido. Seleccione el nombre para editar. Los filtros distinguen publicado, oculto y ejemplo. La ficha agrupa información, tallas/opciones, fotografía y publicación. “Publicado” no transforma un ejemplo en un producto real; conservar su identificación. La foto actual tiene vista previa y las nuevas cargas mantienen optimización WebP. La portada conserva únicamente los módulos permitidos por su cuenta.

## Varias fotos y ficha del producto

Aplicación verificada en Railway con el paquete autorizado ADR 009. En la edición de producto, agregar fotos en el bloque inferior, escribir descripciones, asignar orden y activar «visible». Guardar; después elegir una portada entre las fotos activas del producto. Máximo seis visibles; desactivar para retirar sin borrar. Si la portada debe desactivarse, elegir otra o dejar la selección vacía en el mismo guardado. Revisar «Ver producto» en el catálogo. Las fotos actuales se conservan. Los productos de ejemplo se pueden revisar, pero no cotizar/comprar.

## Galería «Ideas que toman forma» — habilitada en Railway

Abra [Admin → Galería](https://jyz-web-production.up.railway.app/admin/catalogo/galeriaimagen/) con sus accesos actuales. Módulo habilitado y verificado por HTTPS (ADR 016). Para agregar: Añadir foto de galería. Escriba un título y una descripción de lo que se ve, seleccione JPEG/PNG/WebP y guarde. Supabase optimiza automáticamente; conserve el original fuera del sitio para impresión. No afirme precios, técnica ni disponibilidad sin confirmarlos.

Abra el título para reemplazar foto o editar texto. Los números menores en Orden aparecen primero. Desmarque Visible y guarde para ocultar sin borrar; orden/visible también se cambian desde la lista con Guardar. Si oculta todas las fotos, desaparece la sección y el enlace Trabajos. Si una carga falla, la foto anterior se conserva; seleccione nuevamente el archivo. Revise el inicio público después de guardar. La galería es independiente de las fichas de productos y no crea cotizaciones.

Las tres fotos recibidas ya están cargadas. Título y descripción se editan para cada foto; el encabezado «Ideas que toman forma» y la introducción general todavía se cambian en la plantilla. Edición, orden y ocultación comprobados en Railway y restaurados tras la prueba; la capacitación del dueño sigue pendiente.

## Responsables confirmados y acceso por preparar

El usuario confirmó a Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid como nombres del negocio y responsables de atención por WhatsApp. Usuario solicitado para entrar al panel: **Mryoan**. Mryoan está creado y su login HTTPS verificado (ADR 017); asociación a una persona, entrega segura al negocio y práctica humana pendientes. El perfil previsto es Responsable de catálogo, con productos, imágenes y galería, sin borrar ni administrar usuarios. La cuenta de Danilo se conserva separada.

Para la entrega vigente, consulte [entrega operativa](entrega-operativa.md). El catálogo real lo carga el negocio después; cuenta, guía y capacidad de carga están disponibles.

## Catálogo inicial y tallas generales — ADR 019

El catálogo inicial tiene once fichas de las fotos seleccionadas. Sin precios; precio/medidas se conversan por WhatsApp. La opción general se escribe exactamente ["Todas las tallas"] en el campo tallas; el cliente podrá escribir las tallas que necesita al cotizar. Si se reciben opciones concretas, reemplazar por una lista confirmada, por ejemplo ["S", "M", "L"], y el formulario solicitará cantidades por talla. No inventar rangos o medidas.

Panel vigente: https://jyzgt.com/admin/. Usa únicamente el login Django con Mryoan (ADR 020). Catálogo cargado con once fotos; cinco pixeladas quedaron fuera y un duplicado se omitió. Fotos originales conservadas.
