# Preparación de solicitudes WhatsApp

Fecha: 8 de octubre de 2026. Estado: cotización integrada y contacto directo desde el footer (ADR 010); apertura real de WhatsApp pendiente. Requisitos R03–R05, A07 parcial.

El número procede del PDF y del código +502 confirmado directamente: 50247233834. `catalogo/solicitudes.py` prepara URLs https://wa.me/50247233834 con el texto codificado. No guarda clientes, pedidos, diseños ni consultas de seguimiento. No envía automáticamente mensajes.

## Cotización

- Selecciona por ID únicamente productos publicados y no marcados como ejemplo.
- Cantidad total entera positiva; cantidades por talla enteras no negativas según opciones del producto. Su suma debe coincidir con el total.
- Campo de colores retirado por instrucción del usuario (ADR 012); detalles del diseño se conversan en WhatsApp.
- Si no hay opciones confirmadas, el mensaje pide consultarlas con JYZ, sin inventar tallas disponibles.
- Reconsulta publicación y tallas durante validación para rechazar un producto ocultado o con opciones modificadas desde la construcción del formulario.
- Incluye instrucciones para adjuntar diseño en el chat y solicitar confirmación de disponibilidad, precio y entrega.

## Seguimiento

Recorrido vigente (ADR 010): enlace directo de WhatsApp en el footer. La referencia se proporciona en el chat, sin formulario de seguimiento en la web. La utilidad anterior y sus pruebas se conservan como historial; ya no se usa en la vista pública.

## Evidencia y pendientes

Siete pruebas nuevas verifican codificación de acentos/ampersand/saltos, destino internacional, validaciones numéricas, distribución por talla, producto oculto/de ejemplo, cambios durante validación y seguimiento. La suite `scripts/local.py runtime-test` pasó **28 pruebas nativas en ese corte** contra PostgreSQL local (21 anteriores y 7 nuevas). Registro local: `.local/solicitudes-test.log`.

Esto demuestra generación y validación local. Falta integrar plantillas tras revisar la primera sección, comprobar mensajes desde navegador y celular, y probar apertura/destino real en WhatsApp sin enviar mensajes automáticamente. A07 no está completo.

## Integración posterior

Tras aprobación visual, cotización y seguimiento integrados en /inicio/. Tres pruebas de integración adicionales llevan la suite a 31; evidencia .local/inicio-tests.log. Seguimiento PRUEBA-ñ1 observado mediante POST en navegador Workers local con mensaje y destino codificados correctamente; captura .local/design-review/seguimiento-workers.jpg. No se abrió ni envió el chat. Cotización comercial completa requiere productos reales confirmados.

## Consulta de posibilidades

Tarjeta «¿Qué puedo personalizar?» disponible sin seleccionar un producto. Mensaje: pregunta por camisetas, hoodies u otra idea y por prendas/materiales/opciones que JYZ puede trabajar. No promete disponibilidad ni guarda solicitudes. ADR 006 registra la instrucción de Marielos recibida por el usuario.

## Cambio del 8 de octubre — ADR 010

El usuario solicita retirar toda la sección «Sigamos en contacto». Se elimina también su formulario y vista previa; navegación «Contacto» apunta al footer, con WhatsApp, logo e Instagram. La evidencia anterior del formulario describe una versión reemplazada.
