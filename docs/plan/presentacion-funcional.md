# Presentación funcional de JYZ

Fecha: 8 de octubre de 2026. Relacionado con R01–R10, A01–A13 y ADR 008.

## Ya funcional y verificable

Django, plantillas, panel privado y fotos en Railway/Supabase. Usuario danilo puede ver/agregar/editar productos. Nuevas fotos se optimizan a WebP. WhatsApp prepara mensajes y abre un enlace, sin guardar pedidos ni enviar automáticamente. Dominio predeterminado Railway aprobado; comprar dominio propio no es necesario para presentar ni usar el sitio.

## Qué significa retirar «prueba/local»

| Superficie | Estado / acción necesaria |
|---|---|
| Títulos del Admin | ADR 008 sustituye «Catálogo local» y «prueba local» por identidad JYZ. No altera datos o permisos. |
| Raíz `/` | Corregido por ADR 015: `/` muestra inicio, `/inicio/` es alias; catálogo técnico `/catalogo/` exige clave. |
| Franja «Vista de revisión» | Retirarla al aprobar la presentación final, no antes de resolver lo que anuncia. |
| Producto Unsplash de ejemplo | Ocultarlo de la web. No basta cambiarle el nombre o desmarcar ejemplo: su foto/descripción no son un producto confirmado. Conservar datos y objetos para no borrar evidencia. |
| Otros productos sintéticos | Ya ocultos de la página comercial; mantener fuera del catálogo público. Se pueden conservar en el panel con identificación o filtrar ejemplos. |
| Fotos y galería | Usar fotos propias/autorizadas; si aún no hay trabajos, acordar omitir temporalmente la galería y su enlace en navegación. Nunca sustituir referencias por supuestos trabajos reales. |
| Catálogo y cotización | Cargar fichas reales con nombre, descripción, tallas/opciones y foto. Si todavía no existen, acordar una primera presentación enfocada en consulta de personalización por WhatsApp, sin simular productos disponibles. |
| `noindex` / acceso de revisión | ADR 014 ya abre páginas/estáticos públicos sin Basic. Admin y catálogo técnico conservan la clave y el login Django. noindex y aviso de revisión siguen presentes; contenido final y presencia en buscadores pendientes. |
| Esquema/bucket con nombre de prueba | Sus nombres son internos: no hace falta renombrarlos para quitar textos de prueba de la interfaz. Crear/migrar otros recursos sería un trabajo distinto; no lo realizar silenciosamente. |

## Comprobaciones para la presentación

1. Danilo revisa la propuesta visual del panel y practica edición/ocultación con un ejemplo identificado; el dueño recibe su propia cuenta y capacitación cuando se acuerde la entrega.
2. Confirmar desde un teléfono que WhatsApp abre +502 47233834 y muestra el mensaje correcto, sin necesidad de enviarlo. Validar navegación y formulario; comprobar enlaces de redes actuales con el negocio.
3. Elegir contenido para la primera presentación: catálogo real, o consulta de personalización sin fichas ficticias ni galería pendiente. Revisar textos y fotos con la persona del negocio.
4. Antes de operación comercial, acordar responsables, presupuesto, copias privadas de datos y fotos, y ejecutar restauración en destino aislado autorizado. Confirmar revocación de la clave anterior. Persistencia probada no acredita recuperación.
5. Autorizar específicamente los cambios de lanzamiento: ruta principal, contenido final y apertura pública, con Admin privado y exclusión de ejemplos. Ejecutar después las pruebas de ese perfil; no asumir que el entorno protegido ya demuestra el perfil público.

## Límites de esta tarea

La instrucción actual autoriza personalizar el Admin y explicar estos pendientes. No se eliminan ejemplos/objetos, no se retira la protección ni se publica comercialmente. No se modifica vibrant-perfection, no se compra dominio, no hay commit/push ni instalaciones nuevas. Una presentación privada a la amiga ya puede hacerse con el enlace Railway y acceso de revisión; no exige terminar la entrega comercial.

## Material para galería

Propuesta práctica: empezar con 4–6 fotos de trabajos propios (cantidad sugerida, no requisito mínimo). Por foto: archivo de buena calidad, nombre/descripción breve, técnica si está confirmada y permiso de publicación; confirmar consentimiento si se identifican clientes/personas. Las imágenes del PDF están rotuladas como referencias y no acreditan trabajos realizados. El catálogo presenta productos ofrecidos; la galería muestra ejemplos reales de trabajos. No hay sincronización automática con Instagram ni gestión independiente de galería en el Admin. Puede prepararse una primera galería fija con material aprobado; edición por el dueño requiere acordar esa ampliación.

## Auditoría actual

Ver [revisión del usuario final](auditoria-usuario-final.md), con evidencia de acceso público, recorridos de idea/producto, adaptación y pendientes reales. Reemplaza las afirmaciones antiguas de raíz técnica y clave para toda la web; no constituye aceptación comercial.

## Estado vigente tras ADR 017

El usuario autorizó la entrega sin catálogo comercial inicial. Fichas de prueba ocultas, Mryoan habilitado, galería administrable real, aviso/noindex público retirados, revisión física del teléfono confirmada y respaldo/restauración local ejecutados. Los apartados anteriores describen la propuesta histórica. Ver ../entrega/entrega-operativa.md para requisitos vigentes y limitaciones; no asumir entrenamiento humano completo ni backups automáticos.
