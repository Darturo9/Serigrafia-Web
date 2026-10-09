# ADR 009. Varias fotos por producto

Fecha: 8 de octubre de 2026. Estado: implementación local aprobada por «Me parece perfecto, procede», tras presentar ficha, miniaturas y botón «Quiero este producto». Paquete concreto de dos migraciones, permisos de fotos y despliegue protegido autorizado directamente por «autorizo» el 8 de octubre de 2026.

## Experiencia propuesta

En catálogo mostrar una sola portada, para mantener la lista limpia. La instrucción posterior aprueba «Ver producto» para abrir una ficha del producto con foto principal y miniaturas seleccionables. Mostrar descripción/opciones y la acción de cotizar al mismo WhatsApp existente. Si solo hay una foto, no mostrar controles sobrantes. En celular, miniaturas desplazables; teclado, etiquetas, foco y descripción útil. No reproducción automática ni carrusel que cambie sin intervención.

Primera propuesta: máximo seis imágenes activas por producto, conservando las desactivadas. Cada foto sigue conversión WebP/límites de entrada; carga diferida y sin descargar todas las originales en la lista. Las fotos están en Storage privado; generar URLs firmadas al cargar la ficha, contemplar expiración/fallo sin romper acceso al resto de la información. No fotos/diseños del cliente ni pedidos en la web.

## Administración y datos

Añadir modelo relacionado ProductoImagen con archivo, descripción, orden y estado activo. Definir portada mediante referencia del producto a una imagen activa del mismo producto; validar esa pertenencia y el límite/orden del conjunto. Evitar elegir dos portadas. Editar fotos dentro de la ficha de producto del Django Admin, mediante inline, sin panel nuevo ni API separada. Otorgar únicamente los permisos necesarios de foto al grupo Responsable de catálogo después de aprobación específica.

La foto actual de Producto se conserva mientras se migra y como respaldo compatible. Una migración de datos futura registraría las referencias existentes como imágenes relacionadas sin copiar/sobrescribir/borrar objetos Storage. Preparar y probar primero en base local; cualquier aplicación en Supabase requiere autorización explícita. No eliminar el campo viejo hasta verificar compatibilidad y recuperación, mediante decisión separada.

Retirar una foto de la presentación significa desactivarla; eliminación física de archivos es procedimiento separado. Un reemplazo fallido conserva referencias válidas. La transacción PostgreSQL no revierte automáticamente subidas a Storage: registrar/gestionar objetos huérfanos mediante un procedimiento autorizado, sin limpieza destructiva automática.

## Evidencia requerida antes de entregar

Probar 0/1/6 imágenes, límite excedido, permisos de añadir/editar/reactivar, selección de portada válida, orden, WebP y fallo en carga múltiple sin perder anteriores. Conservar la foto actual y sus hashes después de migración local. Revisar ficha/miniaturas en computadora, celular y teclado; verificar el ámbito del producto en rutas/consultas y URLs privadas. Solo ejecutar migración remota/ajuste de permisos tras presentar paquete concreto y recibir autorización. Paquete autorizado y aplicado: dos migraciones, seis permisos de catálogo y despliegue fbda1822-3da5-4f22-b1a7-827aa344600a verificados; ver docs/plan/fichas-y-fotos-multiples.md.

Relacionado con R02/R07/R08/R09, A03/A05/A06/A10/A11/A12. No modifica vibrant-perfection ni requiere nuevos servicios.
