# ADR 020. Panel con un solo inicio de sesión

Fecha: 8 de octubre de 2026. Aprobación directa: «quita la primera proteccion del panel». Retirar el desafío HTTP Basic de /admin y /static/admin/ en Railway. Django Admin conserva login/sesiones, CSRF, HTTPS, cookies seguras, noindex/no-store y permisos existentes. /catalogo/ es ruta técnica ajena al acceso del panel y conserva protección previa. No cambiar cuentas, contraseñas ni permisos.

Sustituye parcialmente ADR 014/017 para la capa Basic del panel, sin modificar el resto. Autorización directa para código y despliegue exclusivo JYZ, sin migraciones, datos comerciales, compras, instalaciones, DNS, commit/push ni cambios en vibrant-perfection.

Aceptación: /admin/login/ 200 anónimo y sin WWW-Authenticate; /admin/ y productos redirigen al login sin sesión. Login Mryoan sin Basic funciona; lista/galería 200, usuarios/borrado 403, CSRF sin token rechazado, estáticos Admin públicos 200. Verificar por HTTPS y actualizar guía de acceso.
