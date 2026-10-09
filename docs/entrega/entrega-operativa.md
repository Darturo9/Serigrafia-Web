# Entrega operativa JYZ

Fecha: 8 de octubre de 2026. ADR 017. Catálogo comercial lo cargará el negocio después de la entrega, según instrucción del usuario. Sitio: https://jyz-web-production.up.railway.app/ . Admin: https://jyz-web-production.up.railway.app/admin/ . No necesita comprar dominio para usar esta versión.

## Qué recibe el negocio

- Inicio, galería con las tres fotos recibidas, contactos y formulario de idea que prepara una consulta por WhatsApp. Sin carrito, pagos, inventario ni pedidos almacenados.
- Panel para productos, fotos múltiples y galería. Nuevas fotos JPEG/PNG/WebP se convierten automáticamente a WebP, máximo 1600 px y 500 KB; entrada hasta 5 MB/16 megapíxeles. Conservar originales para impresión.
- Cuenta Mryoan, activa y staff, sin superusuario ni borrado/gestión de usuarios. Nueve permisos de catálogo, imágenes y galería. Cuenta danilo independiente conservada.
- Cuatro fichas sintéticas ocultas, sin borrar datos/fotos. La página explica que se prepara el catálogo y permite consultas. Fotos reales de galería no se convierten automáticamente en fichas comerciales.
- Copia cifrada y recuperación comprobada en PostgreSQL local aislado. Código y documentación entregables en archivo local, sin credenciales ni entornos.

## Acceso inicial privado

Archivo local restringido: `/Users/danilo/Documents/Serigrafia-Web/.local/entrega-jyz/acceso-mryoan.txt`. Conserva el acceso inicial histórico. Desde ADR 020, el panel solo usa la cuenta Django Mryoan; ignore la sección Basic anterior. No contiene las claves de Supabase/PostgreSQL. Danilo debe entregarlo al responsable por un canal privado; no está enviado a otras personas ni publicado.

Al entrar, use «Cambiar contraseña» (/admin/password_change/) para elegir una contraseña propia. No pegarlas en chats públicos ni capturas. El archivo conserva la contraseña inicial y no se actualiza cuando el dueño la cambia. No hay recuperación por correo configurada. Para restablecer acceso, el responsable técnico debe verificar identidad y gestionar la cuenta, manteniendo permisos acotados.

Los nombres recibidos son Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid. Los tres fueron indicados para atender WhatsApp. Aún no se asigna Mryoan a uno de ellos de manera individual; el negocio debe conservar la contraseña con el administrador que designe y evitar compartirla indiscriminadamente.

## Práctica breve del administrador

Consultar [guía completa](guia-de-catalogo.md). Con su acceso:

1. Entrar y abrir Productos → Agregar. Escribir datos reales, foto y opciones confirmadas; guardar primero oculto.
2. Abrirlo, corregir información y revisar la vista previa de la foto. No reutilizar una ficha sintética cambiando solamente la marca de ejemplo.
3. Publicar y comprobarlo desde la web pública. Abrir «Ver producto» y «Quiero este producto»; revisar el mensaje preparado sin enviarlo durante la práctica.
4. Ocultar y comprobar que ficha y listado dejan de ser accesibles; publicar de nuevo solo si está aprobado como oferta real.
5. En Galería, editar título/descripción, cambiar orden y mostrar/ocultar. Guardar y comprobar el inicio. Ocultar todas las fotos retira sección y enlace Trabajos.
6. Cerrar sesión. Registrar responsable, fecha y resultado sin contraseñas.

La creación/login de Mryoan y los permisos están probados técnicamente. El usuario confirmó la práctica de galería (entrar, ordenar, ocultar y mostrar); el ejercicio con productos reales queda para cuando carguen el catálogo.

## Uso por el cliente

«Cuéntanos tu idea» prepara una vista previa; el botón abre WhatsApp al +502 47233834. El cliente adjunta su diseño allí y decide cuándo enviar. Precio, opciones y entrega se acuerdan con el negocio. La página no envía mensajes ni guarda solicitudes o clientes. El 8 de octubre el enlace abrió el destino correcto con perfil visible «Juan Gonzalez»; no se envió mensaje. Esa observación confirma el destino del enlace, no entrega de mensajes ni disponibilidad de atención.

## Verificación y límites

