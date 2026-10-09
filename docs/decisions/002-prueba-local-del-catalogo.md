# ADR 002. Prueba local del catálogo

Estado: verificado localmente por autorización «Muy bien, puedes proceder», después de acordar una prueba local de Django Admin, productos y fotos. No autoriza servicios externos ni publicación.

## Decisión

Crear una base técnica pequeña: Django 5.2 LTS, panel integrado, un modelo Producto y catálogo de verificación. Usar entorno virtual aislado y dependencias fijadas en requirements.txt. Esta prueba no constituye diseño aprobado de la web.

Al inicio Docker estaba detenido y se hizo una comprobación temporal con SQLite. Después el usuario confirmó «Ya levante docker en local». Se creó PostgreSQL 16.14 en un contenedor exclusivo, puerto 127.0.0.1:55439 y volumen propio. La prueba final utiliza esta base mediante el ORM y psycopg. Las fotos siguen en archivos locales dentro de .local; el volumen PostgreSQL no guarda esas fotos. PostgreSQL en Supabase y Storage siguen siendo los destinos propuestos; su compatibilidad y persistencia en Workers permanecen pendientes. La configuración de PostgreSQL es explícita y falla si falta información, sin conectarse automáticamente ni usar credenciales de otros proyectos.

Producto provisional: nombre, descripción, categoría opcional como texto, tallas como lista de cadenas únicas, una foto, texto alternativo, publicación, orden y marca de dato de ejemplo. Una sola foto cubre esta prueba; múltiples fotos y categorías relacionadas se decidirán con el catálogo real.

Imágenes de prueba y panel: JPEG, PNG o WebP válidos, hasta 5 MB y 16 megapíxeles. La validación rechaza imágenes corruptas y conserva la foto existente cuando un reemplazo es inválido. Los archivos no se eliminan automáticamente al reemplazarlos en esta prueba.

El rol de catálogo recibe permisos de consultar, agregar y editar productos, sin administrar usuarios ni borrar productos. Publicar/ocultar se realiza editando el producto. El superusuario es solo para configuración local y no representa el acceso del emprendimiento.

No se construye WhatsApp, galería, pagos, pedidos ni diseño de marca en esta etapa. El catálogo local señala los datos de muestra y bloquea indexación. El servidor debe iniciarse en 127.0.0.1.

## Verificación requerida

Acceso anónimo restringido, rol de catálogo acotado, creación/edición por el panel, carga y reemplazo de foto, rechazo de archivo inválido, publicación/ocultación y persistencia en un segundo proceso local. La prueba remota de arquitectura del ADR 001 continúa pendiente.

Fuentes consultadas: https://docs.djangoproject.com/en/5.2/releases/5.2/ y https://docs.djangoproject.com/en/5.2/ref/contrib/admin/ . Django 5.2 ofrece soporte LTS y compatibilidad con el Python instalado en el entorno virtual. Las versiones efectivamente instaladas se registran en requirements.txt; no prueban compatibilidad con Python Workers.

## Resultado local

10 pruebas pasan contra PostgreSQL: acceso, permisos, alta/edición/ocultación, fotos y validaciones, escape HTML y CSRF. Producto de ejemplo visible con foto; lectura persistente desde un segundo proceso confirmada. Revisión visual en navegador de catálogo y redirección a login completada. No se verificó reinicio del contenedor ni recuperación de respaldo. Python 3.11.16 y Django 5.2.18 en entorno virtual. Supabase y Workers continúan pendientes.
