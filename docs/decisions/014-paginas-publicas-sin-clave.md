# ADR 014. Páginas públicas sin clave de revisión

Fecha: 8 de octubre de 2026. Aprobado por instrucción directa «Si, procede» tras elegir entre: quitar la clave solo en páginas públicas (recomendado), en todo el sitio o mantenerla.

En Railway la clave de revisión (Basic) se exige solo en `/admin` y `/static/admin/`. Inicio, catálogo, fichas y estáticos públicos quedan abiertos. Se mantienen `X-Robots-Tag: noindex, nofollow`, `Cache-Control: no-store`, rechazo de HTTP sin TLS y el login propio de Django Admin. Reemplaza parcialmente la protección total del paquete de prueba Railway.

Riesgo aceptado: cualquiera con el enlace ve contenido de revisión (aviso, ejemplos, producto de prueba 4 cotizable por WhatsApp, fotos de referencia). No equivale al lanzamiento comercial: dominio/DNS y retiro del contenido de prueba siguen pendientes.

Reemplazo parcial posterior: ADR 020 retira Basic del panel y estáticos Admin por instrucción directa; Django Login y los demás controles se conservan.
