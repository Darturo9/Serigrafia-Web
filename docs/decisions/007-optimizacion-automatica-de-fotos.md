# ADR 007. Optimización automática de fotos

Fecha: 8 de octubre de 2026. Estado: autorizada por «Si procede» tras la propuesta; implementada y verificada localmente y en Railway.

Al guardar una foto en el backend Supabase, validar JPEG/PNG/WebP estáticos con los límites actuales de entrada (5 MiB y 16 megapíxeles), corregir orientación EXIF, reducir proporcionalmente sin ampliar ni recortar a un máximo de 1600 px y convertir a WebP con calidad 80. Conservar transparencia y eliminar metadatos de la copia web. No aceptar animaciones como fotos estáticas de forma silenciosa.

Límite de salida: 500 KiB. Si calidad 80/1600 px todavía excede ese tamaño, reducir dimensiones progresivamente conservando proporción y calidad; si no se obtiene una salida válida, rechazar antes de subir. El panel explica la optimización automática. El cambio no requiere que el dueño convierta imágenes manualmente ni instalaciones locales adicionales.

Guardar únicamente la nueva copia optimizada en una ruta UUID .webp privada. No sobreescribir ni borrar fotos existentes; una conversión o carga fallida revierte la edición y conserva la referencia anterior mediante la transacción actual del Admin. Fotos ya guardadas mantienen su formato; no se convierte todo el bucket ni se altera el original del PDF. Prueba remota limitada al producto de ejemplo autorizado, conservando el original local. Sin migraciones, nuevos servicios, commit/push ni cambios en vibrant-perfection.

R08/R09, A05/A11 parciales: pruebas deben verificar formato/dimensiones/orientación/transparencia/peso, rechazo previo a HTTP y conservación de referencia ante fallo. La copia web puede tener pérdida de calidad; conservar originales fuera del sitio para impresión.

## Evidencia ejecutada

43 pruebas locales aprobadas. Despliegue Railway 9a8d78bc-2b1a-4e75-b31a-949c6b31503e SUCCESS. Carga por HTTPS en Django Admin, limitada al producto de ejemplo 3: JPEG original de 399222 bytes convertido a WebP de 49098 bytes, 1600 × 1067 px, sin EXIF; reducción de 87,7 % para esta imagen. Lectura privada y URL firmada verificadas con MIME image/webp. Objeto anterior conservado; reemplazo inválido mantiene la foto válida. Evidencia local sin credenciales: .local/railway-prueba/webp-http.json y deployment-webp.json. No se realizó una conversión masiva ni una nueva revisión visual del navegador para esta versión.
