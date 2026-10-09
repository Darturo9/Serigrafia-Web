# 04. Arquitectura y datos

Estado: Railway verificado técnicamente con Django/Admin/PostgreSQL/fotos y persistencia tras segundo despliegue (ADR 004); lanzamiento comercial pendiente. Los apartados de pruebas Workers posteriores se conservan como historial.

## Componentes

| Componente | Propuesta | Responsabilidad |
|---|---|---|
| Aplicación | Django con plantillas | Renderizar web y gestionar catálogo |
| Interfaz | Bootstrap y JavaScript | Diseño adaptable y preparación de mensajes |
| Administración | Django Admin | Usuarios autorizados y edición de productos |
| Alojamiento | Railway, Django nativo con Gunicorn | Ejecutar Django y servir la web; prueba técnica aprobada |
| Conexión a datos | psycopg al pooler Supabase con TLS verify-full | Conectar Django a PostgreSQL con rol limitado |
| Base de datos | PostgreSQL en Supabase Free | Catálogo, usuarios y datos de funcionamiento de Django |
| Imágenes | Supabase Storage | Conservar fotos independientemente de los despliegues |
| Dominio | Cloudflare Registrar y DNS | Dirección pública y gestión de registros |
| Atención | Enlaces a WhatsApp | Cotización, diseños, confirmación y seguimiento manual |

Usar autenticación de Django para el panel. Supabase Auth no forma parte de la propuesta. No añadir React, servicios separados ni API de pedidos sin necesidad y decisión documentada.

## Flujo

La visita llega al origen HTTPS y Railway ejecutará Django. Django consultará PostgreSQL mediante la conexión definida. El catálogo referencia fotos almacenadas en Storage. El formulario prepara un enlace a WhatsApp. Las operaciones del administrador modifican catálogo y fotos; no crean pedidos. Dominio y publicación siguen pendientes.

## Modelo conceptual

- **Producto:** identificador, nombre, descripción, categoría opcional, estado publicado/oculto y orden de presentación.
- **Opciones del producto:** tallas y opciones reales disponibles, sin cantidades de inventario.
- **Foto:** referencia de archivo en Storage, asociación al producto, descripción y orden si hay varias fotos.
- **Administrador:** usuario de Django con permisos acotados a las operaciones autorizadas.

La base conserva referencias de fotos, no archivos binarios de las imágenes. El esquema exacto, relación de tallas/categorías y manejo de múltiples fotos se definirán durante la especificación de implementación con el catálogo real.

## Prueba de viabilidad obligatoria

Validar Django Admin, autenticación/sesiones, consultas del ORM, guardado, ocultación y foto en Railway con PostgreSQL y Storage de Supabase. Comprobar que producto y foto persisten tras un nuevo despliegue. Definir ejecución de migraciones fuera de peticiones y su autorización antes de aplicarlas a una base externa. No ejecutar migrate automáticamente durante despliegues. Plan vigente: ../plan/prueba-railway.md.

Cloudflare documenta Django y controladores PostgreSQL para Python Workers, pero eso no prueba este proyecto completo. Hyperdrive con Python aparece en documentación con condiciones de compatibilidad; verificar versiones y límites al implementar. No asumir que el despliegue normal de un servidor Django es idéntico a Workers.

## Operación y permisos

Credenciales solo en secretos del servidor. No enviar claves privilegiadas al navegador. Definir permisos de Storage y de cualquier esquema expuesto por Supabase; el catálogo público no autoriza escrituras anónimas. No usar la cuenta propietaria de la base como acceso general sin evaluar los permisos mínimos.

Preparar respaldo de datos y fotos y procedimiento de recuperación. Los respaldos de base de datos no sustituyen copias de archivos. El emprendimiento debe conservar los accesos. Configurar registros sin credenciales ni datos personales innecesarios.

## Costos y límites

Supabase Free: 500 MB de base de datos y 1 GB de archivos según documentación consultada durante la conversación. Contempla pausa por inactividad y no incluye respaldos automáticos. Confirmar condiciones al configurar.

El dominio tiene costo inicial y renovación. Workers y Hyperdrive tienen límites propios; el plan no garantiza alojamiento gratuito ni disponibilidad ininterrumpida. El presupuesto total está pendiente.

## Fuentes técnicas consultadas en esta conversación

- https://developers.cloudflare.com/workers/languages/python/packages/django/
- https://developers.cloudflare.com/hyperdrive/examples/python-workers/
- https://developers.cloudflare.com/workers/platform/pricing/
- https://developers.cloudflare.com/hyperdrive/platform/pricing/
- https://developers.cloudflare.com/registrar/
- https://supabase.com/pricing
- https://supabase.com/docs/guides/database/connecting-to-postgres
- https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

No se fija una versión del framework por la URL de referencia. Verificar y elegir versiones compatibles en la etapa técnica.

