# Revisión para uso por clientes y dueño

Fecha: 8 de octubre de 2026. Inspección actual de código/documentación, HTTP y navegador remoto. No modifica configuración, productos, permisos ni recursos. El enlace de Facebook solicitado previamente ya está presente en el footer compartido.

## Verificado ahora

- Raíz e /inicio/ muestran el inicio; fichas públicas responden sin clave. Catálogo técnico y Admin mantienen Basic. La afirmación anterior de que toda la web necesitaba clave quedó reemplazada por ADR 014/015.
- Navegador de escritorio: imágenes cargadas y sin desbordamiento horizontal. A 390 px: inicio y ficha sin desbordamiento; no sustituye un teléfono real.
- Idea libre prepara mensaje con texto/destino al +50247233834; ficha 4 prepara producto/cantidad/opciones por consultar. No se abre/envía WhatsApp ni se guardan pedidos.
- Facebook apunta al ID 61595434880342, Instagram al perfil confirmado y WhatsApp al número confirmado. No se verificó la identidad/contenido de las redes con el dueño ni el chat real.
- La página contiene aviso de revisión y noindex. Catálogo visible incluye producto 4 «Playera de prueba · cotización por WhatsApp», explícitamente sin oferta comercial; galería contiene tres referencias Pexels. No es catálogo/portafolio real.
- Última versión consultada Railway bb8a8e82-70aa-47cd-a02f-fdb39cd84984 SUCCESS; el código también incluye idea libre, fecha opcional, raíz corregida e iconos SVG. La revisión se basa en ese estado, no en una versión anterior de la conversación.

## Pendientes por prioridad

1. **Contenido de lanzamiento (A01/R02/R06).** Sustituir el producto de prueba por fichas/fotos/tallas reales confirmadas, u ocultarlo y lanzar solo consulta de personalización. La galería debe usar trabajos propios autorizados o retirarse temporalmente. Conservar originales/registro de prueba; no convertir imágenes de referencia en trabajos reales.
2. **Presentación final.** Retirar aviso «Vista de revisión» al aprobar contenido. Revisar textos finales con el negocio. noindex puede conservarse si solo se comparte el enlace; cambiarlo al aprobar presencia en buscadores. No hace falta dominio propio para usar Railway.
3. **Prueba humana del recorrido (A07/A10).** Desde teléfono físico abrir WhatsApp, confirmar chat del negocio y texto, regresar al sitio, probar idea y producto real. Validar redes con el dueño. Pruebas HTTP/formato del enlace no demuestran apertura/identidad del chat.
4. **Operación del dueño (A12).** Acceso definitivo por canal seguro y práctica de agregar/editar foto/ocultar producto; definir quién responderá WhatsApp. La cuenta danilo y la guía no prueban capacitación del dueño.
5. **Continuidad (A13).** Acordar responsable/destino/frecuencia de respaldos de PostgreSQL y Storage, y ejecutar restauración aislada autorizada. El plan existe, pero no hay evidencia de restauración. Confirmar revocación de clave anterior; código aún sin commit/push autorizado.

## Mejoras que pueden esperar

Dominio propio, SEO social (descripción/imagen al compartir), métricas de visitas. No son necesarias para empezar a recibir consultas. Pagos, carrito, inventario y pedidos guardados siguen fuera de alcance.

## Resultado

Ya puede compartirse y probarse con clientes mediante el enlace Railway, sin clave pública. La funcionalidad principal está operativa; no se considera presentación comercial terminada mientras conserve contenido de prueba. Recomendación: cerrar contenido y validación humana antes de promoción. Sin nueva publicación/configuración/despliegue durante esta auditoría.

Evidencia: .local/railway-prueba/auditoria-lanzamiento-http.json y auditoria-acceso-anonimo.json; capturas footer-facebook-remoto.png y auditoria-whatsapp-movil.png. Capturas de navegador remoto. Esta revisión no certifica WCAG, rendimiento bajo carga, recuperación ni todos los navegadores físicos.

## Actualización: fotos recibidas después de esta auditoría

El usuario entregó tres fotografías propias para sustituir la galería de referencia. Se incorporan copias WebP de los originales, preservados en assets/jyz-fotos-recibidas. El pendiente de fotos de la galería se reduce a aceptación visual; catálogo/fichas cotizables y sus opciones siguen por confirmar. Consultar la entrada «Fotografías reales recibidas» en estado y tareas para el resultado del despliegue.

Actualización ADR 016: galería administrable aplicada y verificada en Railway/Supabase. Ya no está pendiente la edición independiente de fotos, textos, orden y visibilidad; capacitación y aceptación humana siguen pendientes. Resultado completo en galeria-administrable.md.
