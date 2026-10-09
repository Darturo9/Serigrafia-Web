# Estado y pendientes

**Estado vigente al 8 de octubre:** web pública entregada en https://jyzgt.com/, dominio comprado por el usuario y HTTPS verificado. Logo para enlaces compartidos implementado/desplegado/verificado técnicamente (ADR 018); tarjeta real de WhatsApp pendiente de confirmación humana. Admin protegido, galería real y catálogo comercial a cargo del negocio; entrega/práctica inicial confirmadas. Ver registros finales para evidencias y límites. vibrant-perfection intacto y protegido por instrucción expresa.

## Corte documental

Fecha del corte inicial: 7 de octubre de 2026, contexto del usuario en Guatemala. Estado vigente: ver registro del 8 de octubre al final; las sesiones anteriores conservan su contexto histórico.

La propuesta funcional fue aceptada según confirmación directa del usuario. Se creó el paquete SDD. Hay una aplicación técnica local con Django Admin, PostgreSQL en Docker y fotos locales. No hay repositorio Git inicializado ni servicios externos configurados.

| Tema | Estado | Evidencia o límite |
|---|---|---|
| Alcance funcional | Aprobado | Confirmación directa del usuario: «Si aceptaron la propuesta» |
| Atención por WhatsApp | Aprobado | Mensaje de Marielos: «Por Whatsapp Tito» |
| Web para uso real | Aprobado | Marielos indica que debe dejarse al emprendimiento |
| Panel para productos | Aprobado en el alcance documentado | Solicitud posterior de incluir administración y aprobación de la propuesta |
| Logo | Recibido dentro del PDF; original pendiente | Identidad JYZ; vector/archivo independiente sin recibir |
| Redes | Enlaces candidatos recibidos; verificación pendiente | Especificación 06; no afirmar destinos verificados |
| Stack y alojamiento | Propuesto | Elección del usuario; integración no probada |
| Documentos y copias | Verificado | Validación documental en esta etapa |
| Catálogo y fotos | Parcial | PDF con tipos e imágenes de referencia; faltan fichas y fotos autorizadas |
| WhatsApp real | Número internacional confirmado | +502 47233834; formulario/apertura todavía sin probar |
| Dominio y costos | Pendiente | Sin nombre comprado ni presupuesto confirmado |
| Prueba local | Verificado localmente | 10 pruebas PostgreSQL, persistencia desde segundo proceso, catálogo y login revisados en navegador |
| Acceso MCP Supabase | Verificado en lectura | Servidor OAuth devuelve URL del proyecto correcto y SELECT; distinto del conector previo |
| Prueba en Workers | Verificada localmente, remoto pendiente | 25 comprobaciones HTTP y 21 pruebas nativas; fotos locales en memoria |
| Lanzamiento | Pendiente | Requiere revisión y autorización |

## Decisiones que requieren información

- Confirmar uso de identidad JYZ recibida; archivo de logo independiente y nombre legal, si corresponde.
- Productos y opciones que deben aparecer; derechos y autorización de fotos.
- Funcionamiento de WhatsApp y verificación de identidad/destinos de redes.
- Persona administradora y persona responsable de atención.
- Registro manual de pedidos y referencias para seguimiento.
- Dominio, titular de cuentas, presupuesto de publicación y renovación.
- Coordinación de Henry y Roger, mencionados en la imagen original.
- Esquema exacto del catálogo, tamaños de fotos y versiones técnicas tras prueba.

## Próximo paso

P1 y P2 completados localmente. Revisar el paquete concreto en ops/ y autorizar específicamente esquema/roles, migraciones, bucket y datos sintéticos antes de P3–P4. Después se requerirá autorización propia de Hyperdrive y Worker protegido, incluyendo despliegues de prueba. La lectura MCP ya pasó; no demuestra integración. Completar materiales y aprobar la primera sección antes de extender el diseño.

## Registro de continuidad

Cada sesión agrega fecha, autorización recibida, tareas afectadas, resultados con evidencia, pendientes y siguiente paso. No reemplazar hechos previos con supuestos. Actualizar estado «verificado» solo con comprobación real.

## Fuentes humanas

Mensajes y capturas compartidos por el usuario en este chat, resumidos en los documentos para permitir continuidad. No se copió la captura como archivo de referencia porque el plan solo contempla PDF y presentación; sus roles y el resultado esperado están recogidos aquí y en alcance.

## Registro inicial

- Autorización: implementar el plan de carpeta y documentación, sin aplicación ni servicios.
- Resultado: documentos Markdown y copias de referencias.
- Validación: estructura, enlaces relativos, requisitos/aceptación y hashes de copias.
- Pendiente: toda implementación y prueba del sitio.

## Sesión de implementación local — 7 de octubre de 2026

- Autorización: «Muy bien, puedes proceder» para el paso local acordado; luego «Ya levante docker en local».
- Resultado: Django 5.2.18 en entorno aislado; catálogo mínimo, panel y rol Responsable de catálogo; PostgreSQL 16.14 exclusivo en Docker; fotos locales.
- Evidencia: 10 pruebas pasan en PostgreSQL; `check` sin problemas; migración sin cambios pendientes; `.local/persistencia.json` confirma producto y hash de foto desde segundo proceso. Catálogo/foto y login revisados en navegador.
- Límites: no se crearon credenciales administrativas persistentes; hay comando interactivo para hacerlo. No se verificó reinicio de contenedor, respaldo, móvil, Supabase, Storage ni Workers. Formulario WhatsApp, galería y diseño comercial aún pendientes.
- Guía reproducible: `docs/plan/prueba-local.md`.

## Materiales y cuentas — 7 de octubre de 2026

- Usuario confirma «Listo» tras indicaciones para probar el panel; es confirmación humana, no una nueva inspección de sus datos.
- Recibido PDF JYZ de cinco páginas, leído completo y revisado visualmente. Copia conservada sin cambios.
- Contenido detallado en especificación 06; pendientes iniciales de identidad/contacto ahora son parciales, no ausencia total de materiales.
- Supabase: referencia `kcahxuvfmrzxzlnpezyf` recibida. Consultas de proyecto y tablas rechazadas por permisos. No se modificaron recursos externos.
- Cloudflare: cuenta existente según el usuario; acceso y recursos no verificados.
- Próximo paso técnico: conectar Supabase en Codex con permiso para ese proyecto; inspección de esquema antes de preparar migraciones. Preparar cambios concretos antes de solicitar aplicación remota cuando sea necesaria.

## Autenticación MCP — 7 de octubre de 2026

- El usuario completó OAuth. `codex mcp add` terminó con «Successfully logged in» y `codex mcp list` muestra `supabase` habilitado con OAuth y limitado a `kcahxuvfmrzxzlnpezyf`.
- La conexión se agregó a la configuración global del cliente; el alcance remoto está limitado por `project_ref`.
- El conjunto de herramientas de este chat todavía expone el conector del plugin `mcp__codex_apps__supabase_*`; su consulta de tablas sigue devolviendo falta de permisos. No confundirlo con el nuevo servidor CLI autenticado.
- Pendiente: recargar la sesión del cliente para que exponga el servidor nuevo y verificar lectura de tablas con esa conexión. No se aplicaron cambios remotos.

## Inspección OAuth y preparación — 7 de octubre de 2026

- Autorización directa: inspección de solo lectura y preparación local. Prohibidos migraciones remotas, configuración externa, publicación, compras, commit y push; instalaciones sin autorización.
- Se leyó AGENTS, README, seis especificaciones, dos decisiones y documentos de plan. Se preservaron aplicación y referencias. Git continúa sin inicializar.
- El nuevo servidor `mcp__supabase__*` está disponible. `get_project_url` coincide con `kcahxuvfmrzxzlnpezyf`; consultas SELECT y listado de tablas/migraciones respondieron correctamente. El conector previo no se usó ni se volvió a verificar.
- PostgreSQL remoto 17.11; 12 esquemas incluidos los del sistema. Inventario no perteneciente al catálogo del sistema: 39 tablas y 3 vistas, correspondientes a servicios Supabase; `public` sin tablas/vistas, sin esquema JYZ ni tablas Django. Conteos exactos: 0 buckets y 0 objetos. Historial de migraciones consultado por MCP vacío, distinto de migraciones internas de servicios.
- No se consultaron contenidos de usuarios, tokens ni secretos. Inventario no equivale a auditoría completa ni a permiso de escritura.
- Entregables: `inspeccion-supabase.md` con consultas/resultados y `prueba-alojamiento.md` con pasos, recursos remotos propuestos, restricciones y evidencia requerida. Corrección: prueba técnica A02–A06, A11/A13 parciales; A07 depende de WhatsApp.
- Revisión del código local: settings/media son de desarrollo; faltan adaptador, settings Workers, Storage y assets de Admin. `uv` disponible; wrangler/pywrangler no encontrados en PATH. No se descargó ni instaló nada.
- Verificación de esta sesión: lectura remota exitosa y revisión documental; enlaces Markdown locales comprobados. No se repitieron las 10 pruebas locales ni se ejecutó Worker, conexión Django remota, upload, migración o despliegue. Cloudflare y planes de cuentas siguen sin inspección.
- Próximo paso: P1 local; autorización de instalación si hace falta para P2; paquete exacto de cambios remotos después del filtro local. ADR 001 permanece propuesto; no se cambió arquitectura ni se adoptaron configuraciones propuestas como decisiones definitivas.

## Adaptación y ejecución Workers local — 7 de octubre de 2026

- Autorización: continuar implementación local y objetivo de avanzar hoy; instalación aislada aprobada expresamente. No amplía permiso remoto, commit ni push. WhatsApp +502 confirmado directamente.
- Resultado: settings separados, entrada WSGI serializada, PBKDF2 compatible vía Web Crypto, perfil de ruedas WebAssembly fijado, assets Admin y backend REST privado Supabase preparado. Se preservó .venv y el catálogo original; prueba Workers en esquema local jyz_worker_local.
- Evidencia: 21 pruebas nativas aprobadas (10 existentes + 11 nuevas); 25 comprobaciones HTTP aprobadas en workerd con Python 3.14.2, incluyendo sesiones, permisos, CSRF, alta/edición/ocultación, tres formatos, rollback y concurrencia. Ver evidencia-workers-local.md y ADR 003.
- Preparación remota: ops/01-esquema-y-roles.propuesto.sql, inventario de 19 migraciones, SQL de catálogo para revisión, bucket privado propuesto y configuración Workers con placeholders. Ninguno aplicado fuera del equipo local.
- Límites: fotos de Workers en memoria; backend Supabase probado con respuestas simuladas, sin upload real ni prueba de su transporte en WebAssembly. Sin Hyperdrive remoto, revisión visual/móvil, costo confirmado, despliegue ni persistencia tras redespliegue. Bundle local aproximado 44 MiB sin comprimir; límites reales pendientes. No hay catálogo comercial ni primera sección aprobada.
- Siguiente paso: revisar/provisionar paquete remoto únicamente con autorización específica y credenciales por canal seguro; en paralelo completar materiales y preparar primera sección para revisión. No se garantiza publicación hoy.

## Cierre documental — 8 de octubre de 2026

- Actualizados README, AGENTS, arquitectura, criterios, materiales, tareas y plan de alojamiento con evidencia local y límites remotos.
- Guía de reproducción y ADR 003 guardados; staging incluye lock npm y lock WebAssembly. Comprobación de sintaxis Python y enlaces Markdown locales aprobada.
- Se solicitó autorización específica del paquete Supabase preparado. Hasta respuesta explícita, continúa prohibida su aplicación. Cloudflare/despliegues quedan fuera de esa solicitud.

