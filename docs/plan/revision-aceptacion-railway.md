# Revisión de aceptación JYZ — Railway

Fecha: 8 de octubre de 2026. Referencia: especificación 05. Prueba técnica y vista de revisión, no aceptación comercial.

| Criterio | Evidencia actual | Falta para aceptar |
|---|---|---|
| A01 | Logo/textos del PDF y WhatsApp +502 confirmados; primera sección aprobada. | Catálogo/fotos reales, enlaces de redes y revisión final. |
| A02 | 22 comprobaciones Admin HTTPS: sesión, CSRF, permisos acotados y logout. | Cuenta definitiva del dueño y revisión humana remota. |
| A03–A05 | CRUD/ocultación y nuevas cargas optimizadas a WebP verificados por HTTPS Admin. Foto de ejemplo: 399222 → 49098 bytes, 1600 × 1067 px; reemplazo inválido conserva la anterior. Orientación, transparencia y peso cubiertos por pruebas locales. | Aplicarlo a fichas comerciales confirmadas; no convertir ejemplos en reales. |
| A06 | Nueva versión y proceso releen producto/foto con mismo hash. | Respaldos y recuperación no quedan probados por esta persistencia. |
| A07 | URL internacional y acentos correctos en lógica, navegador y HTTP Railway; revisión previa sin envío. | Abrir destino en WhatsApp con el dueño, verificar chat; producto comercial. |
| A08 | Validaciones de cantidades/tallas en suite; referencia excesiva y ejemplo oculto rechazados por HTTP. | Recorrido con opciones comerciales en navegador/teléfono. |
| A09 | Contacto directo por WhatsApp desde footer, sin formulario de seguimiento (ADR 010); diseño adjuntado en chat. | Práctica humana de ese recorrido. |
| A10 | Frontend y Admin remoto en 320/390/1440 sin desbordamiento; etiquetas, skip y secuencia de campos/login/logout con teclado. | Teléfono físico, manejo de selector de archivo/errores con teclado y aceptación humana. |
| A11 | Catálogo vacío, ocultación, imagen inválida y fallo simulado de Storage. | Recuperación ante caída real de Storage no ejecutada. |
| A12 | Guía actualizada a Railway; el dueño administrará el panel, confirmado por usuario. | Cuenta personal, capacitación y comprobación de tareas por el dueño. |
| A13 | TLS verify-full, rol limitado, bucket privado, revisión protegida, noindex, healthcheck y plan Hobby. | Consumo representativo/presupuesto (lectura inicial redondeada disponible), respaldo/recuperación, responsables, revocación de clave anterior y autorización de lanzamiento. Dominio predeterminado Railway aprobado; dominio propio aplazado, no bloqueante. |

El producto de ejemplo nuevo está autorizado y delimitado por ADR 005. No demuestra catálogo real ni disponibilidad. Evidencias privadas sin credenciales: .local/railway-prueba y .local/design-review. No se configura dominio/DNS, no se publica comercialmente, no hay commit/push ni instalaciones locales. vibrant-perfection conserva la prohibición expresa de modificación/borrado.

## Panel JYZ — ADR 008

Lista y ficha con identidad de la tienda implementadas. 43 pruebas locales pasan. Revisión visual local en 320/390 px y modos claro/oscuro; A10 continúa parcial porque no hay teléfono físico ni aprobación humana de esta propuesta. Los ejemplos permanecen etiquetados y no se modifican sus datos. Ver presentacion-funcional.md para las acciones antes de abrir el sitio al público.

## Actualización de entrega ADR 017

A01: identidad y galería reales; catálogo diferido por el usuario, pruebas ocultas. A02/A06: cuenta Mryoan y persistencia verificadas HTTPS. A03/A04/A05: función ya probada técnicamente; contenido comercial lo carga el negocio posteriormente. A07/A09: mensaje y destino WhatsApp abiertos en navegador sin enviar; usuario confirmó funcionamiento en teléfono. A10: 320/390 px y confirmación humana del teléfono completados. A11: estado vacío y 404 de ocultos comprobados; caída real de proveedor no simulada como prueba de resiliencia total. A12: acceso/guía entregables listos, práctica por el responsable pendiente de confirmación. A13: autorización/publicación recibida, responsables definidos, dominio Railway aprobado y primera copia/recuperación ejecutada; respaldo recurrente/custodia externa, consumo representativo y revocación anterior siguen sin evidencia. Ver entrega-operativa.md y registro final de estado. No presentar toda la aceptación del negocio como completada por la publicación técnica.

## Confirmación humana de entrega

El usuario confirmó «Lo revisé en el teléfono y funciona» para galería y apertura de WhatsApp, y «Sí, entró y completó la práctica» para acceso Mryoan, ordenar, ocultar y volver a mostrar una foto desde Galería con comprobación pública. La entrega/práctica inicial del panel quedan confirmadas por la persona, además de las pruebas técnicas. No divulgar credenciales. La práctica específica con productos comerciales se realizará al cargar el catálogo, diferido expresamente hasta después de recibir el sitio; no es un bloqueo de esta entrega sin catálogo inicial.

Código/documentación local: .local/entrega-jyz/jyz-codigo-entrega.zip (174 archivos; excluye entornos, .local y credenciales; contenido comparado con las fuentes). El usuario conserva acceso a las cuentas existentes, copia cifrada local y clave separada; no se ha copiado fuera del equipo ni configurado respaldo automático. Custodia externa, rutina de copias y revisión de revocación anterior son obligaciones operativas documentadas, no pruebas realizadas. Sitio funcional entregable en el dominio Railway aprobado.
