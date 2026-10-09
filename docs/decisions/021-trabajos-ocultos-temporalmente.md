# ADR 021 — Sección Trabajos oculta temporalmente

Estado: aprobado por instrucción directa del usuario, 8 de octubre de 2026.

El usuario pidió comentar por ahora la sección Trabajos y hacer push al finalizar. Se comenta con etiquetas Django tanto la sección pública como su enlace de navegación: no se emiten imágenes ni contenido oculto en el HTML. Se conservan código, fotos, registros, permisos y administración de galería. Reactivarla requiere retirar esos dos bloques de comentario.

Reemplaza temporalmente la presentación pública de ADR 016; su administración y almacenamiento permanecen vigentes. No requiere migraciones ni cambios de datos. La autorización de commit y push aplica a esta entrega; el repositorio aún no tiene commits, por lo que se registra el estado completo del proyecto en el commit inicial, excluyendo secretos y archivos locales.

Validación: pruebas de galería comprueban que Admin conserva edición, orden y ocultación sin publicar Trabajos; comprobación HTTPS posterior al despliegue exclusivo JYZ. Evidencia final en estado-y-pendientes.md.
