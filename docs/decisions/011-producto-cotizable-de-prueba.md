# ADR 011. Producto de prueba con cotización habilitada

Fecha: 8 de octubre de 2026. Estado: autorizado por instrucción directa del usuario de crear un producto «real» para probar la ficha en producción.

Se crea una ficha nueva publicada con `es_ejemplo=False` para habilitar el recorrido normal de cotización en el Railway protegido. Es una excepción técnica a ADR 005 para este nuevo registro; no convierte los ejemplos anteriores en productos reales. Nombre, categoría y descripción indican explícitamente que se trata de una prueba sin oferta comercial, porque no se han recibido datos de un producto real.

Nombre: «Playera de prueba · cotización por WhatsApp». Sin precio ni tallas inventadas; solicita confirmación en el chat. Reutilizar referencia de foto existente, atribución de Fallon Michael/Unsplash y portada relacionada, sin nueva descarga/subida ni modificación del objeto. No enviar mensajes ni crear pedidos.

Antes de lanzamiento comercial, ocultar este registro o sustituir su contenido por datos/fotos reales confirmados. Su clasificación técnica de catálogo no demuestra validación comercial. Verificar por HTTPS catálogo, ficha, botón, formulario y mensaje con nombre del producto/destino confirmado. Sin migraciones, cambios de permisos, compras, commit/push ni intervención en vibrant-perfection.