## Solicitudes y preparación visual — 8 de octubre de 2026

- Turno anterior clasificado como progreso: adaptación comprobada, documentación y staging actualizados. Sin respuesta nueva que amplíe permisos remotos.
- Leídos requisitos/contenido, decisiones y reglas actuales. Extracción directa del JPEG del logo recibido; PDF preservado y hash registrado junto al recurso. No se usaron fotos de referencia como trabajos.
- Implementados CotizacionForm y SeguimientoForm en catalogo/solicitudes.py: cantidades/tallas/colores, rechazo de productos ocultos/de ejemplo o modificados, texto Unicode y número confirmado. No hay registros de pedidos ni envío automático.
- Evidencia: 7 pruebas nuevas; 28 pruebas nativas aprobadas en PostgreSQL local. Las 25 comprobaciones HTTP de Workers siguen como evidencia previa del runtime; no prueban estos formularios ni la apertura de WhatsApp.
- Se solicitaron preferencias de tono visual y estilos a evitar; contexto visual y primera sección aún sin implementar/aprobar. Próximo paso: preparar esa sección tras respuestas y mantener pendiente el paquete remoto hasta autorización explícita.

## Guía de administración — 8 de octubre de 2026

- Turno anterior: progreso, con lógica de solicitudes y siete pruebas nuevas. Se conserva la prohibición de cambios remotos y extensión visual sin las respuestas/aprobaciones pendientes.
- Preparada guía de administración en docs/entrega/guia-de-catalogo.md, contrastando campos, límites, permisos y errores con modelos/formulario/Admin/comando de rol. Incluye recorrido de capacitación pendiente y límites de almacenamiento local/remoto.
- Login Workers local revisado visualmente en navegador: etiquetas y botón visibles, pantalla de prueba. No se ingresaron credenciales ni se editaron productos en esta inspección. La observación confirma proceso local accesible actualmente; no es nueva prueba de persistencia ni prueba remota.
- R10 parcialmente preparado; A12 sigue pendiente de persona responsable, acceso definitivo y ejercicio real con la guía. Sin commit, push, cambios externos ni publicación.
- Próximos pasos dependen de respuestas: estrategia visual para primera sección y permiso del paquete Supabase. No solicitar otra vez autorizaciones ya pendientes.

## Auditoría de continuidad — 8 de octubre de 2026

- Último turno clasificado como progreso: guía concreta y revisión visual de login. La implementación completa no está terminada.
- Revalidado estado actual: solo existe plantilla técnica de catálogo; formularios WhatsApp tienen lógica probada sin integración visible; configuración remota mantiene placeholders; recursos remotos propuestos sin aplicación autorizada.
- La misma falta de respuestas/autorización se mantiene durante al menos tres turnos consecutivos. Se agotaron los pasos locales independientes necesarios de esta etapa: adaptador/runtime, backend preparado, mensajes validados, recursos de identidad y guía. No se prolongará la ejecución con comprobaciones repetidas ni documentos que no desbloqueen la implementación.
- Dependencias para retomar: responder permiso concreto de Supabase y preferencias visuales ya solicitadas. Después deben revisarse primera sección, catálogo/materiales reales, prueba remota y entrega; no confundir guía/pruebas locales con A01–A13 completos.
- Restricción remota: AGENTS exige autorización explícita de la acción externa concreta. Restricción de diseño: habilidad Impeccable, reference/teach.md, exige confirmar respuestas estratégicas antes de escribir PRODUCT.md; AGENTS exige aprobar primera sección antes de extenderla. No se pidió otra vez la misma autorización ni se cambió proveedor.

## Reanudación autorizada — 8 de octubre de 2026

El usuario respondió: «Autorizo Supabase; expresivo y urbano; sin estilos que evitar» y pidió proceder con el objetivo. Autoriza el paquete concreto previamente presentado: esquema/roles, 19 migraciones, bucket privado y pruebas sintéticas en el proyecto indicado. No autoriza Cloudflare ni despliegues. La primera sección puede prepararse con esa dirección visual; debe aprobarse antes de extenderla.

## Ejecución autorizada y diseño aprobado — 8 de octubre de 2026

- Esquema y roles aplicados/verificados; login provisionado con secretos locales restringidos. 19 migraciones Django y 11 tablas en jyz_prueba; ACL sin acceso anon/authenticated. Producto sintético oculto creado/editado/releído con rol jyz_app; lectura desde otro proceso comprobada.
- Bucket privado jyz-prueba-fotos creado por dashboard y configuración comprobada por MCP. Backend de fotos pendiente de clave utilizable; solicitud de provisión segura abierta. Ver evidencia-supabase-prueba.md para fallos, correcciones y límites.
- Primera sección implementada en /inicio/ con logo recibido y fuentes locales OFL. Revisada en navegador y viewport 390 px; capturas locales. El usuario respondió «Apruebo la dirección visual», autorizando extensión del diseño. PRODUCT.md y DESIGN.md recogen dirección y límites.
- No se tocó Cloudflare ni se desplegó; no commit/push. Próximo paso: extender secciones/formularios reales y probar backend de fotos cuando exista credencial. Catálogo real, galería autorizada y entrega definitiva siguen pendientes.

## Fotos y panel Supabase verificados — 8 de octubre de 2026

- El usuario dejó la clave Storage en el archivo local indicado; presencia y permisos 0600 verificados sin mostrar su contenido. Su uso contra el proyecto autorizado funcionó. Reemplazo de la clave compartida en un comentario pendiente antes de entrega/despliegue.
- Django nativo cargó y leyó PNG/JPEG/WebP en bucket privado; bytes/hashes, URL firmada y rechazo de lectura pública comprobados. Segundo proceso confirmó persistencia. Panel probado con Django Client nativo: 14 comprobaciones aprobadas, incluyendo sesión, CSRF, permisos, edición/foto, rechazo de imagen corrupta y ocultación.
- SELECT MCP final: 19 migraciones, 11 tablas con RLS, cuatro objetos sintéticos y producto de ejemplo oculto. Rol jyz_app operativo; anon/authenticated sin acceso al esquema. Dashboard Data API: jyz_prueba no seleccionado, 0 de 11 tablas expuestas; sin cambios en esa pantalla. Asesor de seguridad sin avisos.
- Vista /inicio/ extendida tras aprobación visual: catálogo real filtrado, cotización, galería sin fotos inventadas y contacto/seguimiento. 31 pruebas nativas aprobadas; seguimiento Unicode observado en navegador Workers local. Catálogo real aún vacío.
- Evidencia y límites: evidencia-supabase-prueba.md; registros fotos-result.json, admin-result.json y persistencia-foto.log dentro de .local/supabase-prueba.
- Pendientes: transporte Storage en Workers, Hyperdrive remoto, reinicio/redespliegue, recuperación y costos. Pruebas nativas remotas no confirman alojamiento final ni A06 completo. No se crearon recursos Cloudflare, desplegó, compró, hizo commit ni push.
- Próximo paso: preparar/comprobar el paquete Cloudflare y solicitar autorización concreta para Hyperdrive, secretos y Worker de revisión protegido. Completar catálogo/fotos comerciales y responsables antes de publicar.

## Reemplazo de clave y asociación Git — 8 de octubre de 2026

- Usuario informa reemplazo de la clave Storage y proporciona https://github.com/Darturo9/Serigrafia-Web.git. Lectura privada de la foto actual comprobada con Django nativo, sin modificaciones remotas ni impresión de secretos; archivo 0600. Revocación anterior no verificada.
- Consulta git ls-remote exitosa, sin referencias anunciadas. Git inicializado en la carpeta existente, rama main, origin configurado con esa URL. No se clonó sobre los archivos ni se reemplazó contenido.
- git check-ignore confirma exclusión de storage-key, configuración con contraseña, entornos y archivos .env/.dev.vars. Todos los archivos del proyecto permanecen sin seguimiento: sin git add, commit ni push.
- Pendientes técnicos y límites de Cloudflare/publicación continúan vigentes. Próximo paso: preparación local del paquete Cloudflare; cualquier envío al repositorio requiere autorización explícita.

## Preparación Cloudflare — 8 de octubre de 2026

- Turno anterior: progreso, credencial actual verificada en lectura y Git asociado al remoto sin commit/push.
- scripts/worker_remote_prepare.py genera paquete independiente, excluye secretos/pruebas/perfiles nativos y reutiliza ruedas instaladas. Primer intento pywrangler falló al resolver Pillow; se conservan versiones y Wrangler empaquetó directamente las ruedas existentes. Resultado dry-run exit 0, 44377.76 KiB (43,34 MiB), 134 assets, máximo 325171 bytes. Evidencia .local/worker-remote-review/result.json y dry-run.log.
- Límites documentados actuales: 64 MiB sin comprimir, 128 MB memoria, 1 segundo de inicio; Free 10 ms CPU/petición. Paquete dentro del límite de tamaño; CPU/memoria/inicio y cuenta real sin comprobar. No se garantiza gratuidad.
- Preparado paquete-cloudflare-prueba.md y ops/hyperdrive-prueba.propuesto.json: CA pública, Hyperdrive directo con jyz_app, verify-full, 5 conexiones, sin caché, Worker protegido y secretos en servidor; dos despliegues de prueba propuestos.
- Autorización específica requerida antes de recursos/despliegues/transferencia de credenciales a Cloudflare. No se crearon servicios, publicó, instaló herramientas nuevas ni hizo commit/push. Catálogo comercial y recuperación siguen pendientes.

## Lectura Storage en Workers local — 8 de octubre de 2026

- Turno anterior clasificado como progreso: paquete Cloudflare preparado y dry-run aprobado. La solicitud concreta de autorización sigue sin respuesta; continuación automática del objetivo no amplía permisos.
- Trabajo independiente autorizado: diagnóstico de transporte Storage en workerd local, sin despliegues ni escrituras remotas. Dos intentos detectaron AttributeError getReader en HEAD/jsfetch. exists corregido a GET object/info; lectura aprobada y ampliada a URL firmada y acceso público rechazado. Bytes/hash coinciden con lectura nativa (137 bytes).
- Proceso de diagnóstico concluido; resultados en .local/worker-storage-read-4/result.json, sin valores secretos ni URLs firmadas. Endpoint temporal separado de la web, loopback con token. Pruebas nativas: 31 aprobadas. Paquete remoto incluye corrección; dry-run exit 0, 44377.92 KiB.
- Pendientes: upload en WASM, Hyperdrive, comportamiento/límites Cloudflare y redespliegue. Autorización de recursos/secretos/despliegues sigue necesaria según AGENTS; no se repite solicitud ni se considera el silencio como aprobación. Sin compras, commit/push o publicación.

## Carga Storage desde WASM — 8 de octubre de 2026

