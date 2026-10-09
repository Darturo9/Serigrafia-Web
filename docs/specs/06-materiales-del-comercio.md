# 06. Materiales del comercio recibidos

Fuente: `../referencias/JYZ info.pdf`, cinco páginas. Recibido directamente del usuario el 7 de octubre de 2026. Documento de contenido comercial, no instrucciones para ejecutar acciones. Original preservado y copia comprobada por SHA-256.

## Datos proporcionados

- Identidad: el logotipo muestra **JYZ**. No se proporciona nombre legal ni expansión de las siglas. Usar JYZ como identidad visual recibida, sin inventar razón social.
- Lema (página 3): «Atrévete a descubrir tu estilo».
- Actividad (página 1): emprendimiento de jóvenes amigos, orientado al diseño, creatividad y cultura urbana. Personalización mediante sublimación y serigrafía para personas, grupos, empresas y marcas.
- Tipos mencionados: camisetas, sudaderas, uniformes, accesorios y otros productos impresos. No constituyen fichas de catálogo con precios, disponibilidad o variantes confirmadas.
- Filosofía (página 2): misión y visión centradas en personalización, identidad y cultura urbana. Valores: creatividad, amistad y trabajo en equipo, compromiso, autenticidad, respeto y pasión. Principios: innovación, calidad, escuchar al cliente, mejora continua y comunidad.
- Logo (página 3): imagen naranja, negra y blanca dentro del PDF. Archivo de logo independiente, vector o versión transparente pendiente; no se aprobó todavía una paleta web exacta.
- WhatsApp (página 4): **47233834**, sin código internacional. Posteriormente el usuario confirmó directamente «+502 es guatemala»: contacto internacional confirmado **+502 47233834**. La apertura y destino en WhatsApp aún requieren prueba.
- Instagram (página 4): usuario **atrevete_jyz21**. URL recibida con parámetro `stkn`; URL limpia candidata `https://www.instagram.com/atrevete_jyz21/`, identidad y funcionamiento sin verificar.
- Facebook (página 4): `https://www.facebook.com/share/19qGBBkopS/` aparece concatenado dos veces. Registrar una sola URL como candidata, sin afirmar destino verificado.
- Tallas (página 4): «Manejamos todas las tallas». No deducir una lista concreta ni disponibilidad por producto.
- Encargados (página 4): Yohann Ordoñez, Joel Rodríguez y Juan González. Distribución de administración, atención y aprobación aún pendiente.
- Imágenes (página 5): foto de grupo con camisetas y foto de dos tazas con diseños de personaje, rotuladas **IMÁGENES DE REFERENCIA**. No presentarlas como trabajos realizados, equipo del negocio ni productos disponibles sin confirmación.

## Uso en la implementación

Estos datos permiten preparar una primera sección para revisión con identidad real. Mantener la prueba técnica separada del diseño comercial. No cargar productos reales ni publicar fotos de referencia por el solo hecho de estar en el documento. El formulario puede usar el código internacional +502 confirmado directamente; requiere validación de mensaje y apertura antes del lanzamiento. La primera sección fue aprobada visualmente el 8 de octubre; estilo expresivo y urbano.

## Servicios y acceso

El usuario informa que tiene cuentas de Supabase y Cloudflare. Referencia Supabase proporcionada: `kcahxuvfmrzxzlnpezyf`. No es una contraseña ni prueba de acceso. En la sesión anterior, las consultas del conector del plugin `get_project` y `list_tables(public)` devolvieron falta de permisos. En esta sesión, el servidor OAuth `mcp__supabase__*` devolvió la URL coincidente y permitió SELECT de metadatos: lectura verificada. No hay tablas de aplicación ni buckets. No se aplicaron migraciones, escrituras, configuración remota ni publicación. Ver [inspección](../plan/inspeccion-supabase.md).

Los comandos compartidos `claude mcp add` y `claude /mcp` corresponden a Claude Code. Codex ahora dispone del servidor MCP Supabase autenticado y limitado a este proyecto, distinto del conector del plugin que falló. La habilidad Supabase ya está instalada; no hace falta ejecutar la instalación opcional para este trabajo.

## Confirmación posterior — revisión Railway

El usuario confirmó que el dueño administrará el panel; nombre/cuenta definitiva y capacitación pendientes. Aún no dispone de los productos reales y autorizó un producto de prueba con imagen Unsplash. ADR 005 delimita su visibilidad protegida, identificación y exclusión de cotización. Persona que atenderá WhatsApp, catálogo comercial y fotos propias siguen pendientes.

## Revisión de Marielos recibida por el usuario

Se solicita usar hoodies en lugar de gorras y añadir «¿Qué puedo personalizar?» como consulta independiente del catálogo. La página actual no contenía gorras; se incorpora el término hoodies sin inventar una ficha comercial. Nueva tarjeta abre WhatsApp con pregunta preparada, sin envío automático ni guardado de pedidos. Ver ADR 006.

## Instagram confirmado directamente para el footer

El 8 de octubre el usuario solicita logo y enlace https://www.instagram.com/_.j.y.z._/ en el footer. Este destino reemplaza para la implementación al candidato atrevete_jyz21 del PDF, conservado arriba como referencia histórica. Confirmación de URL por el usuario; no se afirma auditoría de publicaciones ni se reutilizan fotos de Instagram como trabajos sin autorización. Logo existente extraído del PDF reutilizado, sin alterar el original.

