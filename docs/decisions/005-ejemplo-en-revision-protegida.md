# ADR 005. Producto de ejemplo en la revisión protegida

Fecha: 8 de octubre de 2026. Estado: aprobado por instrucción directa; ejecutado y verificado en Railway.

El usuario indicó que el dueño administrará el panel y autorizó crear un producto de prueba, pudiendo usar una imagen Unsplash, porque aún no tiene los productos reales. Se conserva es_ejemplo=True: no se convierte en producto comercial. Solo el perfil Railway protegido muestra ejemplos publicados, con aviso explícito de prueba/no venta y fotografía de referencia. No ofrece cotización para ellos y el servidor sigue rechazando solicitudes de ejemplo. Los perfiles sin ese ajuste conservan el catálogo comercial sin ejemplos.

Se crea únicamente un ejemplo en el esquema/bucket de prueba existentes, sin migraciones, precios ni opciones comerciales inventadas. La fotografía de Fallon Michael muestra prendas en perchas: [fuente](https://unsplash.com/photos/white-dress-shirt-hanging-on-clothes-hanger-e8sbQNYEwX8), [licencia Unsplash](https://unsplash.com/license), consultadas hoy. La foto no es un trabajo de JYZ. Original descargado en .local/catalogo-demo, no se modifican las imágenes del PDF. Catálogo/fotos comerciales y persona que atenderá WhatsApp siguen pendientes.

Resultado: producto 3 visible con foto cargada y sin enlace de cotización; POST directo rechazado. Versión final 9e9c9ff2-9177-4df1-8593-bdee7dda04cf SUCCESS; salud/revisión/configuración conservadas. Navegador remoto sin desbordamiento en 320/390/1440. No acredita catálogo comercial.
