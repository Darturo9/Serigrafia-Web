# ADR 006. Hoodies y consulta de posibilidades

Fecha: 8 de octubre de 2026. Estado: implementado y verificado en la revisión Railway.

El usuario transmite la revisión de Marielos: cambiar gorras por hoodies y añadir una opción para consultar qué podría personalizar el cliente. En el código visible actual no aparece «gorras»; no se alteran los documentos originales para simular un reemplazo. La página usará «hoodies» entre las ideas de prendas y añadirá una tarjeta «¿Qué puedo personalizar?» que abre WhatsApp con una consulta preparada.

La tarjeta funciona con o sin productos, sin obligar a elegir una ficha del catálogo. Pregunta por posibilidades, materiales y opciones, sin prometer disponibilidad, precio ni entrega. Mantiene revisión/envío manual en WhatsApp; no guarda solicitudes, no carga diseños y no añade pedidos ni productos comerciales. El catálogo real sigue pendiente y el ejemplo conserva su identificación. R03/R04/R06, A07/A09 parciales.

Evidencia: 11 pruebas afectadas aprobadas; versión 6c407cf3-7f60-43af-8653-7ad298ded74b SUCCESS. Navegador remoto verifica mensaje, +50247233834 y ausencia de desbordamiento en 320/390/1440. Captura hoodies-y-personalizacion-railway.png y consulta-personalizacion.json dentro de .local. No se abrió ni envió el chat durante la comprobación.
