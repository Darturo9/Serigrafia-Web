# ADR 018. Logo al compartir el dominio JYZ

Fecha: 8 de octubre de 2026. Solicitud directa del usuario: agregar el logo a la vista previa al compartir el enlace por WhatsApp. El usuario informa que compró https://jyzgt.com/; HTTPS devuelve 200 y la página JYZ actual.

Usar el logo JPEG existente extraído del PDF, sin alterar el original. Incorporar Open Graph en el HTML inicial de inicio y fichas públicas, con título, descripción confirmada y logo estático público HTTPS. URLs absolutas bajo jyzgt.com; raíz e inicio usan la raíz como URL canónica, las fichas conservan su ruta. No incluir consultas del formulario en metadatos. Añadir tarjeta social compatible y conservar acceso restringido del panel.

La petición autoriza implementar y desplegar este cambio acotado exclusivamente en jyz-revision/jyz-web. No cambiar DNS, comprar, instalar dependencias, migrar bases, editar catálogo, hacer commit/push ni intervenir proyectos ajenos. El dominio ya responde; no requiere conectar recursos nuevos.

Aceptación: HTML público contiene og:image; una petición anónima con agente de rastreador obtiene JPEG 200, con dimensiones y bytes coincidentes. La tarjeta real en WhatsApp requiere comprobación humana y puede conservar caché de versiones anteriores; no afirmar que se probó mediante una petición HTTP.