- Turno anterior: progreso, fallo HEAD corregido y lectura Storage/URL firmada verificada desde workerd local; autorización Cloudflare sin respuesta.
- Comprobación independiente dentro de Supabase autorizado: PNG/JPEG/WebP sintéticos creados y guardados desde Pillow/Storage en WASM. Tres objetos adicionales (82/633/68 bytes), metadatos y bytes/hash privados/firmados coincidentes; imagen corrupta rechazada.
- Proceso local de diagnóstico terminado. Otro proceso Django releyó las tres fotos y verificó hashes; producto de prueba continúa oculto/de ejemplo, sin modificar referencia de foto. Evidencia .local/worker-storage-read-5/result.json y persistence.json. Sin eliminaciones.
- Transporte Storage local en WASM verificado en carga y lectura. ORM/Hyperdrive remoto, CPU/memoria en Cloudflare y persistencia tras segundo despliegue siguen pendientes. No se crearon servicios Cloudflare, desplegó, compró ni hizo commit/push. Sigue abierta la solicitud concreta del paquete Cloudflare; no reinterpretar la continuación automática como aprobación.

## Auditoría de bloqueo Cloudflare — 8 de octubre de 2026

La misma autorización pendiente se mantiene desde la presentación del paquete Cloudflare y durante al menos tres turnos consecutivos de la meta. Los turnos anteriores aportaron progreso independiente: empaquetado, corrección HEAD y carga/lectura Storage WASM con persistencia desde otro proceso. Resultados actuales revalidados: todos aprobados; configuración remota conserva Hyperdrive ficticio y workers_dev=false.

No hay un proceso de despliegue pendiente de esperar: las comprobaciones locales finalizaron y no se inició despliegue. La siguiente prueba necesaria requiere crear Hyperdrive, transferir secretos a Cloudflare y desplegar dos versiones del Worker, acciones sin autorización específica. No repetir pruebas aprobadas ni generar trabajo accesorio para sostener ejecución automática. Meta bloqueada por esta dependencia humana, sin declarar implementación o alojamiento completos. Se retomará con respuesta explícita al paquete-cloudflare-prueba.md; catálogo comercial, fotos autorizadas y responsables siguen pendientes para la entrega final.

## Autorización Cloudflare recibida — 8 de octubre de 2026

Usuario responde «Si autorizo» al paquete concreto solicitado. El bloqueo de autorización se resuelve; comenzar por inspección de acceso CLI, cuenta y plan. Recursos/secretos y dos despliegues protegidos autorizados según paquete-cloudflare-prueba.md; sin compras, cambio de plan, dominio/DNS, lanzamiento comercial, eliminaciones, commit ni push. No afirmar acceso Cloudflare ni ejecución remota antes de verificar.

## Acceso Cloudflare — 8 de octubre de 2026

Wrangler 4.148.0 whoami confirma que no existe sesión CLI autenticada. Iniciado login OAuth en navegador predeterminado con account:read, user:read, workers:write y ssl_certs:write (offline_access añadido por Wrangler). La aprobación OAuth debe completarla el usuario. Proceso de login pendiente; comprobar su handle antes de repetir o reiniciar. No se han creado CA, Hyperdrive ni Worker ni enviado credenciales Supabase a Cloudflare. La autorización del paquete está recibida y no debe pedirse otra vez; autenticación es una dependencia distinta.

## Inicio de ejecución Cloudflare — 8 de octubre de 2026

Login OAuth inicial venció; usuario solicitó reinicio y posteriormente confirmó autorización concedida. CLI confirmó sesión. Dashboard cuenta bdc73f4bbbc036a160e49f5f9cc86b62, plan Free y subdominio giron605.workers.dev. Consultas API de suscripción/subdominio denegadas por scopes iniciales; se verificaron mediante dashboard sin modificar plan.

CA pública jyz-supabase-prueba-ca subida, ID a49c9d58-9d1e-4134-8eba-0003b263fa53. Hyperdrive jyz-prueba creado, ID 0b4d3142b2354c2d832c44bf1f0fde4a: origen directo Supabase, rol jyz_app, verify-full, caché desactivada y límite 5 conexiones. Creación API exitosa verifica credenciales/conexión inicial, no ORM. Evidencia .local/cloudflare-prueba/hyperdrive-create.json.

OAuth ampliado únicamente con workers_scripts:write y workers_tail:read necesarios para scripts y diagnóstico; usuario completó esa segunda autorización. Primer deploy CLI en curso con --secrets-file local 0600, origen HTTPS jyz-prueba.giron605.workers.dev, previews desactivadas y observabilidad para pruebas. No declarar despliegue exitoso antes de verificar proceso/versión y HTTP. Cuenta conserva Free; sin compras, cambios de plan, DNS/dominio, commit ni push.

## Resultado Cloudflare Free — 8 de octubre de 2026

- Primer deploy terminó exitosamente: versión 10db0a9f-cb3c-4212-ae88-1de6361d2522, startup 899 ms. Recursos Hyperdrive/CA aplicados y settings/secrets revisados sin valores. Cuenta conserva Free.
- HTTP anónimo 401; autorizado inicio 500 (Cloudflare 1101), login Admin 503. Tail diagnóstico confirma CpuLimitExceeded al importar Django (cpuTime 2003 ms) y otro evento exceededCpu (16 ms), frente al límite Free 10 ms. No se probó ORM/hiperdrive desde una petición Django exitosa.
- Resultado técnico fallido, no alojamiento aceptado. Detenida etapa y segundo despliegue, tal como se acordó si Free no resulta suficiente. Se preserva versión protegida y recursos; no se compra ni cambia plan.
- Próximo paso requiere decisión: autorizar evaluación con Workers Paid y contratación por el usuario (mínimo USD 5/mes más excesos), o acordar investigación de una alternativa de alojamiento Django. Paid no probado; no prometer compatibilidad ni costo final.
- Evidencia: evidencia-cloudflare-prueba.md y .local/cloudflare-prueba/diagnostico.json/estado-remoto.json. Sin commit/push, cambios DNS o publicación comercial.

Comprobación final: API confirmó configuración real de Hyperdrive y los cuatro bindings secret_text sin valores. Nueva petición anónima devolvió 500 después de los fallos; la evidencia 401 corresponde al primer intento, no garantiza disponibilidad estable. No hubo contenido Django servido. No dar A02 por aprobado.
# Estado vigente — Railway elegido el 8 de octubre de 2026

El usuario indicó «Mejor con Railway, es la plataforma que más conozco!». Railway sustituye Workers/Hyperdrive como destino de la próxima prueba, conservando Django, Admin, PostgreSQL y Storage Supabase. ADR 004 registra la decisión; prueba-railway.md concreta preparación local, paquete remoto y criterios. Integración Railway no verificada.

Este turno actualizó documentación y arquitectura, sin cambios de código, recursos, secretos o datos remotos. No se ejecutaron pruebas de aplicación porque no cambió código. Próximo paso: preparar perfil nativo, protección de revisión y paquete local; nuevas instalaciones y ejecución remota requieren autorización aplicable. No ejecutar migrate automático. Commit/push, compras, dominio/DNS, publicación y eliminación de recursos Cloudflare siguen pendientes de autorización.

Las secciones anteriores conservan el historial de etapas y pruebas; para la elección de alojamiento prevalece ADR 004.

## Avance Railway autorizado y preparación nativa

Usuario reitera «Railway ya está aprobado… puedes proceder». Acceso CLI 4.40.2 confirmado; dashboard del workspace muestra Trial expired. Usuario activará el plan y avisará. No contratar ni cambiar suscripción por él; no se alteraron proyectos existentes ni creó JYZ.

Perfil nativo, gate de revisión antes de assets/Admin, TLS con rol limitado, CA pública, Dockerfile/config Railway y paquete separado preparados. 39 pruebas locales aprobadas (31 anteriores + 8 nuevas), sin nuevas instalaciones ni escrituras Supabase. Native probe, Gunicorn/collectstatic y build Docker pendientes de respuesta a instalación aislada solicitada; luego primera/segunda versiones cuando el plan esté activo. A02–A06 en Railway siguen pendientes. Evidencia detallada: evidencia-railway-prueba.md.

## Vista local para mostrar avances

El usuario solicitó abrir el frontend para mostrarlo a su amiga. Se verificó el servidor existente en 127.0.0.1:8787: GET /inicio/ respondió HTTP 200 con contenido JYZ y la sección aprobada. Se abrió la página en Codex; no se inició una instancia duplicada. Es una vista local, con catálogo/fotos comerciales pendientes; no implica despliegue Railway ni enlace accesible desde otro dispositivo.

## Plan Railway activo y proyecto protegido

El usuario informa que pagó Railway e instruye NUNCA borrar vibrant-perfection. Dashboard confirma Hobby activo en darturo9's Projects; vibrant-perfection (53241be7-2641-4ab2-9ac5-82c3943af5fa) visible con bot-AI/Redis. AGENTS.md y plan Railway registran prohibición de borrar o modificar ese proyecto; JYZ debe usar otro proyecto. Solo se realizaron lecturas, sin crear/modificar/borrar recursos. CLI whoami/list respondieron; status en la carpeta actual devolvió Unauthorized, por lo que el contexto de despliegue aún necesita verificar al vincular el proyecto JYZ.

Plan de cuenta resuelto. Instalación aislada Gunicorn/WhiteNoise/httpx continúa sin respuesta; no inferir su autorización del pago del alojamiento. Arranque nativo, build Docker y despliegue siguen pendientes.

## Railway desplegado y probado — ruta directa

El usuario eligió desplegar directamente en Railway sin instalar paquetes localmente. Se creó jyz-revision (db6b6a44-0a60-4ae3-b8b3-5bb4c309bc6a) y servicio jyz-web (bf4d7246-eda6-4265-b649-695fa2fd5991), origen https://jyz-web-production.up.railway.app/inicio/. Vinculación CLI del proyecto nuevo resolvió el contexto anterior; destino confirmado antes de secretos y segundo despliegue. No se tocó otro proyecto.

Primera versión 1bdf38b6-ad0d-48cc-ba7b-f158600f7794 y segunda activa c06d3114-c026-43f4-ac4c-2cf928c2556d: SUCCESS. Imagen Linux construida en Railway, Gunicorn nativo y 133 estáticos/397 postprocesados. Configuración y secretos de servidor sin valores expuestos; TLS verify-full, rol jyz_app, esquema/bucket existentes. Sin nuevas migraciones ni usuarios, sin bases/volúmenes Railway adicionales.

HTTP páginas/Admin/estáticos: 401 sin revisión, 200 con revisión; salud DB 200. Veintidós comprobaciones Admin HTTPS aprobadas (login/sesión/permisos/CSRF/crear/editar/publicar/ocultar/PNG/JPEG/WebP/corrupta/logout). Producto sintético nuevo ID 2 termina oculto/de ejemplo, tres fotos nuevas sin borrar objetos; producto 1 no modificado. Cinco verificaciones de persistencia después de nueva versión, incluyendo login/producto y foto firmada cuyo hash coincide.

vibrant-perfection reconsultado: estado, servicios bot-AI/Redis y updatedAt originales sin cambios. Archivo privado acceso-revision.txt (0600) contiene acceso de revisión; no documentos ni chat con claves de servidor. Evidencia detallada evidencia-railway-prueba.md; captura despliegue-confirmado.jpg. Sin instalaciones locales, commit/push, compras por el agente, dominio/DNS, eliminación de recursos Cloudflare o lanzamiento comercial.

Pendientes: revisión humana del remoto y móvil, catálogo/fotos reales, WhatsApp real, compra/configuración de jyzgt.com (solo candidato), costo medido, responsables, respaldo/recuperación y capacitación. Prueba técnica de alojamiento completada; proyecto comercial no completo.

## Ajuste final de configuración Railway

