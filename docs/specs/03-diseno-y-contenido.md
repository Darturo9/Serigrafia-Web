# 03. Diseño y contenido

Estado: materiales comerciales recibidos parcialmente; primera sección aprobada con dirección expresiva y urbana. Catálogo real y galería pendientes. Ver `06-materiales-del-comercio.md` para datos, fuente y límites.

## Organización de la página

Propuesta inicial: una página principal con secciones Inicio, Catálogo, Solicitar cotización, Galería y Contacto/Seguimiento. El panel privado tiene acceso separado. Esta organización concreta se validará al revisar la primera sección, antes de ampliar el diseño.

El diseño usa el logo existente y la identidad real del negocio. No hay una paleta ni tipografía comercial aprobada. Los colores de las presentaciones no constituyen identidad de marca.

## Materiales requeridos

| Material | Estado | Uso |
|---|---|---|
| Nombre definitivo y logo original | Pendiente de recibir; Marielos confirma que existe logo | Inicio e identidad |
| Descripción, misión, visión y valores | Pendiente de confirmar | Presentación, según pertinencia del contenido |
| Productos, categorías, tallas y opciones | Pendiente | Catálogo y formulario |
| Fotos de prendas y trabajos | Pendiente, con autorización de uso | Catálogo y galería |
| Número de WhatsApp | Pendiente | Cotización y seguimiento |
| Redes sociales | En creación según Marielos; enlaces pendientes | Contacto |
| Horarios, ubicación y cobertura | Pendiente de confirmar | Solo mostrar si el negocio los proporciona |
| Responsables de catálogo y atención | Pendiente | Capacitación y operación |

## Aprobación visual

1. Recibir identidad y contenido mínimo.
2. Crear la primera sección con datos reales o marcadores claramente identificados para revisión privada.
3. Mostrarla al usuario y aprobar estilo, navegación y organización.
4. Extender el resto manteniendo coherencia visual.

## Reglas

Priorizar lectura en celular, contraste, etiquetas de campos y navegación accesible con teclado. Las imágenes tendrán descripciones útiles. Evitar promociones, precios, testimonios y cifras sin confirmación.

La galería inicial se carga con materiales confirmados. Su edición desde el panel no está incluida como función independiente; si se solicita, documentar la ampliación.

El lanzamiento requiere retirar marcadores, datos de muestra y enlaces provisionales. No prometer sincronización de catálogo con redes sociales.

## Material recibido posteriormente

El PDF JYZ aporta identidad visual, lema, descripción, filosofía, número local de WhatsApp, redes, responsables e imágenes de referencia. La tabla anterior registra los pendientes iniciales; para el estado actualizado prevalece `06-materiales-del-comercio.md`. Faltan catálogo concreto, validación de enlaces, funciones de responsables y confirmación de uso de fotos. El usuario confirmó +502 para WhatsApp; ver especificación 06.

## Recurso preparado para revisión

El 8 de octubre se extrajo directamente el JPEG del logo de la página 3, conservando el original sin redibujar ni eliminar fondo. Recurso en catalogo/static/catalogo/logo-jyz-del-pdf.jpg; procedencia y hash en el README contiguo. La versión independiente/vectorial y la aprobación visual siguen pendientes. Se solicitó preferencia de tono expresivo o sobrio y estilos a evitar.

## Revisión posterior

Primera sección aprobada por el usuario; formularios y restantes secciones integrados. Comprobación local en anchos 320/390/1440 sin desbordamiento horizontal, etiqueta de seguimiento y enlace Saltar al contenido accesible por teclado. No acredita revisión en teléfono físico ni aceptación humana final. Un producto de ejemplo autorizado puede mostrarse únicamente en Railway protegido con identificación explícita (ADR 005).

## Revisión de Marielos recibida por el usuario

Se solicita usar hoodies en lugar de gorras y añadir «¿Qué puedo personalizar?» como consulta independiente del catálogo. La página actual no contenía gorras; se incorpora el término hoodies sin inventar una ficha comercial. Nueva tarjeta abre WhatsApp con pregunta preparada, sin envío automático ni guardado de pedidos. Ver ADR 006.

## Panel JYZ — ADR 008

Personalización autorizada del Django Admin existente: cabecera con logo recibido, naranja/tinta/papel y fuentes locales, miniaturas/estados y campos agrupados. Retirar etiquetas históricas de entorno del encabezado; conservar identificación de datos de ejemplo, seguridad y funciones existentes. Revisión de lista y ficha en navegador; aprobación visual de esta propuesta aún pendiente. Ver ../plan/presentacion-funcional.md para separar presentación privada y lanzamiento público.

