# Diseño JYZ

Dirección de primera sección aprobada directamente por el usuario el 8 de octubre de 2026. Código de referencia: catalogo/templates/catalogo/inicio.html y catalogo/static/catalogo/inicio.css. La aprobación visual no autoriza publicación.

## Escena y dirección

Una persona revisa desde su celular una idea para personalizar prendas y necesita reconocer JYZ y abrir una conversación fácilmente. Tema de tinta oscura con texto claro y naranja visible, inspirado en el logo recibido, presentado como cartel de estampación. Creativa, urbana y expresiva; sin fotografía comercial inventada.

## Color

Estrategia de paleta comprometida: naranja en llamadas a la acción y cinta, tinta oscura como superficie principal y papel claro para el cartel del logo. Tokens OKLCH: tinta 18% .008 55, papel 97% .006 70, naranja 77% .17 65, texto secundario 80% .008 70. Son valores de la propuesta aprobada, no un manual oficial de marca.

## Tipografía

Antonio variable para titulares/cartel: escala fluida 55–112 px y peso 700; Barlow Regular para lectura y formularios. Selección como objeto físico: cartel de prendas y rotulación, con texto corriente legible. Fuentes locales, font-display swap y fallback Impact/Arial; no solicitudes de fuentes a terceros al visitar la página.

Fuentes descargadas del repositorio oficial google/fonts: ofl/antonio y ofl/barlow, licencias SIL OFL incluidas en catalogo/static/catalogo/fonts. Conservar avisos. No se instalaron como fuentes del sistema.

## Composición y adaptación

Escritorio: titular a la izquierda y cartel del logo a la derecha; separación proporcional y CTA clara. Bajo 800 px: una columna, titular primero, imagen después. No galería de tarjetas idénticas ni cifras comerciales. El logo se conserva como JPEG original extraído, con su fondo.

## Interacción

Enlaces con texto explícito, foco visible, enlace para saltar al contenido, HTML semántico y meta viewport. WhatsApp abre otra pestaña con mensaje preparado, sin envío automático. Respetar reduced-motion; no animación de entrada obligatoria.

## Verificación y límites

Primera sección revisada en navegador Workers local y a 390 × 844 px: fuentes e imagen cargadas, sin desbordamiento horizontal. No equivale a auditoría completa de contraste, navegación por teclado, dispositivos físicos o A10 de toda la web. Capturas locales en .local/design-review/. Las siguientes secciones deben mantener esta dirección y solo usar productos/fotos confirmados.

## Panel de administración JYZ

ADR 008: registro producto. Trabajo diario del catálogo en computadora/teléfono, tema claro papel y tema oscuro tinta. Cabecera con logo recibido/naranja, Antonio en títulos y Barlow en controles. Lista con miniaturas de 64 px y estados textuales; formulario dividido en información, opciones, fotografía y publicación. Tabla desplazable en celular sin desbordar la página. Se conservan controles estándar, foco visible y modos claro/oscuro/automático de Django. No se utiliza una biblioteca nueva ni se modifica el alcance de permisos. Propuesta pendiente de aprobación visual humana.
