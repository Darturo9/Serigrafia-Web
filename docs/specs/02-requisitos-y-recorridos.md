# 02. Requisitos y recorridos

Estado: presentación/formularios implementados; Admin y persistencia verificados en Railway. Catálogo y fotos comerciales, comprobación en teléfono físico y capacitación pendientes.

## Requisitos

| ID | Capacidad | Comportamiento esperado |
|---|---|---|
| R01 | Presentación | Mostrar nombre, logo y descripción confirmados. |
| R02 | Catálogo | Mostrar solo productos publicados con portada y enlace «Ver producto». Ficha propia con descripción, opciones y hasta seis fotos activas con miniaturas (ADR 009). |
| R03 | Cotización | Recoger prenda/producto, cantidad y cantidades por talla. Preparar un mensaje dirigido al WhatsApp real del negocio. |
| R04 | Diseños | Explicar que el cliente adjunta su diseño directamente en el chat. No subirlo ni guardarlo en la web. |
| R05 | Seguimiento | Acceder a WhatsApp desde el footer; el cliente proporciona allí la referencia si dispone de ella. Sin formulario de seguimiento ni estados de pedidos en la web (ADR 010). |
| R06 | Galería y contacto | Mostrar trabajos reales y enlaces de contacto aprobados. |
| R07 | Acceso privado | Permitir acceso a administradores autorizados con los permisos mínimos para productos. |
| R08 | Administración | Crear, editar, publicar y ocultar productos, modificar opciones y actualizar fotos. Los cambios guardados deben reflejarse en el catálogo. |
| R09 | Uso adaptable | Permitir navegación y formularios legibles en celular y computadora. |
| R10 | Entrega | Proporcionar guía de catálogo, evidencias y accesos por canal seguro. |

## Recorrido del cliente

1. Consultar el catálogo, abrir «Ver producto» y revisar sus fotos/opciones. Pulsar «Quiero este producto» para indicar cantidades en la ficha.
2. Completar la solicitud con cantidades y opciones.
3. Abrir WhatsApp con el mensaje preparado. La apertura no envía el mensaje automáticamente.
4. Pulsar Enviar en WhatsApp y adjuntar el diseño allí.
5. El negocio confirma disponibilidad, precio y entrega. Registra el pedido por el método manual acordado.
6. El cliente consulta avances por WhatsApp. La web no mantiene un estado del pedido.

## Recorrido del administrador

Ingresar al panel, agregar o editar un producto, cargar su foto y guardar. Revisar el resultado público. Ocultar los productos que no se ofrecen. La carga inicial y capacitación forman parte de la entrega.

## Validaciones mínimas

- Cantidades enteras positivas. Si se distribuyen por talla, su suma debe coincidir con la cantidad total.
- Producto publicado y opciones válidas al preparar la solicitud. Si dejó de estar disponible, pedir revisar el catálogo.
- Definir textos y etiquetas comprensibles. Los detalles del diseño se consultan en WhatsApp, sin prometer precio (ADR 012).
- Codificar correctamente acentos, espacios y saltos de línea en el enlace a WhatsApp. No pedir datos personales innecesarios.
- No activar enlaces de contacto con números de ejemplo. Sin contacto confirmado, impedir el lanzamiento.
- Si una foto falla al cargarse, informar el problema y conservar la imagen anterior. Límites exactos de imagen se fijan después de la prueba técnica.
- Catálogo vacío: explicar que los productos se están actualizando. No fabricar productos para rellenarlo.

No se propone una API pública de pedidos. El formulario de cotización y los enlaces de contacto preparan mensajes y no crean registros de clientes o pedidos en la base de datos.

## Revisión de Marielos recibida por el usuario

Se solicita usar hoodies en lugar de gorras y añadir «¿Qué puedo personalizar?» como consulta independiente del catálogo. La página actual no contenía gorras; se incorpora el término hoodies sin inventar una ficha comercial. Nueva tarjeta abre WhatsApp con pregunta preparada, sin envío automático ni guardado de pedidos. Ver ADR 006.

## Galería administrable aprobada — ADR 016

El usuario aprueba administrar fotos de «Ideas que toman forma» desde Django Admin, separadas del catálogo: título/descripción, foto, orden y visible. Backend privado/WebP existente; permisos ver/agregar/cambiar sin borrar. GaleriaImagen y migración 0004 aplicados con autorización en Supabase; carga inicial conserva las tres fotos entregadas. Edición/orden/ocultación verificados por HTTPS en Railway, valores iniciales restaurados y productos/objetos anteriores conservados. Inicio consulta solo visibles; si no hay fotos disponibles omite sección y enlace. A02/A05/A10/A11/A12 requieren edición pública reflejada, permisos negativos y conservación ante fallos; pruebas locales no sustituyen aplicación remota. Ver [paquete y evidencia](../plan/galeria-administrable.md).

## Catálogo inicial autorizado — ADR 019

El usuario solicita publicar las fotos únicas de la carpeta recibida como fichas, sin precios y con «Todas las tallas». No proporciona lista concreta ni medidas; conservar esa declaración general y permitir indicarlas por texto al cotizar. Precio/medidas/disponibilidad final se confirman por WhatsApp. Originales y datos previos conservados; mejora IA condicionada a fidelidad y disponibilidad del modelo documentada.