## Footer confirmado

Logo recibido y enlace al Instagram _.j.y.z._ autorizado directamente por el usuario. Apertura en pestaña nueva con noopener/noreferrer y texto visible del perfil; conservar Volver arriba y adaptación móvil. Galería todavía necesita fotos de trabajos propios con permiso de publicación y descripción confirmada; su administración independiente no forma parte del panel actual.

## Galería de referencia autorizada

El usuario solicita fotos de prueba de playeras y gorras, de Pexels o fuente similar. Se incorporan tres fotografías de Pexels como galería fija para revisión, cada una marcada Referencia de prueba y con crédito/enlace de origen; aviso explícito de que no son trabajos de JYZ. Gorras se incluyen aquí por esta instrucción, sin reemplazar hoodies en el texto de catálogo aprobado. No se crean productos ni módulo Admin de galería. Para presentación comercial se requieren trabajos propios autorizados o decisión expresa sobre una sección de inspiración; no quitar avisos y convertir estas fotos en supuesto portafolio. Procedencia/licencia/hashes registrados en catalogo/static/catalogo/galeria-referencias/procedencia.json.

## Distribución de catálogo revisada

Usuario aprueba corregir espacio vacío lateral: encabezado centrado, cuadrícula auto-fit con fichas de hasta 360 px y ancho máximo 1240 px; consulta general como franja independiente debajo. Adaptación a cero/uno/varios productos sin inventar fichas para llenar espacio. No se modifica contenido, estado de ejemplo ni enlace WhatsApp. Varias fotos por producto solicitadas como propuesta, no migración aprobada.

## Fotografías reales recibidas — 8 de octubre

El usuario entrega tres fotos en `/Users/danilo/Documents/fotos galeria jyz` y solicita reemplazar referencias por fotos reales. Se preservan originales en `assets/jyz-fotos-recibidas/`; copias WebP en `catalogo/static/catalogo/galeria-jyz/` (719×1600, 719×760 y 899×1177 px; 152408, 69376 y 77788 bytes), sin recorte ni ampliación. Galería sustituye Pexels por las tres prendas fotografiadas, con descripciones visuales sin afirmar técnica, tallas, precio o disponibilidad. Fotos antiguas conservadas.

Dos retoques IA integrados revisados y descartados por reconstruir detalles del diseño; originales optimizados elegidos. Modelo GPT Images 2.5 no seleccionable/verificado. Pendiente aclaración del usuario: solo galería o también fichas cotizables. Producto 4 conserva su identificación de prueba; no se convierten datos sintéticos en reales por recibir fotografías.

Verificación local: inicio 200 y tres recursos resueltos en la base de demo ya migrada; sin Pexels ni avisos de referencia dentro de la galería. La primera comprobación usó una base SQLite antigua sin columna portada; se corrigió el destino a la demo vigente, sin migrar bases remotas. Despliegue limitado a jyz-web/jyz-revision solicitado como sustitución de fotos de la web; resultado HTTPS pendiente. Sin modificaciones PostgreSQL/Storage, migraciones, commit/push, instalaciones ni intervención en vibrant-perfection.

## Galería administrable aprobada — ADR 016

El usuario aprueba administrar fotos de «Ideas que toman forma» desde Django Admin, separadas del catálogo: título/descripción, foto, orden y visible. Backend privado/WebP existente; permisos ver/agregar/cambiar sin borrar. GaleriaImagen y migración 0004 aplicados con autorización en Supabase; carga inicial conserva las tres fotos entregadas. Edición/orden/ocultación verificados por HTTPS en Railway, valores iniciales restaurados y productos/objetos anteriores conservados. Inicio consulta solo visibles; si no hay fotos disponibles omite sección y enlace. A02/A05/A10/A11/A12 requieren edición pública reflejada, permisos negativos y conservación ante fallos; pruebas locales no sustituyen aplicación remota. Ver [paquete y evidencia](../plan/galeria-administrable.md).

## Vista previa al compartir — ADR 018

Solicitud aprobada el 8 de octubre: usar el logo recibido como imagen de enlace en WhatsApp y el dominio comprado jyzgt.com. Metadatos Open Graph renderizados en servidor en inicio/fichas; logo JPEG estático público y URLs absolutas HTTPS. No alterar el logo ni agregar contenido comercial no confirmado. Comprobación técnica y prueba humana de WhatsApp se registran por separado.


## Cambio aprobado — ADR 021

Trabajos y su enlace de navegación quedan comentados temporalmente mediante etiquetas Django. La página pública no debe emitir la sección, su enlace ni las fotos de galería. Galería sigue disponible en Admin y sus archivos/registros se conservan.