## Continuidad de la prueba — 7 de octubre de 2026

Lectura del proyecto Supabase correcto verificada con el nuevo servidor MCP OAuth. PostgreSQL remoto 17.11, sin tablas de aplicación, buckets ni objetos; ver [inspección](../plan/inspeccion-supabase.md). OAuth del MCP no proporciona por sí mismo las credenciales de ejecución de Django/Storage.

El [plan de alojamiento](../plan/prueba-alojamiento.md) concreta el filtro local de Workers y las posteriores pruebas remotas, con esquema/roles, bucket privado y Worker protegido como propuestas pendientes de autorización. La configuración exacta y versiones se fijarán tras pruebas; ADR 001 continúa en validación. No se incorporó Supabase Auth ni se modificó el stack.

## Perfil local validado

ADR 003 registra adaptaciones específicas a Workers: WSGI serializado, PBKDF2 mediante Web Crypto y ruedas de WebAssembly fijadas. Django/ORM/Admin funcionaron contra Docker en 25 comprobaciones HTTP. El backend privado Supabase está preparado y probado con simulaciones; integración y persistencia remotas siguen pendientes. Ver ../plan/evidencia-workers-local.md.

## Evidencia adicional — 8 de octubre de 2026

Supabase autorizado y probado desde Django nativo: 19 migraciones, 11 tablas protegidas con RLS en esquema no expuesto por Data API, bucket privado, carga/lectura PNG/JPEG/WebP y 14 comprobaciones del panel aprobadas. A02–A05 tienen evidencia adicional con datos remotos; A06 solo lectura desde segundo proceso. Workers/Hyperdrive remoto, redespliegue y aceptación final siguen pendientes. Ver [evidencia Supabase](../plan/evidencia-supabase-prueba.md). Suite nativa local actual: 31 pruebas; no confundir con las 25 comprobaciones HTTP Workers previas.

## Fotos optimizadas

ADR 007: nuevas cargas al backend Supabase se convierten a WebP calidad 80, orientación corregida, máximo 1600 px sin ampliar/recortar y hasta 500 KiB mediante reducción proporcional adicional si hace falta. JPEG/PNG/WebP estáticos de entrada conservan límites 5 MiB/16 MP. Transparencia conservada y metadatos eliminados de la copia web. Fotos anteriores/originales no se convierten ni borran automáticamente.

Dominio: el usuario decide conservar por ahora jyz-web-production.up.railway.app; pospone la compra de dominio propio al 9 de octubre o cuando la confirme. Dominio propio no bloquea usar la web funcional en Railway. No comprar ni cambiar DNS.

## Varias fotos por producto — propuesta

Usuario solicita evaluar varias fotos; ADR 009 propone modelo relacionado, portada, orden/estado, inline Admin y ficha con miniaturas. Actualmente Producto mantiene una sola foto; no existe todavía esa función ni migración remota autorizada. Conservar foto/objetos existentes, WebP, permisos acotados y proceso de recuperación.

## Fichas y fotos múltiples (ADR 009)

Ruta `/productos/<id>/` renderizada por Django, con la misma política de publicación/ejemplos que el catálogo. ProductoImagen contiene foto, descripción, orden y activo; Producto.portada referencia una imagen activa del propio producto. Máximo seis fotos activas, edición inline en Admin, sin borrado. La foto antigua se conserva y sus referencias se registran mediante migración de datos sin copiar/eliminar archivos. Permisos de ver/agregar/cambiar imágenes limitados al rol de catálogo. Migración y permisos remotos pendientes de aprobación del paquete probado.

## Galería administrable aprobada — ADR 016

El usuario aprueba administrar fotos de «Ideas que toman forma» desde Django Admin, separadas del catálogo: título/descripción, foto, orden y visible. Backend privado/WebP existente; permisos ver/agregar/cambiar sin borrar. GaleriaImagen y migración 0004 aplicados con autorización en Supabase; carga inicial conserva las tres fotos entregadas. Edición/orden/ocultación verificados por HTTPS en Railway, valores iniciales restaurados y productos/objetos anteriores conservados. Inicio consulta solo visibles; si no hay fotos disponibles omite sección y enlace. A02/A05/A10/A11/A12 requieren edición pública reflejada, permisos negativos y conservación ante fallos; pruebas locales no sustituyen aplicación remota. Ver [paquete y evidencia](../plan/galeria-administrable.md).

## Acceso vigente al panel — ADR 020

El usuario solicita un solo login: HTTP Basic retirado de Admin y sus estáticos; Django mantiene autenticación, sesiones, CSRF, HTTPS, noindex y permisos. Anónimo redirige desde panel/listas al login; login/formulario y estilos accesibles. Mryoan conserva permisos acotados. Verificar login real sin Basic y denegación de usuarios/borrado.
