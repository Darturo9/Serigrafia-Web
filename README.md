# Serigrafía Web

Proyecto de página web para un emprendimiento de serigrafía y prendas personalizadas. El cliente consulta productos y solicita una cotización por WhatsApp. El negocio administra su catálogo desde un panel privado.

## Situación actual

- **Público y verificado:** [sitio JYZ](https://jyzgt.com/), Django en Railway y datos/fotos privados en Supabase. Galería real, consulta por WhatsApp y panel de productos/fotos/galería. Sin fichas sintéticas públicas ni avisos de revisión; Admin usa un solo login Django y permisos acotados (ADR 020).
- **Entrega preparada:** Mryoan creado/login HTTPS probado; acceso privado local, guías y código entregables. Catálogo inicial de once fichas publicado con fotos seleccionadas, sin precios y con todas las tallas (ADR 019).
- **Verificación:** 65 pruebas locales y 23 comprobaciones HTTPS; revisión móvil técnica 320/390 px, confirmación humana en teléfono y práctica del responsable con Mryoan. Respaldo cifrado/restauración PostgreSQL 17 local de 13 tablas/15 objetos comprobados. WhatsApp abre destino confirmado y mensaje preparado; no se envió mensaje.
- **Pendientes del negocio:** confirmación comercial de precios/medidas, práctica con nuevos productos y custodia de una copia cifrada fuera del equipo y continuidad del respaldo manual. No hay respaldo periódico automatizado; revocación de la clave anterior sin evidencia. Dominio propio jyzgt.com comprado por el usuario y HTTPS verificado.
- **Documentación de entrega:** [guía y accesos](docs/entrega/entrega-operativa.md), [catálogo](docs/entrega/guia-de-catalogo.md), [recuperación](docs/entrega/respaldo-y-recuperacion.md). Las secciones posteriores conservan evidencia histórica; prevalece este estado y el registro final en estado-y-pendientes.

## Orden de lectura

1. `AGENTS.md`: reglas de continuidad y límites de autorización.
2. `docs/specs/01-proyecto-y-alcance.md`: objetivo y alcance.
3. `docs/specs/02-requisitos-y-recorridos.md`: comportamiento esperado.
4. `docs/specs/03-diseno-y-contenido.md`: contenido y aprobación visual.
5. `docs/specs/04-arquitectura-y-datos.md`: propuesta técnica y datos.
6. `docs/specs/05-criterios-de-aceptacion.md`: comprobaciones necesarias.
7. `docs/decisions/001-stack-y-alojamiento.md`: decisión de arquitectura y condiciones.
8. `docs/plan/estado-y-pendientes.md` y `docs/plan/tareas.md`: situación actual y trabajo siguiente.

## Cómo continuar con cualquier IA

Abrir esta carpeta como proyecto y pedir: «Lee README.md, AGENTS.md, las especificaciones y el estado. Resume lo aprobado, los pendientes y la próxima tarea. Trabaja solo dentro de la autorización que te dé. Actualiza tareas y estado con evidencia al terminar».

SDD significa desarrollo guiado por especificaciones. Los requisitos tienen identificadores y los criterios de aceptación los referencian. Si una decisión cambia, actualizar especificaciones, decisión técnica y tareas antes de implementarla. No hace falta instalar un framework SDD.

## Referencias

- `docs/referencias/Pagina web.pdf`: documento original, secciones 4.1 a 4.5.
- `docs/referencias/Propuesta_aprobada.pptx`: copia sin cambios de la presentación de cinco diapositivas utilizada como referencia del alcance.

La aprobación la confirma el usuario. El archivo no contiene una firma ni demuestra una aprobación formal individual de cada diapositiva. Los mensajes de Marielos aclaran que la atención será por WhatsApp, que existe logo y que la web quedará al emprendimiento.

Los apartados originales de pagos, CRM, inventario y logística describen posibilidades más amplias. Para esta primera versión prevalece el alcance acordado en las especificaciones.

## Autorización de esta etapa

El usuario autorizó la prueba local de Django Admin, productos y fotos y, posteriormente, inspección remota de solo lectura y preparación local del plan de alojamiento. Se creó una aplicación mínima con dependencias aisladas y migraciones en PostgreSQL local. La instalación local aislada de Python y herramientas Workers fue autorizada expresamente. Git inicializado el 8 de octubre en la rama local main y asociado a https://github.com/Darturo9/Serigrafia-Web.git como origin, sin commits ni push. El 8 de octubre se autorizó y ejecutó el paquete de prueba Supabase; Cloudflare y publicación siguen pendientes.

## Prueba local

Consultar `docs/plan/prueba-local.md` para iniciar Docker, ejecutar verificaciones y crear el acceso administrativo. Catálogo: http://127.0.0.1:8000/ . Panel: http://127.0.0.1:8000/admin/ . Estos accesos funcionan mientras el servidor local esté iniciado. La pantalla actual es una prueba técnica con un producto ficticio, no el diseño comercial aprobado.

## Materiales del comercio

Se recibió `docs/referencias/JYZ info.pdf`. Contenido y pendientes actualizados en `docs/specs/06-materiales-del-comercio.md`. Las cuentas de Supabase y Cloudflare existen según el usuario. El nuevo servidor MCP autenticado verificó lectura del proyecto `kcahxuvfmrzxzlnpezyf`; la inspección inicial no encontró tablas de aplicación ni buckets; posteriormente se creó el paquete de prueba autorizado del 8 de octubre. El conector del plugin falló anteriormente y es una conexión distinta. Ver [resultados de inspección](docs/plan/inspeccion-supabase.md) y [plan de alojamiento preparado](docs/plan/prueba-alojamiento.md). La integración completa con Workers/Hyperdrive sigue pendiente.

## Workers local y siguiente etapa

Ver [evidencia de ejecución](docs/plan/evidencia-workers-local.md), [guía reproducible](docs/plan/ejecutar-workers-local.md) y [ADR 003](docs/decisions/003-adaptacion-local-a-python-workers.md). El Worker local usa PostgreSQL Docker y fotos en memoria; Storage persistente se verificó desde Django nativo; la integración con Workers remoto aún no está verificada. SQL, inventario de migraciones y configuración del bucket están preparados en `ops/` con estado documentado; esquema, migraciones y bucket ya se aplicaron en Supabase con autorización.

WhatsApp confirmado directamente: `+502 47233834`. La validación y generación de mensajes están preparadas y probadas localmente (31 pruebas nativas en total). La cotización está integrada en `/inicio/`; el formulario anterior de seguimiento fue retirado por instrucción del usuario (ADR 010). WhatsApp está en el footer, junto al logo e Instagram. La apertura real del chat sigue pendiente. La primera sección fue aprobada; faltan productos reales.

Ver [solicitudes WhatsApp preparadas](docs/plan/solicitudes-whatsapp.md). No se guardan pedidos ni se envían mensajes automáticamente.

La [guía de administración preparada](docs/entrega/guia-de-catalogo.md) describe el panel existente. Acceso definitivo y capacitación pendientes.

## Avance autorizado del 8 de octubre

[Primera sección](http://127.0.0.1:8787/inicio/) implementada y dirección visual aprobada. Supabase ya contiene esquema/roles, 19 migraciones, producto sintético oculto y bucket privado de prueba; ver [evidencia remota](docs/plan/evidencia-supabase-prueba.md). Carga y lectura privada de fotos y 14 comprobaciones del panel aprobadas desde Django nativo contra Supabase. Cloudflare/Hyperdrive remoto sigue pendiente. Catálogo, cotización, galería y contacto están integrados como vista de revisión; faltan productos y fotos comerciales autorizados.

## Repositorio asociado

[GitHub: Darturo9/Serigrafia-Web](https://github.com/Darturo9/Serigrafia-Web). La consulta de referencias remotas respondió sin ramas ni etiquetas. La carpeta local conserva toda la aplicación y documentación; no se ha enviado contenido. `.local/`, entornos y archivos de secretos están excluidos mediante `.gitignore`. Commit/push siguen pendientes de autorización.

El [paquete de prueba Cloudflare](docs/plan/paquete-cloudflare-prueba.md) está preparado y supera empaquetado local (43,34 MiB). Recursos, secretos y despliegues requieren autorización específica; compatibilidad completa y costos en cuenta real pendientes.

Storage real también supera carga/lectura PNG/JPEG/WebP desde WebAssembly en Workers local y lectura desde otro proceso. Hyperdrive, alojamiento remoto y persistencia tras redespliegue continúan pendientes.

## Resultado remoto Cloudflare

Con autorización, se crearon CA/Hyperdrive y se desplegó una versión protegida de prueba. **Django no supera la prueba en Workers Free:** registros confirman límite de CPU al cargar el framework. No se ha cambiado plan ni contratado nada; segundo despliegue y aceptación pendientes de decisión. Ver [evidencia y opciones](docs/plan/evidencia-cloudflare-prueba.md).

## Presentación funcional

Panel personalizado en Railway con logo, miniaturas, estados y ficha agrupada; 43 pruebas locales y once comprobaciones HTTPS aprobadas. Aprobación visual humana pendiente. Para retirar ejemplos y presentar el sitio sin textos provisionales, ver [plan concreto](docs/plan/presentacion-funcional.md). La web continúa protegida; dominio propio no requerido.

## Fichas y fotos múltiples

Ampliación autorizada y desplegada: «Ver producto», ficha con miniaturas y «Quiero este producto» para preparar cotización de productos reales publicados. 51 pruebas locales y 17 comprobaciones HTTPS aprobadas. Dos migraciones y permisos de imágenes aplicados; tres fotos anteriores conservadas por referencia y SHA-256. Ver [paquete y resultados](docs/plan/fichas-y-fotos-multiples.md). Los ejemplos continúan identificados y sin compra.

## Galería administrable verificada

[Admin → Galería](https://jyz-web-production.up.railway.app/admin/catalogo/galeriaimagen/) permite fotos, título/descripción, orden y mostrar/ocultar. Tres fotos reales recibidas en Storage privado, conversión WebP automática; 27 comprobaciones HTTPS y edición/orden/ocultación/restauración aprobadas. Productos y archivos anteriores conservados. Ver [resultado y límites](docs/plan/galeria-administrable.md). Los apartados históricos de preparación conservan el avance anterior; este resultado reemplaza el estado de galería fija/pendiente. Capacitación y catálogo comercial siguen pendientes.


## Trabajos ocultos temporalmente — ADR 021

Por solicitud del usuario, la sección pública Trabajos y su enlace están comentados. Galería sigue disponible en Admin; fotos y registros se conservan. Retirar los dos bloques de comentario Django en inicio.html permite reactivarla.