Railway no aplica Config as Code a servicios nuevos desde el 28 de agosto de 2026, según aviso del dashboard y [documentación oficial](https://docs.railway.com/config-as-code/reference). La revisión de los metadatos detectó healthcheck sin ruta y 10 reinicios: railway.json no era efectivo. Se conserva como referencia histórica y se excluye de nuevos paquetes. Se configuró únicamente jyz-web desde su dashboard: /healthz/, timeout 120 segundos, ON_FAILURE con 3 reintentos, una réplica. Tercera versión 455e5314-b271-4371-8244-73c07779f308: SUCCESS. Metadatos del despliegue confirman ruta, timeout y reintentos aplicados; siete comprobaciones HTTP finales aprobadas (salud 200, protección 401 y acceso de revisión/estáticos 200). Evidencia: deployment-health.json y http-health-final.json. No se modifica vibrant-perfection ni se instala software local.

## Revisión de entrega y producto de ejemplo

Cuatro comprobaciones HTTP de solicitudes en Railway aprobadas: mensaje con acentos/destino, revisión previa, referencia excesiva y producto oculto/de ejemplo rechazados. Navegador local: 320/390/1440 sin desbordamiento horizontal, etiquetas correctas, Saltar al contenido enfocado/activado con teclado y seguimiento PRUEBA-ñ1. Evidencia .local/design-review/revision-adaptable.json y capturas móviles; no teléfono físico ni apertura real de WhatsApp. Guía actualizada al acceso Railway.

Usuario confirma que el dueño administrará el panel y autoriza crear un producto de prueba con imagen Unsplash; no tiene productos reales disponibles. ADR 005 registra límites. Producto 3 creado mediante Admin HTTPS limitado, es_ejemplo=True/publicado=True/tallas=[]; foto Fallon Michael, 399222 bytes, hash/fuente/licencia en .local/railway-prueba/producto-demo.json. Perfil Railway protegido mostrará ejemplos identificados sin cotización; otros perfiles mantienen exclusión. Doce pruebas locales afectadas aprobadas; nueva versión en curso, resultado remoto pendiente. Cuenta definitiva del dueño, responsable WhatsApp, contenido real, revisión física/móvil, recuperación y lanzamiento pendientes.

Revisión visual del ejemplo detectó que una sola ficha se expandía a todo el ancho de escritorio; se ajustó la cuadrícula para conservar columnas de tamaño normal. No cambia campos, opciones ni permisos. Verificación final de tamaño/foto pendiente del despliegue de este CSS.

Resultado final del ejemplo: versión 9e9c9ff2-9177-4df1-8593-bdee7dda04cf SUCCESS. Navegador remoto confirma foto cargada y tarjeta de 287 px en escritorio 1440; sin desbordamiento en 320/390/1440. Producto 3 identificado como prueba/no venta, sin enlaces de cotización y rechazo de POST directo verificado. Evidencia demo-http-final.json, demo-browser.json, deployment-demo-final.json y .local/design-review/catalogo-demo-railway.png. Perfil protegido/healthcheck y configuración de reinicios conservados. Guía del dueño actualizada; propuesta de respaldo/recuperación preparada sin ejecutar. Datos/fotos comerciales, cuenta/capacitación, WhatsApp en dispositivo real, recuperación y lanzamiento siguen pendientes; no marcar objetivo completo.

## Revisión del Admin en navegador remoto

Login/logout ejecutados con teclado; ficha 3 abierta sin guardar cambios. Secuencia Tab recorre descripción, categoría, tallas, foto/limpiar, descripción de foto, publicado y orden. Todos los campos de datos tienen etiqueta; botones submit usan su texto como nombre accesible. Anchos 320/390/1440 sin desbordamiento horizontal. Evidencia admin-browser.json y .local/design-review/admin-movil-railway.png. No se editaron productos ni permisos; no sustituye teléfono físico, selector de archivos/errores completos por teclado ni capacitación A12.

## Lectura inicial de consumo Railway

Consulta de solo lectura del proyecto jyz-revision: Usage muestra USD 0.00 actual/estimado redondeados; detalle inicial memoria 0.0003, CPU 0.0000 y egreso 0.0001 USD. Son datos de un servicio recién creado, no una factura ni una previsión mensual válida, y no incluyen Supabase/dominio/otros proyectos. No se cambia plan, presupuesto, alertas ni límites. Evidencia consumo-inicial.json/png y metricas-revision.png. Seguimiento de consumo representativo y presupuesto del dueño sigue pendiente.

## Hoodies y consulta de posibilidades — revisión de Marielos

Instrucción transmitida por el usuario: hoodies en lugar de gorras y una opción para consultar qué se puede personalizar. ADR 006 registrado antes de implementar. No había gorras en la página actual; el catálogo menciona camisetas/hoodies como ideas y añade una tarjeta independiente «¿Qué puedo personalizar?». Enlace al WhatsApp confirmado con consulta preparada sobre prendas/materiales/opciones; no envío automático, sin nuevos pedidos/productos ni escrituras de catálogo. Once pruebas afectadas aprobadas. Versión 6c407cf3-7f60-43af-8653-7ad298ded74b SUCCESS. Navegador remoto: título/texto con hoodies, consulta al +50247233834 codificada correctamente y sin desbordamiento en 320/390/1440. Evidencia consulta-personalizacion.json y captura .local/design-review/hoodies-y-personalizacion-railway.png. Sin apertura/envío del chat, migraciones ni cambios en vibrant-perfection.

## Auditoría de cierre de la etapa autorizada

Última solicitud de Marielos implementada y probada; paquete coincide con los diez archivos esenciales de código/arranque revisados (paquete-vigente.json). No hay despliegue pendiente de esperar: versión 6c407cf3-7f60-43af-8653-7ad298ded74b terminal SUCCESS según evidencia actual. Prueba de alojamiento completada, aceptación comercial A01–A13 incompleta según revision-aceptacion-railway.md.

La siguiente etapa depende de catálogo/fotos comerciales (usuario indicó que aún no los tiene), identidad de acceso del dueño, responsable WhatsApp y comprobación humana en teléfono. Se solicitó usuario deseado/persona de atención y resultado de apertura del chat; no se pide contraseña. La guía y plan de recuperación ya están preparados; restauración remota, cuenta definitiva, dominio/DNS, primer commit/push y lanzamiento requieren alcance/autorización concreta antes de ejecutarlos. Primera constatación de esta dependencia tras agotar la etapa autorizada; meta sigue activa, sin declararla completa ni crear tareas accesorias para prolongarla.

Dependencia de entrega revalidada por segunda continuación: no llegó información nueva del dueño, comprobación humana ni catálogo real. No hay trabajo remoto pendiente de esperar ni otro cambio necesario autorizado que resuelva esos criterios. No se repiten pruebas ni se amplía el alcance; meta activa, aceptación comercial incompleta.

## Dependencia humana confirmada — objetivo bloqueado

Tercera continuación consecutiva con la misma dependencia sin resolver. Prueba de alojamiento y cambios autorizados completos; no hay proceso de despliegue activo que esperar ni otro cambio autorizado que resuelva aceptación comercial. Faltan usuario del dueño/responsable WhatsApp, comprobación humana en teléfono y catálogo/fotos reales; acceso definitivo, recuperación/dominio/lanzamiento requieren definir y autorizar sus pasos. El objetivo se marca bloqueado, no completo. Retomar al recibir datos, resultado de revisión o una nueva instrucción concreta. Conservar web protegida, código, evidencia y recursos; vibrant-perfection permanece fuera del alcance.

Dominio: el usuario decide conservar por ahora jyz-web-production.up.railway.app; pospone la compra de dominio propio al 9 de octubre o cuando la confirme. Dominio propio no bloquea usar la web funcional en Railway. No comprar ni cambiar DNS.

## Optimización automática de fotos autorizada

«Si procede» autoriza implementar propuesta WebP, ADR 007 registrado. Backend valida antes de HTTP, corrige EXIF, reduce proporcionalmente a 1600 px, codifica WebP calidad 80/transparencia, elimina metadatos y limita salida a 500 KiB con reducción adicional. Animaciones rechazadas. Ruta nueva UUID, fotos anteriores/originales preservadas. Ayuda del panel/guía actualizadas. Suite local actual: 43 pruebas aprobadas, con orientación, transparencia, peso, fallo de codificación sin subida y rollback del Admin. Sin instalación local, migraciones ni cambios en vibrant-perfection. Build/verificación remota de esta versión pendientes.


## Cierre de optimización WebP — 8 de octubre

Despliegue 9a8d78bc-2b1a-4e75-b31a-949c6b31503e SUCCESS. Prueba real por HTTPS Admin con producto de ejemplo 3: entrada JPEG 399222 bytes; salida WebP 49098 bytes, 1600 × 1067 px, sin EXIF (87,7 % de reducción en esta imagen). Storage privado y URL firmada sirven image/webp; objeto anterior conservado y reemplazo inválido conserva referencia válida. Evidencia: .local/railway-prueba/webp-http.json y deployment-webp.json. Suite local: 43 pruebas aprobadas. Ver ADR 007. Sin migraciones, nuevas instalaciones, conversión masiva, commit/push ni cambios en vibrant-perfection. Revisión visual nueva de esta versión no ejecutada; aceptación comercial y entrega del dueño siguen pendientes.

Dominio vigente por instrucción del usuario: jyz-web-production.up.railway.app. Puede usarse para la web funcional; compra y configuración de dominio propio quedan aplazadas hasta una nueva confirmación del usuario.

Auditoría posterior: criterios A05/A11 actualizados con evidencia WebP y A13 con dominio Railway aprobado. La optimización está completada; el objetivo de entrega comercial conserva los pendientes humanos de cuenta/capacitación del dueño, WhatsApp en teléfono, contenido real y recuperación/aprobación final. El turno anterior aportó progreso documental; no hay despliegue pendiente confirmado ni se declara completada la entrega.

Revalidación de entrega tras WebP: segunda constatación consecutiva de los mismos pendientes humanos, sin nueva respuesta del negocio. La revisión del plan de recuperación confirma que faltan destino/responsable y autorización específica de exportación/restauración. No hay trabajo remoto autorizado que resuelva estos puntos; no se ejecutan cambios ni se repiten pruebas. Esta continuación no aporta avance funcional y la meta permanece activa, sin declarar lanzamiento completo.

## Entrega bloqueada tras cierre WebP

Tercera continuación consecutiva confirma los mismos pendientes humanos sin nueva respuesta: identidad de acceso/capacitación del dueño, responsable WhatsApp, comprobación en teléfono, catálogo/fotos reales y destino/autorización de recuperación. El turno anterior fue sin progreso funcional; registrar el estado no resuelve estos criterios. La etapa técnica y optimización están verificadas; entrega comercial incompleta. Se marca el objetivo bloqueado hasta recibir datos o autorización concreta. Se conserva revisión protegida en el dominio Railway aprobado; vibrant-perfection permanece intacto.

## Cuenta danilo autorizada y verificada

El usuario confirmó crear la cuenta danilo tras comprobar su ausencia en la base usada por Railway. Se creó activa y staff, sin superusuario, con el grupo existente Responsable de catálogo (ver/agregar/editar; sin borrar ni gestionar usuarios). Login HTTPS, listado/agregar, restricción de usuarios y logout verificados. Evidencia sin contraseña: .local/railway-prueba/acceso-danilo-verificacion.json. Credencial guardada exclusivamente en archivo privado local con modo 0600, excluido de Git. No se modificaron productos, migraciones ni vibrant-perfection. Cuenta de Danilo no demuestra entrega/capacitación del dueño; esos criterios siguen pendientes.

## Personalización del Admin autorizada — ADR 008

«Procede» autoriza la propuesta del panel y solicita explicar pendientes para presentar sitio funcional. Identidad JYZ, miniaturas, estados y cuatro grupos de edición implementados, sin migraciones/dependencias. 43 pruebas existentes pasan y check sin problemas. Navegador local: fotos cargadas y sin desbordamiento de página en lista/ficha 320/390; tabla con desplazamiento interno. Capturas admin-jyz-lista.png, admin-jyz-edicion.png y admin-jyz-edicion-movil.png en .local/design-review. Despliegue protegido Railway en curso. Aprobación visual pendiente, lanzamiento público no ejecutado. Plan concreto en presentacion-funcional.md; ejemplos conservados y vibrant-perfection intacto.

## Panel JYZ desplegado y comprobado

Versión final a8450427-575e-47cf-8e48-8431a305ee23 SUCCESS en jyz-revision/jyz-web. Once comprobaciones HTTPS aprobadas: salud, protección de revisión, título JYZ, CSS vigente (normalizando hashes de fuentes de collectstatic), fuente local, login, portada, lista/estados, edición agrupada, usuarios restringidos y logout. Evidencia .local/railway-prueba/deployment-admin-jyz.json y admin-jyz-http.json; script reproducible scripts/railway_admin_design_probe.py. Sin cambios de productos, permisos o recursos ajenos; vibrant-perfection intacto. Las capturas corresponden a navegador local con los mismos archivos, no a revisión visual remota.

La tarea de personalizar el panel y explicar pendientes está completada técnicamente. Revisión visual humana aún pendiente; no se retiró Basic/noindex ni se publicó comercialmente. Plan de presentación/limpieza en presentacion-funcional.md. Requisitos de entrega del negocio siguen abiertos y no se confunden con esta tarea concreta.

## Footer e Instagram solicitados

Logo recibido incorporado al footer y enlace confirmado directamente https://www.instagram.com/_.j.y.z._/ (pestaña nueva, noopener/noreferrer). Sustituye candidato del PDF para implementación; historial preservado. Navegador local: logo cargado y sin desbordamiento 320/390 px; capturas footer-jyz-instagram.png y footer-jyz-instagram-movil.png. Check aprobado. Despliegue protegido en curso; no se modifica catálogo ni se cargan fotos de galería. Galería sigue pendiente de trabajos reales, permiso de uso y descripciones; módulo independiente de edición no incluido en el Admin actual.

Footer desplegado: 166e41aa-f167-4434-8e91-484cc71948c2 SUCCESS. Seis comprobaciones HTTPS aprobadas: página, Instagram exacto, nueva pestaña segura, logo en footer, archivo del logo y CSS nuevo. Evidencia .local/railway-prueba/deployment-footer.json y footer-http.json; capturas visuales locales. Sin migraciones, datos editados, nuevos recursos, commit/push ni cambios en vibrant-perfection.

## Galería de referencia Pexels autorizada y desplegada

Usuario solicita fotos de prueba, principalmente playeras y gorras. Tres fotos: dos playeras y una gorra; licencia Pexels consultada y páginas/autores/hashes registrados en catalogo/static/catalogo/galeria-referencias/procedencia.json. Cada foto marcada Referencia de prueba, crédito/enlace de origen y aviso No son trabajos realizados por JYZ. Copias WebP 15248/57968/38702 bytes (111918 bytes total), originales de descarga conservados localmente. No representan productos ofertados ni portafolio real.

Versión 13de94b7-21f1-4a5c-92ef-4d9445f33067 SUCCESS. Seis comprobaciones HTTPS: página, aviso, tres etiquetas, créditos, tres fotos y bytes/MIME de archivos coincidentes con fuente. Evidencia .local/railway-prueba/deployment-galeria.json y galeria-http.json. Navegador local: tres fotos cargadas; sin desbordamiento 320/390; capturas galeria-pexels.png y galeria-pexels-movil.png. Check aprobado. No hay módulo de galería en Admin, nuevas instalaciones/migraciones ni escrituras de catálogo; revisión protegida conservada, vibrant-perfection intacto. Para versión comercial siguen pendientes trabajos propios autorizados y revisión humana.

## Catálogo centrado y propuesta de varias fotos

Usuario aprueba corregir distribución y solicita pensar opción para varias fotos. Encabezado centrado; cuadrícula auto-fit de fichas hasta 360 px, máximo 1240 px; consulta general fuera de la cuadrícula, franja debajo. Mejorado contraste de ayudas sobre fondo claro. Check y 21 pruebas de catálogo aprobadas. Navegador local con producto remoto de ejemplo: ficha centrada (360 px), sin desbordamiento 320/390; escenarios 0/3 renderizados sin escribir en base remota también sin desbordamiento de página en escritorio. Capturas catalogo-centrado.png y consulta-personalizacion-franja.png.

Versión da83999c-9b9b-4b80-946b-d31c0b802c24 SUCCESS. Seis comprobaciones HTTPS aprobadas: página, consulta independiente, encabezado centrado, identificación del ejemplo, CSS vigente y WhatsApp conservado. Evidencia .local/railway-prueba/deployment-catalogo-layout.json y catalogo-layout-http.json. No se modifican catálogo, recursos ajenos, migraciones, permisos ni protección de revisión. vibrant-perfection intacto.

ADR 009 es propuesta pendiente: portada en catálogo, ficha con miniaturas y hasta seis fotos sugeridas; administración inline/orden/portada, Storage/WebP y compatibilidad con foto actual. No se implementa todavía ni se aplica migración remota. Siguiente paso: revisar distribución y decidir si aprobar ampliación de fotos antes de preparar paquete de datos/permisos.

## Contacto trasladado al footer — ADR 010

Instrucción directa del usuario: eliminar toda la sección «Sigamos en contacto» y trasladar WhatsApp al footer. Se retiraron título, texto, formulario de referencia y vista previa; la vista pública ya no procesa seguimiento. Footer conserva logo e Instagram y añade WhatsApp +502 4723 3834. Navegación «Contacto» apunta al footer. R05/R06/R09 y A09/A10 actualizados; historial del recorrido anterior preservado.

21 pruebas del catálogo aprobadas. Navegador local: contacto visible, sin desbordamiento en escritorio y 390 px; capturas .local/design-review/contacto-footer.png y contacto-footer-movil.png. Railway 5e67421f-4990-4217-bab6-cf9f04bf8887 SUCCESS; seis comprobaciones HTTPS aprobadas, evidencia .local/railway-prueba/contacto-footer-http.json y deployment-contacto-footer.json. Capturas corresponden a versión local; contenido remoto verificado por HTTP. Sin migraciones, escrituras de datos, nuevas instalaciones, commit/push ni cambios en vibrant-perfection; revisión protegida conservada. Apertura humana de WhatsApp y aceptación comercial siguen pendientes. ADR 009 (varias fotos) continúa como propuesta sin implementar.

## Fichas de producto y fotos múltiples — preparación local

Usuario aprueba ficha propia, miniaturas y «Quiero este producto». ADR 009 pasa a implementación local aprobada; paquete remoto requiere autorización específica. Código y dos migraciones preparados, sin aplicar en Supabase. 51 pruebas aprobadas en SQLite y PostgreSQL local; check y ausencia de migraciones faltantes verificados. Navegador local: cambio de miniatura, cantidades M/L y mensaje correcto, sin desbordamiento de página en escritorio/390 px. Demo aislada en 8002, fotos Pexels repetidas exclusivamente para prueba de seis imágenes; no son productos reales. Capturas ficha-producto.png / ficha-producto-movil.png. Guía y paquete concreto en fichas-y-fotos-multiples.md; archivos de código preparados en el staging local de Railway, aún no desplegados.

Inspección MCP autenticado de solo lectura: tres productos/tres fotos previas; portada/tabla de fotos no aplicadas. Privilegios por defecto existentes cubren tablas/secuencias del migrador. Sin cambios remotos, datos, nuevas instalaciones, commit/push ni intervención en vibrant-perfection. Objetivo continúa pendiente de aplicación remota autorizada, HTTPS y revisión humana. La web Railway sigue en versión 5e67421f-4990-4217-bab6-cf9f04bf8887 con footer actualizado, sin esta ampliación.

Verificación adicional: ocho pruebas nuevas, 51 totales aprobadas en SQLite y PostgreSQL. Carga múltiple parcialmente fallida revierte cambios y registra el archivo subido sin referencia, sin borrarlo. Navegador: miniatura activada con Enter cambia foto/estado. Siete comprobaciones HTTP del Admin local: inline, sin borrado, selector de portada, usuarios 403, guardar portada/reflejo en ficha/restauración; evidencia .local/producto-demo/admin-http.json. Servidor demo local activo en 8002.

## Confirmación remota pendiente — segunda constatación

La continuación no contiene aprobación nueva del paquete remoto presentado. Relectura de ADR 009 y del paquete confirma la misma dependencia; no se aplica migración, permisos ni despliegue. La implementación y pruebas locales ya están terminadas, y no hay otro trabajo autorizado necesario que resuelva la dependencia. Se presenta la confirmación específica en el chat; objetivo activo, sin declarar completada la versión remota. Esta constatación no representa progreso funcional.

## Paquete de fichas bloqueado por confirmación remota

Tercera constatación consecutiva de la misma dependencia: no llegó confirmación específica de migraciones, permisos de imágenes y despliegue del paquete presentado. El turno anterior fue sin progreso funcional; no hay proceso remoto en ejecución ni trabajo local necesario pendiente que resuelva esa autorización. Se marca el objetivo bloqueado, no completado. Código, documentación y evidencia quedan preparados; retomar al recibir la aprobación. No se aplican cambios remotos ni se interviene vibrant-perfection.

## Paquete remoto de fichas autorizado

El usuario responde «autorizo» a la confirmación específica de las dos migraciones en Supabase, permisos de fotos y despliegue protegido JYZ. Se retoma el objetivo. Plan remoto confirma únicamente catalogo.0002 y 0003; preservar referencias/bytes anteriores y verificar antes del despliegue. vibrant-perfection fuera de alcance.

## Fichas y fotos múltiples completadas técnicamente

Con autorización específica del usuario, se aplicaron catalogo.0002/0003 en jyz_prueba, proyecto Supabase kcahxuvfmrzxzlnpezyf. Tres referencias/fotos anteriores conservadas, comprobadas por SHA-256 de bytes; tres productos, tres imágenes. Rol de catálogo: ver/agregar/cambiar productos/fotos, sin borrado/usuarios, danilo limitado. Railway fbda1822-3da5-4f22-b1a7-827aa344600a SUCCESS; 17 comprobaciones HTTPS aprobadas mediante scripts/railway_fichas_probe.py. Evidencia fichas-migracion.json, fichas-http.json y deployment-fichas.json en .local/railway-prueba. 51 pruebas locales SQLite/PostgreSQL aprobadas en la preparación.

Catálogo enlaza fichas; productos reales publicados permiten «Quiero este producto» y cantidades/opciones para preparar WhatsApp. Ejemplos actuales siguen sin compra/cotización; ocultos 404. Miniaturas/portada, seis fotos y recorrido comercial verificados localmente sin convertir ejemplos remotos en reales. Captura ficha-producto-actual.png local con datos actuales Supabase; navegador remoto bloqueado por Basic, HTTP autenticado sí verificado. No nuevos productos/subidas, compras/DNS, commit/push ni cambios en vibrant-perfection. Objetivo de esta ampliación completado; revisión humana y lanzamiento comercial mantienen sus pendientes propios.

## Producto cotizable de prueba solicitado — ADR 011

El usuario solicita un producto «real» para probar la ficha en producción. Se crea producto 4 «Playera de prueba · cotización por WhatsApp», publicado/es_ejemplo=False para habilitar el flujo, con nombre/categoría/descripción explícitos de prueba y sin oferta comercial. No se reciben datos comerciales reales. Se conserva intacto el ejemplo 3; referencia existente Fallon Michael/Unsplash reutilizada y portada relacionada, sin copiar/subir/modificar archivos. Sin precio ni tallas inventadas.

Nueve comprobaciones HTTPS aprobadas: catálogo/ficha, botón, identificación de prueba, formulario, preparación de mensaje, nombre/destino y opciones por consultar. Evidencia .local/railway-prueba/producto-cotizable-prueba.json y producto-cotizable-http.json. Captura producto-cotizable-prueba.png local con datos Supabase/código vigente. No se abrió/envió WhatsApp, no se crean pedidos, migraciones, permisos, nuevos despliegues, commit/push ni cambios en vibrant-perfection. Antes de lanzamiento comercial ocultar esta ficha o sustituir contenido por datos/fotos reales confirmados. El frontend actual permite probar el recorrido por HTTPS en /productos/4/.

## Campo de colores retirado — ADR 012

Usuario solicita quitar «Número de colores de impresión». Retirado del formulario compartido en inicio/ficha y del mensaje de WhatsApp, incluso si un POST antiguo incluye colores. Cantidades/tallas y confirmación del negocio conservadas. 29 pruebas del catálogo aprobadas. Railway 50b152d2-dbef-4b2f-919f-bad9881286ac SUCCESS; cuatro comprobaciones HTTPS de inicio/ficha, mensaje sin colores y destino correcto. Evidencia .local/railway-prueba/deployment-sin-colores.json y cotizacion-sin-colores-http.json. Captura local cotizacion-sin-colores.png; demo 8002 reiniciada con formulario nuevo. Sin migraciones, datos, permisos, instalaciones, commit/push ni cambios en vibrant-perfection.

## Idea libre en cotización — ADR 013

Usuario solicita que «Cuéntanos tu idea» tenga un campo para escribir la idea y armar mensaje formateado para WhatsApp. Nuevo `IdeaForm` (catalogo/solicitudes.py), acción `idea` en la vista de inicio y formulario en la sección #cotizacion; la cotización por producto se mantiene. 30 pruebas del catálogo aprobadas localmente (nueva prueba de idea libre). Recorrido verificado en demo local 8002: formulario visible y mensaje preparado. Pendiente: desplegar en Railway y verificar por HTTPS. Sin migraciones, datos, commit/push ni cambios en vibrant-perfection.

Ampliación ADR 013: campo opcional «¿Para cuándo lo necesitas?» (fecha, no pasada; mensaje «*Para el:* dd/mm/aaaa»), recomendado y aceptado por el usuario. No se agregó técnica (la define JYZ). 30 pruebas aprobadas; demo 8002 reiniciada y campo verificado visualmente.

Despliegue ADR 013 (autorizado por el usuario: «si»): `railway up` al servicio jyz-web del proyecto jyz-revision, «Deploy complete», imagen sha256:d456dc1e…. Nueve comprobaciones HTTPS aprobadas en jyz-web-production: formulario de idea, textarea, campo de fecha, POST con mensaje preparado, «*Para el:* 24/12/2099», destino wa.me correcto, /productos/4/ 200. Evidencia .local/railway-prueba/idea-libre-http.json. No se abrió ni envió WhatsApp. Sin migraciones, datos, commit/push ni cambios en vibrant-perfection.

## Páginas públicas sin clave — ADR 014

Usuario aprueba («Si, procede») quitar la clave de revisión en páginas públicas y mantenerla en /admin/. ReviewAccessMiddleware protege solo /admin y /static/admin/. 39 pruebas config.tests_railway + catalogo aprobadas (config.tests_runtime sigue sin poder importarse localmente por falta de httpx, ya documentado). `railway up` a jyz-web: «Deploy complete», imagen sha256:45d34ada…. HTTPS sin clave: /, /inicio/, /productos/4/ y CSS público 200; /admin/, /admin/login/ y CSS admin 401; con clave /admin/login/ 200; noindex en todo; formulario de idea operativo. Evidencia .local/railway-prueba/publico-sin-clave-http.txt. Pendiente antes del lanzamiento: quitar aviso de revisión, ejemplos, producto 4 y fotos de referencia; dominio/DNS. Sin migraciones, datos, commit/push ni cambios en vibrant-perfection.

## Raíz muestra el inicio — ADR 015

`/` ahora sirve inicio; `/inicio/` alias; catálogo técnico movido a `/catalogo/` (protegido con clave en Railway). 40 pruebas config.tests_railway + catalogo aprobadas. `railway up` «Deploy complete», imagen sha256:bf5d2e30…. HTTPS: / 200 (inicio, formulario con action /#cotizacion), /inicio/ 200, /productos/4/ 200, /catalogo/ 401, /admin/login/ 401. Evidencia .local/railway-prueba/raiz-inicio-http.txt. Sin migraciones, datos, commit/push ni cambios en vibrant-perfection.

## Íconos iguales en Safari iOS

Usuario reporta que Safari en iPhone mostraba ↗ y ✳ como emoji. U+FE0E probado en simulador iPhone 17 Pro (iOS 26) y descartado (mostraba «?»). Se reemplazan ↗ ↑ ← ✳ en inicio, ficha y footer por `<span class="ico ico-*">` con máscara SVG en línea (color heredado), CSS en inicio.css y producto.css. 31 pruebas del catálogo aprobadas. Verificado en Safari del simulador (local y producción) y en Chromium. `railway up` «Deploy complete», imagen sha256:e9e8c386…; HTML de producción sin los caracteres anteriores y CSS con hash nuevo. Sin migraciones, datos, commit/push ni cambios en vibrant-perfection.

## Facebook y revisión para usuario final

Facebook añadido al footer de inicio/fichas con URL limpia del perfil confirmado ID 61595434880342, nueva pestaña segura. Verificado en HTML y navegador remoto de la versión actual bb8a8e82-70aa-47cd-a02f-fdb39cd84984 SUCCESS. Captura footer-facebook-remoto.png. Las versiones posteriores también incorporan ADR 013/014/015 e iconos SVG; no se revierte ese trabajo.

Auditoría read-only solicitada: páginas públicas accesibles sin clave, raíz correcta, imágenes cargadas, ideas y ficha cotizable preparan mensajes en navegador remoto a 390 px sin desbordamiento, sin abrir/enviar WhatsApp. Persisten aviso/noindex, producto 4 de prueba y galería Pexels; falta contenido comercial, validación humana en teléfono, acceso/capacitación del dueño y recuperación. Evidencia HTTP en auditoria-lanzamiento-http.json y auditoria-acceso-anonimo.json; informe docs/plan/auditoria-usuario-final.md. Plan de presentación corregido para no repetir pendientes de raíz/Basic ya resueltos. Sin nuevas escrituras de datos, configuración, compras, commit/push ni cambios en vibrant-perfection durante auditoría.

## Fotografías reales recibidas — 8 de octubre

El usuario entrega tres fotos en `/Users/danilo/Documents/fotos galeria jyz` y solicita reemplazar referencias por fotos reales. Se preservan originales en `assets/jyz-fotos-recibidas/`; copias WebP en `catalogo/static/catalogo/galeria-jyz/` (719×1600, 719×760 y 899×1177 px; 152408, 69376 y 77788 bytes), sin recorte ni ampliación. Galería sustituye Pexels por las tres prendas fotografiadas, con descripciones visuales sin afirmar técnica, tallas, precio o disponibilidad. Fotos antiguas conservadas.

Dos retoques IA integrados revisados y descartados por reconstruir detalles del diseño; originales optimizados elegidos. Modelo GPT Images 2.5 no seleccionable/verificado. Pendiente aclaración del usuario: solo galería o también fichas cotizables. Producto 4 conserva su identificación de prueba; no se convierten datos sintéticos en reales por recibir fotografías.

Verificación local: inicio 200 y tres recursos resueltos en la base de demo ya migrada; sin Pexels ni avisos de referencia dentro de la galería. La primera comprobación usó una base SQLite antigua sin columna portada; se corrigió el destino a la demo vigente, sin migrar bases remotas. Despliegue limitado a jyz-web/jyz-revision solicitado como sustitución de fotos de la web; resultado HTTPS pendiente. Sin modificaciones PostgreSQL/Storage, migraciones, commit/push, instalaciones ni intervención en vibrant-perfection.

Resultado final: Railway 7e7b400b-8474-4bcf-aaaf-39f636aed570 completó despliegue. Nueve comprobaciones HTTPS aprobadas: inicio/alias/ficha/healthz 200, Admin/catálogo técnico 401, tres WebP 200 y MIME correcto. Galería real visible en navegador; ancho móvil 390 sin desbordamiento. 40 pruebas catalogo + config.tests_railway aprobadas. Captura .local/design-review/galeria-real-jyz.png y evidencia .local/railway-prueba/galeria-real-http.json.

Incidencia corregida: primer paquete 2891655d-dcf3-47eb-9fcf-8e416febefea tenía archivos antiguos y devolvió 401 en páginas públicas. Se sincronizaron los archivos existentes del paquete con el código vigente y redesplegó. Verificación final confirma acceso público y rutas correctas de ADR 014/015; no se alteraron credenciales ni protecciones acordadas. Antes de futuras subidas comparar todo el paquete con la fuente vigente, no solo los archivos del cambio.

Pendiente: respuesta sobre publicar estas prendas como fichas cotizables; no se realizaron escrituras de catálogo/Storage. Los pendientes comerciales restantes de la auditoría conservan su estado.

## Galería administrable — ADR 016

Usuario aprueba «Si procede» el módulo Galería. Código, migración aditiva 0004, seeder inicial, rol acotado, Admin y consulta pública preparados y verificados localmente. Subir/editar títulos y descripciones/ordenar/mostrar u ocultar; originales preservados, sin modificar productos. Sección/enlace omitidos cuando no hay fotos visibles. Conversión WebP del backend existente, errores revierten edición. 61 pruebas SQLite aprobadas; navegador confirma título/orden/ocultación desde Admin reflejados en inicio y restauración. Captura .local/design-review/galeria-admin-local.png.

MCP OAuth solo lectura confirma cuatro productos/cuatro fotos, tabla de galería ausente y política/privilegios actuales. Docker apagado: PostgreSQL local no ejecutado; SQL PostgreSQL generado sin conexión y marcado revisión. Aplicación remota pendiente: una migración, RLS/política de tabla nueva, tres permisos al rol de catálogo, tres cargas/registros iniciales y despliegue JYZ. Paquete concreto en docs/plan/galeria-administrable.md; staging separado .local/railway-galeria, no subido. Sin compras, instalaciones, escrituras remotas, commit/push ni cambios en vibrant-perfection. Objetivo sigue activo hasta autorización y verificación HTTPS.

## Verificación remota de galería preparada

Continúa pendiente la respuesta a la confirmación específica del paquete remoto. Se preparó scripts/railway_galeria_probe.py: acceso público/protecciones, tres fotos privadas WebP con límites, sesión del editor, formularios, lista editable y rechazo de borrado/usuarios. Compilación Python aprobada. No se ejecutó contra remoto porque la tabla/rol/versión nueva todavía no se aplicaron; esta preparación no es evidencia HTTPS. El script no cambia fotos/textos/datos, solo inicia/cierra sesión y registra resultados sin URLs firmadas/credenciales. Edición remota y preservación de fotos anteriores requieren comprobación separada tras autorización. Sin migración, cargas, despliegue, commit/push ni cambios en vibrant-perfection.

## Objetivo de galería bloqueado por autorización remota

Tercera constatación consecutiva de la misma dependencia: no se recibió respuesta a la confirmación específica de migración, permisos, tres cargas iniciales y despliegue JYZ. Implementación local, pruebas (61 aprobadas), captura, SQL y comprobador HTTPS ya preparados; archivos y staging revalidados. No hay proceso remoto de aplicación iniciado ni trabajo local necesario que resuelva la autorización. Se marca el objetivo bloqueado, no completado. Retomar al recibir aprobación del paquete documentado en galeria-administrable.md. Sin escrituras remotas ni cambios en vibrant-perfection.

## Paquete remoto de galería autorizado

El usuario responde «autorizo» a la confirmación del paquete: catalogo.0004, RLS/política y permisos acotados de galería, tres fotos/registros iniciales y despliegue exclusivo JYZ. Se retoma el objetivo previamente bloqueado. Plan migrate verifica únicamente CreateModel GaleriaImagen. Snapshot remoto previo: cuatro productos/cuatro imágenes, tres objetos con hashes y seis permisos del grupo; preservar contenido y bytes. Ninguna autorización para borrar, comprar, commit/push o intervenir vibrant-perfection.

## Resultado remoto verificado — 8 octubre 2026

El usuario autorizó expresamente el paquete remoto con «autorizo». Railway despliegue `324fc0e1-108a-4519-b15e-1c5e1a120208`, estado SUCCESS, exclusivamente jyz-web/jyz-revision. La sección pública ahora consulta la galería administrable; tres fotos reales recibidas cargadas al Storage privado de Supabase. No se modificaron productos ni se sustituyeron diseños con IA.

- Migración catalogo.0004 aplicada en jyz_prueba mediante jyz_migrator: una tabla nueva. RLS activado, política exclusiva jyz_app y DELETE revocado. El primer intento de ejecutar el SQL de permisos falló por separar comentarios con punto y coma; la transacción se revirtió y se corrigió el lector de comentarios antes de aplicarlo con éxito.
- Grupo Responsable de catálogo conserva sus seis permisos y añade tres de galería: ver/agregar/cambiar. Admin rechaza borrado y administración de usuarios del editor. No se cambiaron cuentas ni contraseñas.
- Tres fotos privadas cargadas y leídas realmente: WebP, 719×1600 / 719×760 / 899×1177 px, 131320 / 58726 / 65016 bytes. Originales conservados. El seeder demuestra carga real mediante el backend; formulario de alta y edición verificados por HTTPS. La carga de archivos mediante formulario Admin está probada localmente y el backend compartido anteriormente por HTTPS; esta sesión no añadió ni reemplazó fotos mediante el formulario remoto.
- 27 comprobaciones HTTPS de lectura/sesión aprobadas; inicio/alias/ficha/healthz 200, Admin y catálogo técnico requieren acceso de revisión. Tres fotos firmadas con MIME image/webp y límites correctos; sesión del editor, módulo/lista/formularios/vistas previas y permisos negativos aprobados.
- Cuatro comprobaciones HTTPS adicionales: título reflejado, orden reflejado, ocultación reflejada y restauración. Se guardaron temporalmente título/orden/visibilidad desde el Admin; valores iniciales restaurados al terminar. Sin enviar WhatsApp.
- Conservación posterior al despliegue: cuatro productos y cuatro imágenes iguales al snapshot previo, tres objetos antiguos con SHA-256 idéntico y las tres fotos de galería con bytes/referencias y valores originales conservados. 61 pruebas locales aprobadas en la etapa previa; no se repitieron ni se presentan como pruebas PostgreSQL locales.
- Navegador confirma fotos/títulos actuales en la sección publicada. Captura `.local/design-review/galeria-admin-publica-remota.png`. Evidencias privadas sin credenciales ni URLs firmadas: `.local/railway-prueba/galeria-admin-http.json`, `galeria-edicion-http.json`, `galeria-remota.json`, `galeria-preservacion-final.json` y `deployment-galeria-admin.json`.

Administración: https://jyz-web-production.up.railway.app/admin/catalogo/galeriaimagen/ . Subir o reemplazar foto, editar título/descripción, ordenar y mostrar/ocultar; cambios reflejados en inicio. Si no quedan fotos visibles, se omiten sección y enlace Trabajos. El encabezado/introducción de la sección siguen definidos en plantilla, no como campos editables de la galería.

Pendientes ajenos a esta entrega: práctica y acceso definitivo del dueño (A12), revisión humana de fotos en teléfono, definición del catálogo comercial y recuperación. La web conserva aviso de revisión/noindex y el producto de prueba. Sin compras, instalaciones, borrado, commit/push, DNS ni cambios en vibrant-perfection.

## Responsables y usuario solicitado — confirmación del usuario

Fecha: 8 de octubre de 2026. Fuente: respuesta enviada por el usuario en este chat; sustituye el pendiente de nombres y responsables de WhatsApp, sin modificar el historial del PDF.

- Nombres recibidos en respuesta a «Nombre del dueño»: Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid. Registrar como responsables indicados; no inferir representación legal ni porcentajes de propiedad.
- Usuario solicitado para el panel: `Mryoan`, respetando mayúsculas. La respuesta no asigna expresamente esta cuenta a una persona concreta ni autoriza compartir contraseñas.
- Atención de WhatsApp: Yohann Alexandrey Ordoñez, Joel Alexander Rodriguez y Juan Manuel González Del Cid. Número confirmado previamente: +502 47233834. Horarios y prueba humana de apertura/atención siguen pendientes.
- Acceso definitivo: nombre de usuario definido; creación, asociación a su titular, entrega segura y capacitación pendientes. Perfil previsto: Responsable de catálogo (ver/agregar/cambiar productos, imágenes y galería; sin borrar ni gestionar usuarios), siguiendo las decisiones existentes. La cuenta `danilo` es independiente y se conserva.

Esta actualización registra información en documentación local. No crea ni modifica cuentas, contraseñas, permisos, bases externas, web pública o despliegues. Los nombres no se añaden automáticamente a la página pública. No se reciben fichas comerciales, tallas, precios ni horarios nuevos.

## Entrega operativa autorizada — ADR 017

El usuario difiere el catálogo real hasta recibir el sitio y autoriza avanzar con el resto: cuenta Mryoan acotada, ocultación de fichas sintéticas conservando datos/fotos, revisión técnica móvil, respaldo cifrado y recuperación PostgreSQL local aislada, guía y despliegue público sin avisos/noindex de revisión. Catálogo comercial deja de ser requisito previo de esta entrega. No se asumen realizadas capacitación humana ni prueba en teléfono físico; se registrará evidencia técnica y lo pendiente del negocio. No compra, DNS, borrados, commit/push ni cambios en vibrant-perfection necesarios.

## Entrega operativa ejecutada — ADR 017

Fecha: 8 de octubre de 2026. Usuario autorizó continuar y decidió cargar catálogo real después de recibir el sitio.

- Cuenta Mryoan creada activa/staff, sin superusuario, con los nueve permisos del grupo Responsable de catálogo. Login HTTPS, productos/galería, cambio de contraseña disponible, rechazo de usuarios y borrado, logout verificados. Danilo conservado; contraseña inicial en archivo privado local 0600, no enviada ni publicada. Asociación individual y entrega de acceso al negocio por Danilo pendientes.
- Cuatro fichas sintéticas ocultas mediante actualización exclusivamente de publicado; no se borraron registros, fotos ni migraciones. Ficha 4 devuelve 404 anónima. Inicio muestra estado vacío y consulta de idea; galería de tres fotos reales conservada.
- Publicación Railway 983790d0-61ff-4cd6-a9ee-4e64b55ac649 SUCCESS, solo jyz-web/jyz-revision. JYZ_PUBLIC_LAUNCH=1, ejemplos excluidos. Avisos/noindex retirados de páginas públicas exitosas GET/HEAD; Admin/rutas técnicas y POST/errores conservan noindex/no-store, Basic y sesión Django. robots.txt/sitemap.xml publicados sin fichas ocultas; descripción de inicio preparada con datos confirmados. No garantiza indexación inmediata.
- 65 pruebas locales aprobadas, check sin incidencias y makemigrations --check sin cambios. 23 comprobaciones HTTPS aprobadas: páginas/datos, fotos privadas WebP, catálogo vacío, fichas ocultas, permisos/CSRF, mensaje preparado y perfil Mryoan. Evidencia .local/entrega-jyz/tests-publicacion.txt y entrega-https.json.
- Navegador remoto: ancho 390/contenido 375 y ancho 320/contenido 305; sin desbordamiento, fotos cargadas y formulario genera mensaje legible. Apertura de enlace WhatsApp confirmó destino +50247233834 y perfil visible «Juan Gonzalez», mensaje correcto y sin enviar. Capturas entrega-inicio-390.png, entrega-inicio-320.png, entrega-galeria-390.png y entrega-whatsapp-destino.png, en .local/design-review.
- El usuario respondió «Lo revisé en el teléfono y funciona» a la prueba física de galería/apertura WhatsApp: revisión humana confirmada. No afirmar recepción de mensajes, disponibilidad de atención ni prueba de todos los modelos de teléfono.
- Respaldo lógico real de 13 tablas, 15 objetos Storage y originales; cifrado/descifrado y hashes verificados. Recuperación en PostgreSQL 17 local aislado, conteos iguales, Mryoan restaurado/login/permisos/página y tres fotos WebP leídos. Rol de origen/TLS limitados; nunca se restauró sobre remoto. Contenedor detenido al terminar y temporales propios sin cifrar limpiados. Evidencia privada respaldo-recuperacion.json; copia cifrada fuera del repositorio, clave separada. No hay respaldos periódicos automatizados ni copia fuera de este equipo realizada.

Guía [entrega operativa](../entrega/entrega-operativa.md) y guía de catálogo actualizadas. Catálogo comercial y práctica con nuevos productos corresponden al negocio después de la entrega; se conserva el procedimiento A12. Práctica de galería del responsable consultada, todavía sin confirmación al registrar esta entrada. Presupuesto/consumo representativo, custodia externa del respaldo y evidencia de revocación de la clave anterior permanecen como asuntos operativos, sin afirmar que están resueltos. No compras, DNS, commit/push ni intervención en vibrant-perfection.

## Confirmación humana de entrega

El usuario confirmó «Lo revisé en el teléfono y funciona» para galería y apertura de WhatsApp, y «Sí, entró y completó la práctica» para acceso Mryoan, ordenar, ocultar y volver a mostrar una foto desde Galería con comprobación pública. La entrega/práctica inicial del panel quedan confirmadas por la persona, además de las pruebas técnicas. No divulgar credenciales. La práctica específica con productos comerciales se realizará al cargar el catálogo, diferido expresamente hasta después de recibir el sitio; no es un bloqueo de esta entrega sin catálogo inicial.

Código/documentación local: .local/entrega-jyz/jyz-codigo-entrega.zip (174 archivos; excluye entornos, .local y credenciales; contenido comparado con las fuentes). El usuario conserva acceso a las cuentas existentes, copia cifrada local y clave separada; no se ha copiado fuera del equipo ni configurado respaldo automático. Custodia externa, rutina de copias y revisión de revocación anterior son obligaciones operativas documentadas, no pruebas realizadas. Sitio funcional entregable en el dominio Railway aprobado.


## Presentación para empezar a usar la web — 8 de octubre de 2026

Solicitud directa del usuario: preparar una PPT para el negocio. Entregable local: [JYZ — guía de uso](../entrega/presentacion/JYZ-guia-de-uso.pptx), 17 diapositivas editables con identidad JYZ, fotos recibidas y capturas identificadas como demostración cuando contienen datos de prueba. Explica dos accesos del panel, Mryoan sin contraseñas, alta/edición/publicación/ocultación, tallas en JSON, fotos múltiples y WebP, galería, recorrido de WhatsApp, responsables confirmados, errores habituales y continuidad.

Verificado: integridad del paquete e importación Artifact Tool, geometría y fuentes declaradas sin incidencias ni advertencias; dos tablas nativas, siete enlaces, 17 diapositivas renderizadas e inspeccionadas individualmente. XML válido y ausencia de patrones de claves/URI PostgreSQL. Evidencia privada en `.local/ppt-jyz/build/validation-final.json` y `final-slides/`. No se abrió el archivo en PowerPoint; el validador Office adicional no pudo ejecutarse porque falta defusedxml, sin instalar dependencias. No afirmar validación nativa de PowerPoint.

Contenido basado en entrega-operativa.md vigente. Catálogo real, práctica de productos comerciales, asignación individual de custodia de Mryoan y copias cifradas fuera del equipo permanecen responsabilidades del negocio; respaldo automático no configurado. Fuentes y detalles de alcance en notas de diapositivas. Presentación preparada para compartir por el usuario; no enviada a terceros. Sin cambios en la web, datos remotos, cuentas, despliegues, compras, instalaciones, commit o push. Próximo paso: presentar la guía y cargar el primer producto real aprobado.

## Logo al compartir jyzgt.com — ADR 018

Fecha: 8 de octubre de 2026 (Guatemala). Solicitud directa: mostrar el logo al compartir por WhatsApp; usuario confirma dominio comprado. HTTPS y JYZ_REVIEW_ORIGIN verificados bajo https://jyzgt.com antes del cambio.

Implementado y desplegado: metadatos Open Graph y tarjeta social en inicio/fichas, logo JPEG original de 1600×1600, URLs absolutas y canónica bajo jyzgt.com. Raíz/alias apuntan a raíz; ficha conserva ruta. No incluir datos/query del formulario; título escapado. Recurso estático con hash de collectstatic, sin URL firmada que caduque.

Evidencia: 52 pruebas locales catalogo + config.tests_railway aprobadas, check sin incidencias. Paquete nuevo de 71 archivos (897662 bytes), comparado íntegramente con fuentes; no reutiliza archivos antiguos. Railway 0797029f-cf31-4ba5-a02f-a28628da1433 SUCCESS, exclusivamente jyz-revision/jyz-web. HTML anónimo raíz/alias 200 con og:image/canónica/título correctos y sin noindex; JPEG anónimo solicitado con agente WhatsApp 200, image/jpeg, 166777 bytes, 1600×1600 y SHA-256 idéntico al original. Healthz 200, Admin anónimo 401. Evidencias privadas .local/compartir-jyz/tests.txt, deployment.json y https.json. Fichas verificadas localmente con datos de prueba; no se crean productos remotos para probarlas.

Pendiente: comprobación humana de la tarjeta compartiendo el enlace en WhatsApp; HTTP no demuestra presentación real ni actualización de caché. Próximo paso: compartir https://jyzgt.com/ y confirmar imagen/título. Sin mensajes enviados, migraciones, escrituras de catálogo/Storage, instalaciones, compras, DNS, commit/push ni cambios en vibrant-perfection.

## Instagram actualizado — 8 de octubre de 2026

Solicitud directa del usuario: dirigir Instagram al perfil atrevete_jyz21. Footer compartido de inicio/fichas actualizado a https://www.instagram.com/atrevete_jyz21/ y etiqueta correspondiente; se omite vrfl del enlace de compartición. Historial del destino anterior preservado en especificación 06. Nueva pestaña segura conservada.

Verificado: seis pruebas locales de inicio aprobadas; paquete completo de 71 archivos comparado con fuentes actuales. Railway 27fdfa05-9ab1-4013-aa6a-0b6d699b1b55 SUCCESS, solo jyz-revision/jyz-web. Raíz/alias HTTPS 200 con destino, etiqueta y target/rel correctos; metadatos del logo conservados. Evidencia .local/instagram-jyz/https.json. No se afirma auditoría del contenido del perfil; el destino es el confirmado por el usuario. Sin escrituras de datos, migraciones, instalaciones, compras, DNS, commit/push ni cambios en vibrant-perfection. Tarea terminada; catálogo y restantes pendientes operativos conservan su estado.

## Catálogo inicial publicado — ADR 019

Fecha: 8 de octubre de 2026 (Guatemala). Solicitud original: agregar fotos de la carpeta recibida, mejorar pixeladas, tallas generales sin precios y acceso Admin por chat. Tras rechazo del generador (moderation_blocked/output/other, causa específica no informada), el usuario instruye «entonces solo usa las que no esten pixeleadas». Esta instrucción reemplaza la mejora IA: no queda trabajo IA pendiente ni se publica imagen generada.

Selección visual individual: 17 archivos, 16 únicos. Once aceptadas (tres fotos de prendas y ocho imágenes de presentación); cinco excluidas: catalogo_mejorado.png, catalogo_mejorado_simpsons (1).png, catalogo_mejorado_superman.png, catalogo_mejorado_attack_titan.png, catalogo_mejorado_spiderman.png. Un duplicado de sudadera_mejorada_catalogo.png omitido. Los 17 originales se preservan en assets/catalogo-recibido, con SHA-256 y selección documentada; no se borran del origen.

Publicado: once productos nuevos (ID 5–15) y once fotos ProductoImagen en jyz_prueba/bucket privado existente, mediante rol jyz_app limitado y backend WebP. Fotos 29172–131320 bytes, máximo 1600 px, sin ampliación/recorte. Nombre/descripcion visual, no precios/material/técnica/stock inventados; tallas ["Todas las tallas"]. Formulario recoge tallas solicitadas por texto opcional sin inventar opciones XS–XXL; listas concretas conservan validación de cantidades. Consulta de precio/medidas/entrega por WhatsApp, sin mensajes enviados ni pedidos persistidos.

Evidencia: 53 pruebas locales catalogo + config.tests_railway aprobadas; Railway 78a33643-dcaa-4497-844f-1c9f91c5b3cc SUCCESS exclusivamente jyz-revision/jyz-web, paquete nuevo de 71 archivos idénticos a fuentes. Baseline/preservacion demuestran filas de cuatro productos/cuatro fotos y tres filas de galería previas idénticas. Carga idempotente con diario local. HTTPS verifica las once fichas y sus once fotos (200, WebP, SHA-256 idéntico al archivo almacenado), once POST con tallas libres/mensaje correcto, listado de once, sitemap, salud y ficha sintética 4 oculta 404.

Admin: protección anónima 401; Basic y login Mryoan existentes probados en jyzgt.com, productos/galería 200, usuarios/borrado 403, cambio de contraseña disponible. No se crearon cuentas ni se cambiaron credenciales/permisos. El usuario autorizó su entrega por este chat; solo credenciales del panel, sin claves de servidor. Credenciales no incluidas en documentos/evidencias.

Navegador: once fichas, fotos visibles cargadas, ancho 424/contenido 409 sin desbordamiento; ficha Hello Kitty prepara cantidad 3/tallas 2 M y 1 L correctamente, sin abrir/enviar WhatsApp. Captura .local/catalogo-real/catalogo-publicado.jpg. Evidencias .local/catalogo-real/tests.txt, deployment.json, carga.json, baseline.json, preservacion.json y https.json.

Tarea completada. Siguiente paso del negocio: confirmar medidas/precios en chat y editar futuras fichas desde Admin. Sin migraciones, compras, DNS, instalaciones, borrados, commit/push ni intervención en vibrant-perfection. Respaldos/custodia externa restantes conservan los límites previos.

## Panel con un solo login — ADR 020

Fecha: 8 de octubre de 2026 (Guatemala). Solicitud directa «quita la primera proteccion del panel». HTTP Basic retirado exclusivamente de /admin y /static/admin/; panel usa únicamente login Django. Catálogo técnico /catalogo/ conserva protección previa. No se cambian cuentas/contraseñas/permisos. ADR 014/017 reemplazados parcialmente; guías/README/especificaciones actualizados para un acceso.

Evidencia: 55 pruebas locales catalogo + config.tests_railway aprobadas, incluida integración Django que verifica login obligatorio y permisos. Paquete de 71 archivos idénticos a fuente; Railway 5643779d-178b-406d-a771-0e084f85e663 SUCCESS exclusivamente jyz-revision/jyz-web. Once comprobaciones HTTPS aprobadas: login 200 sin WWW-Authenticate, panel/listas anónimos redirigen a login, CSS público, CSRF sin token 403, login Mryoan sin Basic, panel/productos/galería 200, usuarios/borrado 403, logout revoca acceso, catálogo de once fichas/Instagram/logo conservados, ruta técnica 401 y salud 200.

Navegador nuevo sin sesión muestra directamente el formulario JYZ; captura .local/admin-login-unico/login-publicado.jpg. Evidencias tests.txt, deployment.json y https.json en la misma carpeta. Tarea completada: entrar a https://jyzgt.com/admin/ usando Mryoan y contraseña existente. No datos comerciales/migraciones, instalaciones, compras, DNS, borrados, commit/push ni intervención en vibrant-perfection.


## Trabajos ocultos temporalmente — ADR 021

Solicitud directa del usuario: comentar Trabajos por ahora y hacer push al finalizar. Se comentan con etiquetas Django la sección y su enlace; el HTML público no emite la galería. Código, fotos, registros y Admin se conservan, sin migraciones ni escrituras remotas. README, especificaciones y autorización en AGENTS actualizados.

Verificado: 55 pruebas catalogo + config.tests_railway aprobadas. Paquete nuevo de 71 archivos comparado con fuente; Railway 6e169d82-4b54-44dc-926a-8a9db677c39d SUCCESS exclusivamente jyz-revision/jyz-web. HTTPS confirma ausencia de sección/enlace Trabajos, once productos, cotización, Instagram, metadatos del logo y salud 200. Evidencia privada .local/trabajos-ocultos/https.json y deployment.json.

Push autorizado: repositorio local/remoto sin commits previos, se prepara commit inicial del proyecto completo. Revisión de 200 archivos: ningún patrón de clave de proveedor ni coincidencia con seis credenciales reales privadas; .local, entornos, secretos y dependencias excluidos. Las licencias originales tienen espacios finales que se preservan. Sin compras, instalaciones, DNS, borrados ni cambios en vibrant-perfection. Reactivar Trabajos requiere retirar los dos bloques de comentario de inicio.html.

Entrega cerrada: commit inicial 78de44c publicado mediante push a origin/main. Referencia remota verificada idéntica al commit local; repositorio sin cambios pendientes. Este registro final se entrega en un commit documental posterior.