65 pruebas locales aprobadas; comprobación real HTTPS de publicación, catálogo vacío, fichas ocultas, galería, CSRF, mensaje, login Mryoan, permisos y cambio de contraseña disponible. Navegador: 390/320 px sin desbordamiento, tres fotos cargadas, formulario y apertura de WhatsApp. El usuario confirmó «Lo revisé en el teléfono y funciona» para galería y apertura WhatsApp; práctica de galería con Mryoan confirmada por el usuario.

Las páginas públicas GET/HEAD exitosas ya permiten indexación y no tienen aviso de revisión. Admin/rutas técnicas, errores y POST con mensajes permanecen noindex/no-store; Admin mantiene únicamente login Django (ADR 020). robots.txt y sitemap.xml publicados; no se garantiza cuándo indexarán los buscadores.

Datos, fotos y accesos remotos siguen en las cuentas existentes. No cambió la titularidad de Railway/Supabase y no se transfirieron a una cuenta nueva. La prohibición de intervenir vibrant-perfection permanece.

## Respaldo y continuidad

Ver [procedimiento y evidencia](respaldo-y-recuperacion.md). Archivo cifrado fuera del repositorio: `/Users/danilo/Documents/JYZ-respaldos/2026-10-08/jyz-respaldo.tar.enc`, acompañado por HMAC. Clave separada, privada en `.local/entrega-jyz/clave-respaldo`. Conservar clave y copia por canales distintos; sin clave no podrá descifrarse. No publicar ni subir el contenido sin cifrar.

Esta es una copia manual verificada. No está programado un respaldo automático. Antes de cambios técnicos y al terminar jornadas con cambios de catálogo, el responsable técnico debe generar otra copia y verificarla; conservar las últimas siete como procedimiento inicial, sin borrar las existentes por este documento. El negocio debe mantener además una copia cifrada fuera de este equipo y designar quién la custodia. No asumir que el plan del proveedor incluye los archivos Storage ni prometer pérdida cero.

## Confirmación humana de entrega

El usuario confirmó «Lo revisé en el teléfono y funciona» para galería y apertura de WhatsApp, y «Sí, entró y completó la práctica» para acceso Mryoan, ordenar, ocultar y volver a mostrar una foto desde Galería con comprobación pública. La entrega/práctica inicial del panel quedan confirmadas por la persona, además de las pruebas técnicas. No divulgar credenciales. La práctica específica con productos comerciales se realizará al cargar el catálogo, diferido expresamente hasta después de recibir el sitio; no es un bloqueo de esta entrega sin catálogo inicial.

Código/documentación local: .local/entrega-jyz/jyz-codigo-entrega.zip (174 archivos; excluye entornos, .local y credenciales; contenido comparado con las fuentes). El usuario conserva acceso a las cuentas existentes, copia cifrada local y clave separada; no se ha copiado fuera del equipo ni configurado respaldo automático. Custodia externa, rutina de copias y revisión de revocación anterior son obligaciones operativas documentadas, no pruebas realizadas. Sitio funcional entregable en el dominio Railway aprobado.


## Guía visual del negocio

[Presentación editable JYZ — guía de uso](presentacion/JYZ-guia-de-uso.pptx): 17 diapositivas para explicar acceso al panel, productos, fotos, galería, atención por WhatsApp y continuidad. No contiene contraseñas ni claves. Las capturas de productos con datos sintéticos son demostraciones identificadas; no representan ofertas comerciales. El negocio puede utilizarla en su capacitación y consultar las notas de cada diapositiva para detalles de alcance.

## Actualización de catálogo y dominio — ADR 019

Sitio/Admin vigentes: https://jyzgt.com/ y https://jyzgt.com/admin/. Once fichas nuevas publicadas de la carpeta recibida, con fotos nítidas seleccionadas, sin precios y con todas las tallas generales; cinco pixeladas y duplicado excluidos. Los ejemplos permanecen ocultos. Mryoan y protección Basic existentes probados por HTTPS. El usuario solicita credenciales por chat en esta entrega; no se cambian contraseñas ni permisos. No afirmar capacitación de las once fichas por esta comprobación técnica.

## Acceso simplificado — ADR 020

Por instrucción del usuario, la primera protección Basic se retira del panel y sus estilos. Entre directamente a https://jyzgt.com/admin/ con Mryoan y su contraseña existente. Cuentas/permisos/contraseñas no cambian; no hay acceso anónimo al panel o listas. Documentos/presentación anteriores que muestran dos pasos son históricos para esa parte.
