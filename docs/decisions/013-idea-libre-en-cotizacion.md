# ADR 013. Idea libre en «Cuéntanos tu idea»

Fecha: 8 de octubre de 2026. Aprobado por instrucción directa: agregar un campo donde el cliente escriba su idea y se arme un mensaje formateado para WhatsApp.

La sección de cotización del inicio muestra siempre un formulario de idea libre: nombre, qué personalizar, cantidad aproximada y fecha en que lo necesita (opcionales; fecha no pasada) e idea (obligatoria, máx. 1000 caracteres). Al enviarlo se muestra el mensaje para revisar y el enlace wa.me; no se guarda nada ni se envía automáticamente. Usa negritas de WhatsApp (`*texto*`). La cotización por producto (`?producto=`) se conserva y tiene prioridad. Reemplaza el texto «Elige un producto…» y el botón genérico de esa sección. Sin migraciones, datos, dependencias ni permisos nuevos.