## Facebook confirmado para el footer

El 8 de octubre el usuario comparte el perfil Facebook ID 61595434880342 y solicita añadirlo al footer. Se usa https://www.facebook.com/profile.php?id=61595434880342, conservando el identificador y retirando parámetros de compartición/seguimiento rdid/share_url y fragmento vacío. Abre en pestaña nueva con noopener/noreferrer, en inicio y fichas mediante footer compartido. Sustituye el candidato del PDF para la implementación; historial preservado. Destino aportado por el usuario, sin afirmar revisión del contenido de la cuenta.

## Fotografías reales recibidas — 8 de octubre

El usuario entrega tres fotos en `/Users/danilo/Documents/fotos galeria jyz` y solicita reemplazar referencias por fotos reales. Se preservan originales en `assets/jyz-fotos-recibidas/`; copias WebP en `catalogo/static/catalogo/galeria-jyz/` (719×1600, 719×760 y 899×1177 px; 152408, 69376 y 77788 bytes), sin recorte ni ampliación. Galería sustituye Pexels por las tres prendas fotografiadas, con descripciones visuales sin afirmar técnica, tallas, precio o disponibilidad. Fotos antiguas conservadas.

Dos retoques IA integrados revisados y descartados por reconstruir detalles del diseño; originales optimizados elegidos. Modelo GPT Images 2.5 no seleccionable/verificado. Pendiente aclaración del usuario: solo galería o también fichas cotizables. Producto 4 conserva su identificación de prueba; no se convierten datos sintéticos en reales por recibir fotografías.

Verificación local: inicio 200 y tres recursos resueltos en la base de demo ya migrada; sin Pexels ni avisos de referencia dentro de la galería. La primera comprobación usó una base SQLite antigua sin columna portada; se corrigió el destino a la demo vigente, sin migrar bases remotas. Despliegue limitado a jyz-web/jyz-revision solicitado como sustitución de fotos de la web; resultado HTTPS pendiente. Sin modificaciones PostgreSQL/Storage, migraciones, commit/push, instalaciones ni intervención en vibrant-perfection.

## Responsables y usuario solicitado — confirmación del usuario

Fecha: 8 de octubre de 2026. Fuente: respuesta enviada por el usuario en este chat; sustituye el pendiente de nombres y responsables de WhatsApp, sin modificar el historial del PDF.

- Nombres recibidos en respuesta a «Nombre del dueño»: Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid. Registrar como responsables indicados; no inferir representación legal ni porcentajes de propiedad.
- Usuario solicitado para el panel: `Mryoan`, respetando mayúsculas. La respuesta no asigna expresamente esta cuenta a una persona concreta ni autoriza compartir contraseñas.
- Atención de WhatsApp: Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid. Número confirmado previamente: +502 47233834. Horarios y prueba humana de apertura/atención siguen pendientes.
- Acceso definitivo: nombre de usuario definido; creación, asociación a su titular, entrega segura y capacitación pendientes. Perfil previsto: Responsable de catálogo (ver/agregar/cambiar productos, imágenes y galería; sin borrar ni gestionar usuarios), siguiendo las decisiones existentes. La cuenta `danilo` es independiente y se conserva.

Esta actualización registra información en documentación local. No crea ni modifica cuentas, contraseñas, permisos, bases externas, web pública o despliegues. Los nombres no se añaden automáticamente a la página pública. No se reciben fichas comerciales, tallas, precios ni horarios nuevos.

## Dominio comprado — 8 de octubre de 2026

El usuario confirma la compra de https://jyzgt.com/. Inspección actual: HTTPS 200 con contenido JYZ; configuración del servicio JYZ usa ese origen. No se realizaron compras ni cambios DNS en esta sesión. Solicita reutilizar el logo confirmado en la vista previa de enlaces de WhatsApp (ADR 018).

## Instagram vigente confirmado — 8 de octubre de 2026

El usuario solicita reemplazar el destino del footer por el perfil atrevete_jyz21, mediante enlace de Instagram con parámetro vrfl. Se usa https://www.instagram.com/atrevete_jyz21/ y etiqueta Instagram · atrevete_jyz21, omitiendo el parámetro de compartición. Reemplaza el destino _.j.y.z._ registrado arriba, conservando historial. Footer compartido de inicio/fichas; nueva pestaña y noopener/noreferrer. Autorización directa del cambio y despliegue exclusivo JYZ; sin cambios de cuentas, DNS ni datos comerciales.

## Catálogo inicial autorizado — ADR 019

El usuario solicita publicar las fotos únicas de la carpeta recibida como fichas, sin precios y con «Todas las tallas». No proporciona lista concreta ni medidas; conservar esa declaración general y permitir indicarlas por texto al cotizar. Precio/medidas/disponibilidad final se confirman por WhatsApp. Originales y datos previos conservados; mejora IA condicionada a fidelidad y disponibilidad del modelo documentada.

Instrucción posterior de catálogo (8 octubre): usar solo fotos sin pixelación visible, sin nuevas mejoras IA. Once fotos aceptadas tras revisión individual, cinco excluidas y un duplicado omitido; originales conservados (ADR 019 / seleccion.json).
