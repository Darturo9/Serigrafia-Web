# ADR 017. Entrega operativa sin catálogo inicial

Fecha: 8 de octubre de 2026. Aprobado directamente: «el catalogo real lo van a usar hasta que le entregue… procede con el resto de cosas y si autorizo todo».

El catálogo comercial lo carga el negocio después de la entrega. La primera presentación usa identidad JYZ, galería real y consultas por WhatsApp. Ocultar todas las fichas sintéticas conocidas, conservando registros, referencias y archivos; estado vacío comprensible y recorrido de ideas disponible. No convertir pruebas en oferta comercial. El catálogo y fichas quedan funcionales para futuras altas del dueño.

Crear Mryoan activo y staff con el grupo existente Responsable de catálogo, nueve permisos de ver/agregar/cambiar productos, imágenes y galería, sin borrar, usuarios ni superusuario. No modificar danilo ni contraseñas existentes. Preparar credencial inicial local privada y guía de cambio de contraseña/capacitación. No asignar una identidad personal a Mryoan sin confirmación.

Autoriza exportación privada de datos/fotos y restauración en PostgreSQL local aislado, sin restaurar sobre Supabase activo. Cifrar el archivo de respaldo, guardar la clave por separado y verificar tablas, hashes, login y renderizado de fotos restaurados. Registrar límites de frecuencia/retención, copias fuera del equipo y prueba humana, sin prometer respaldos automáticos del proveedor.

Autoriza preparar y desplegar la presentación pública en JYZ: retirar aviso de revisión y noindex únicamente de páginas públicas exitosas; conservar Basic y Django Login en Admin, restricciones y protección de rutas técnicas. Reemplaza parcialmente ADR 014 para indexación pública; ADR 015 y las demás restricciones permanecen. No compra planes/dominio ni interviene vibrant-perfection. No se necesita commit/push para esta entrega; quedan fuera del paquete. La revisión técnica móvil no sustituye una prueba humana en teléfono ni capacitación ejecutada por el negocio; se entregan instrucciones y se registran con honestidad.

Reemplazo parcial posterior: ADR 020 retira Basic del panel y estáticos Admin por instrucción directa; Django Login y los demás controles se conservan.
