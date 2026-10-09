# Plan de tareas

Estado vigente: Railway probado con tres versiones, Admin/ORM/fotos/persistencia HTTP aprobados en proyecto separado. Publicación comercial y aceptación completa pendientes. Workers Free falló por CPU; secciones anteriores conservadas como historial.

## Etapa 0. Contexto SDD

- [x] Crear carpeta y documentos de contexto.
- [x] Registrar alcance, límites, arquitectura propuesta y pendientes.
- [x] Copiar PDF y presentación de cinco diapositivas sin modificar originales.
- [x] Verificar estructura, referencias y contenido documental.

## Etapa 1. Materiales y viabilidad

- [ ] Recibir identidad, catálogo, fotos y contacto real (R01, R02, R06).
- [ ] Confirmar responsables, dominio, presupuesto y roles de revisión/publicación.
- [x] Obtener autorización para la prueba local de administración, productos y fotos.
- [x] Ejecutar 10 pruebas contra PostgreSQL local, comprobar persistencia y revisar catálogo/login en navegador.
- [x] Autorizar paquete de prueba Supabase (esquema/roles, migraciones, bucket y datos sintéticos). Cloudflare y despliegues siguen pendientes.
- [ ] Fijar versiones compatibles y planes de Workers/Hyperdrive/Supabase.
- [ ] Probar panel, producto, foto y persistencia en el alojamiento propuesto (A02–A06; A11/A13 parciales).
- [x] Registrar ADR 004: Railway elegido tras fallo Workers Free; viabilidad remota pendiente.

## Etapa 2. Diseño y especificación de implementación

- [x] Aprobar dirección visual de primera sección con identidad JYZ y contenido confirmado (R01, R09); respuesta directa del usuario el 8 de octubre.
- [ ] Concretar campos y relaciones del catálogo con los productos recibidos.
- [ ] Fijar límites y validaciones de fotos y permisos del panel.
- [ ] Definir mensaje de solicitud, consulta de seguimiento y referencia manual de pedidos (R03–R05).
- [ ] Documentar esas decisiones antes de extender el código.

## Etapa 3. Construcción

- [ ] Implementar presentación, catálogo, galería y contacto (R01, R02, R06, R09).
- [ ] Configurar administración de productos/fotos y carga inicial (R07, R08).
- [ ] Implementar formulario y enlaces a WhatsApp (R03–R05).
- [ ] Completar permisos, secretos y almacenamiento persistente.

## Etapa 4. Revisión

- [ ] Ejecutar criterios A01–A13 y registrar evidencia y limitaciones.
- [ ] Revisar en celular, computadora y navegación con teclado.
- [ ] Corregir fallos y repetir solo comprobaciones afectadas.
- [ ] Preparar respaldo y recuperación de base y fotos.

## Etapa 5. Entrega y publicación

- [ ] Entregar guía y capacitar al responsable (R10, A12).
- [ ] Entregar accesos por canal seguro y confirmar titularidad.
- [ ] Obtener revisión final y autorización de publicación.
- [ ] Publicar en el dominio aprobado y verificar el recorrido público.
- [ ] Acordar soporte, actualización y revisión de cuotas/incidencias.

No marcar una tarea completa sin evidencia. La fecha objetivo no permite omitir permisos, contenido confirmado ni pruebas. Git inicializado y origin asociado al repositorio indicado por el usuario; primer commit/push y flujo de versiones pendientes de autorización/definición.

## Actualización de materiales

- [x] Recibir y preservar PDF JYZ; documentar contenido y límites en especificación 06.
- [x] Comprobar herramientas MCP disponibles y probar lectura del proyecto proporcionado. Resultado: acceso denegado, no conexión verificada.
- [x] Verificar lectura del proyecto `kcahxuvfmrzxzlnpezyf` mediante el nuevo servidor MCP autenticado, distinto del conector del plugin. URL y SELECT correctos; el fallo anterior del plugin se conserva como histórico.
- [x] Confirmar código de país de WhatsApp: +502, Guatemala, por respuesta directa del usuario.
- [ ] Confirmar catálogo concreto y uso autorizado de fotos de referencia.

## Preparación de alojamiento — 7 de octubre de 2026

- [x] Leer SDD existente y registrar autorización de inspección/preparación sin ampliar permiso remoto.
- [x] Inspeccionar esquemas, relaciones y buckets sin modificar datos; PostgreSQL 17.11, sin tablas Django ni buckets. Evidencia: `inspeccion-supabase.md`.
- [x] Preparar secuencia, cambios remotos propuestos y criterios en `prueba-alojamiento.md`.
- [x] Corregir alcance de prueba: A07 es WhatsApp, no persistencia ni fotos.
- [x] Preparar adaptador Workers, settings separados y backend de fotos con archivos revisables (P1); ADR 003 y archivos en ops/.
- [x] Instalar herramientas aisladas con autorización y superar filtro local Workers (P2): 25 comprobaciones HTTP y 21 pruebas nativas; evidencia-workers-local.md.
- [x] Entregar plan/SQL exacto y obtener autorización específica de esquema, roles, migraciones, bucket y datos sintéticos (P3–P4).
- [ ] Obtener autorización de Hyperdrive, secretos y Worker de prueba protegido, incluyendo despliegues (P5–P6).
- [ ] Verificar A02–A06 y A11/A13 parciales en alojamiento; confirmar o revisar ADR 001 según evidencia (P7).

El plan está preparado; ninguna de estas tareas de ejecución se considera completada por leer documentación del proveedor. El conector del plugin no necesita desbloquearse para esta inspección: el servidor OAuth ya permite lectura.

## Implementación local de Workers

- [x] Preservar entorno y catálogo originales; usar esquema local separado.
- [x] Verificar login PBKDF2, sesiones, CSRF, permisos, ORM, rollback, concurrencia y JPEG/PNG/WebP en WebAssembly.
- [x] Preparar inventario de 19 migraciones, SQL de esquema/roles y configuración privada de bucket sin aplicarlos.
- [x] Probar backend Storage con respuestas HTTP simuladas y conservación de foto anterior ante fallo.
- [x] Probar transporte HTTP Storage en Workers local y persistencia real de fotos en Supabase desde otro proceso; Hyperdrive/redespliegue pendientes.
- [ ] Revisar límites de bundle, CPU, memoria, costos y protección en la cuenta Cloudflare.

Las versiones del perfil local están fijadas; planes y compatibilidad remota siguen pendientes. La fecha objetivo del usuario es avanzar hoy, condicionada a materiales, revisión y permisos.

## Preparación de contenido y solicitudes — 8 de octubre

- [x] Extraer logo JPEG recibido sin alterar PDF y registrar procedencia/hash. Archivo vectorial independiente pendiente.
- [x] Implementar validación y mensajes WhatsApp para R03–R05 sin guardar pedidos; 7 pruebas nuevas, suite nativa total 28.
- [x] Confirmar preferencias, presentar primera sección y obtener aprobación visual.
- [ ] Integrar formularios tras revisión inicial y comprobar A07 en navegador/celular.

Ver solicitudes-whatsapp.md. Supabase fue autorizado; Cloudflare/despliegues aún requieren autorización propia.

## Preparación de guía — 8 de octubre

- [x] Preparar guía de catálogo con campos, permisos, fotos, ocultación y cierre de sesión, contrastada con el código actual.
- [x] Revisar visualmente la pantalla de login Workers local en navegador; no equivale a revisar todo el panel o móvil.
- [ ] Entregar acceso definitivo y ejecutar capacitación con la persona designada siguiendo la guía (R10/A12).

Guía en ../entrega/guia-de-catalogo.md. La entrega sigue pendiente: guía preparada no equivale a persona capacitada.

## Dependencia de respuesta humana

El bloqueo histórico por permiso Supabase y dirección visual quedó resuelto por respuestas explícitas del usuario el 8 de octubre. La primera sección fue aprobada. Permanecen pendientes catálogo/fotos comerciales y autorización específica de Cloudflare/despliegues.

## Supabase aplicado

- [x] Crear/verificar esquema y roles, 19 migraciones Django y bucket privado autorizado.
- [x] Probar creación/edición/lectura ORM con rol de ejecución y producto sintético oculto.
- [x] Provisionar clave Storage y comprobar fotos/panel desde Django nativo con PostgreSQL/Storage remotos (3 formatos y 14 comprobaciones del panel).
- [x] Habilitar/verificar RLS en 11 tablas, acceso del rol servidor y exclusión de jyz_prueba de Data API.
- [ ] Probar las mismas operaciones desde Workers/Hyperdrive remoto y verificar persistencia después de redespliegue.

Evidencia y límites: evidencia-supabase-prueba.md.

## Verificación con clave Storage — 8 de octubre

- [x] Ejecutar prueba de fotos PNG/JPEG/WebP reales en Storage privado, lectura firmada, rechazo de acceso público y conservación de referencia ante imagen inválida.
- [x] Comprobar persistencia de foto desde segundo proceso y panel mediante Django Client nativo con datos remotos.
- [x] Integrar catálogo, cotización, galería pendiente y seguimiento en la vista comercial aprobada; suite nativa total 31 pruebas.
- [x] Comprobar seguimiento con acentos desde navegador Workers local, sin enviar mensajes.
- [ ] Completar A07/A10 en dispositivo real y con catálogo confirmado; apertura real de WhatsApp pendiente.

No se ha creado Hyperdrive, desplegado Workers, comprado servicios ni hecho commit/push.

## Clave reemplazada y repositorio — 8 de octubre

- [x] Comprobar lectura privada con la credencial actual sin modificar datos remotos.
- [x] Inicializar Git local en main y configurar origin con la URL proporcionada.
- [x] Confirmar exclusión de claves, credenciales locales y entornos por .gitignore.
- [ ] Confirmar revocación de la clave anterior.
- [ ] Autorizar y preparar primer commit/push; no ejecutados.

## Paquete Cloudflare — 8 de octubre

- [x] Consultar límites/precios actuales oficiales y registrar límites pendientes de cuenta real.
- [x] Preparar paquete separado sin secretos ni configuración exclusiva del Mac y ejecutar dry-run local: 43,34 MiB, 134 assets, exit 0.
- [x] Concretar origen directo, TLS verify-full, CA, rol limitado, secretos y dos despliegues de revisión en paquete-cloudflare-prueba.md.
- [x] Obtener autorización específica del paquete Cloudflare: respuesta «Si autorizo».
- [ ] Inspeccionar cuenta/plan y ejecutar P5–P7 sin compras ni cambios de plan.

## Compatibilidad de lectura Storage en WASM — 8 de octubre

- [x] Ejecutar lectura privada de objeto existente desde workerd local con Storage real, sin escrituras remotas.
- [x] Resolver fallo HEAD/jsfetch usando GET de metadatos; 31 pruebas nativas con regresión aprobadas.
- [x] Verificar URL firmada, bytes/hash y rechazo de lectura pública desde WebAssembly.
- [x] Actualizar paquete con corrección y repetir dry-run afectado: 44377.92 KiB, aprobado.
- [x] Verificar carga PNG/JPEG/WebP y rechazo de imagen corrupta desde WASM local al bucket autorizado.
- [ ] Verificar Hyperdrive y dos despliegues cuando se autorice Cloudflare.

## Carga Storage WASM — 8 de octubre

- [x] Guardar/leer tres fotos sintéticas mediante Pillow y backend Storage en workerd local; bytes, hash, metadatos y URL firmada correctos.
- [x] Releer las tres fotos desde otro proceso tras terminar Worker; producto permanece oculto/de ejemplo.

Evidencia worker-storage-read-5/result.json y persistence.json dentro de .local. No son materiales comerciales ni prueba de redespliegue remoto.

## Dependencia vigente de Cloudflare

Empaquetado y transporte Storage local completados y revalidados. P5–P7 esperan autorización explícita del paquete-cloudflare-prueba.md. Meta bloqueada tras al menos tres turnos con esta dependencia sin resolver; conservar pruebas y archivos actuales para retomar. No interpretar mensajes automáticos del objetivo como permiso de despliegue o transferencia de secretos.

## Ejecución Cloudflare autorizada

- [x] Autenticar Wrangler con aprobación humana OAuth.
- [x] Verificar plan Free y subdominio en dashboard.
- [x] Subir CA pública y crear Hyperdrive limitado con verify-full, sin caché y cinco conexiones.
- [x] Confirmar primera versión desplegada y respuesta anónima inicial 401; comprobación posterior 500, protección/disponibilidad estable pendientes.
- [ ] Superar A02–A05 remotos: prueba fallida por CPU en Free, decisión de plan/alojamiento necesaria.
- [ ] Segundo despliegue/persistencia y revisión de recursos/CPU.

## Resultado de la prueba Free

- [x] Diagnosticar errores HTTP desde registros reales: CpuLimitExceeded/exceededCpu al cargar Django.
- [x] Registrar resultado, recursos persistentes y límites en evidencia-cloudflare-prueba.md.
- [x] Acordar alternativa de alojamiento: usuario elige Railway; ADR 004 registrado, plan de cuenta pendiente.
- [ ] Retomar prueba completa y segundo despliegue cuando funcione Django en el plan autorizado.

## Railway elegido — 8 de octubre

- [x] Registrar instrucción del usuario, ADR 004 y actualización de arquitectura; conservar aplicación, Supabase e historial Cloudflare.
- [x] Preparar plan local y paquete remoto revisable en prueba-railway.md, vinculados con A02–A06/A11/A13.
- [x] Implementar perfil nativo, protección de revisión, configuración de estáticos y arranque de servidor; ejecución Gunicorn/Docker pendiente.
- [ ] Fijar dependencias y obtener autorización aplicable antes de instalarlas; verificar paquete local.
- [x] Recibir reiteración de autorización del paquete Railway y confirmar acceso CLI/workspace; trial vencido.
- [ ] Recibir aviso de activación del plan por el usuario y confirmar presupuesto disponible antes de desplegar.
- [x] Desplegar y probar Admin/productos/fotos y persistencia tras segundo despliegue; 22 comprobaciones Admin y cinco de persistencia aprobadas.

No se ha creado ningún servicio Railway ni transferido secretos, instalado herramientas, hecho commit/push o aplicado nuevas migraciones en esta etapa.

39 pruebas aprobadas (31 anteriores + 8 de configuración/protección nativa). Paquete separado preparado, 41 archivos/425587 bytes; probe nativo e imagen pendientes de instalación autorizada. Ver evidencia-railway-prueba.md. Usuario activará el plan y avisará; no solicitar de nuevo aprobación del proveedor.

- [x] Verificar y abrir vista local de avances solicitada por el usuario: http://127.0.0.1:8787/inicio/, HTTP 200; servidor existente conservado.

- [x] Confirmar plan Railway Hobby activo y registrar instrucción NUNCA borrar ni modificar vibrant-perfection; JYZ separado.
- [ ] Resolver autorización de instalación aislada, verificar imagen y contexto CLI del proyecto JYZ antes de desplegar.

## Prueba Railway ejecutada directamente

- [x] Resolver ruta sin instalación local por preferencia del usuario; dependencias instaladas dentro de imagen remota.
- [x] Crear/vincular jyz-revision/jyz-web y verificar destino exclusivo antes de secretos y redespliegue.
- [x] Construir imagen Linux, collectstatic y arrancar Gunicorn sin migraciones nuevas.
- [x] Verificar HTTP HTTPS protegido, cookies, Admin limitado, CSRF y CRUD/fotos sintéticas (A02–A05).
- [x] Confirmar nueva versión activa, relectura del producto oculto y hash de foto firmada (A06).
- [x] Reconsultar vibrant-perfection sin modificaciones: mismo ID/servicios/estado/updatedAt.
- [x] Preparar acceso de revisión local privado y evidencia; sin commit/push ni dominio/DNS.
- [ ] Completar contenido real, revisión humana remota/móvil, WhatsApp, costos observados, respaldo y capacitación antes de lanzamiento comercial.

Ver evidencia-railway-prueba.md. Las tareas previas de instalación/probe local quedan reemplazadas por build y prueba remota autorizados, no son bloqueos pendientes.

## Ajuste final de configuración Railway

Railway no aplica Config as Code a servicios nuevos desde el 28 de agosto de 2026, según aviso del dashboard y [documentación oficial](https://docs.railway.com/config-as-code/reference). La revisión de los metadatos detectó healthcheck sin ruta y 10 reinicios: railway.json no era efectivo. Se conserva como referencia histórica y se excluye de nuevos paquetes. Se configuró únicamente jyz-web desde su dashboard: /healthz/, timeout 120 segundos, ON_FAILURE con 3 reintentos, una réplica. Tercera versión 455e5314-b271-4371-8244-73c07779f308: SUCCESS. Metadatos del despliegue confirman ruta, timeout y reintentos aplicados; siete comprobaciones HTTP finales aprobadas (salud 200, protección 401 y acceso de revisión/estáticos 200). Evidencia: deployment-health.json y http-health-final.json. No se modifica vibrant-perfection ni se instala software local.

## Revisión de entrega y ejemplo autorizado

- [x] Verificar seguimiento con acentos, referencia excesiva y rechazo de cotización de ejemplo por HTTP Railway; cuatro comprobaciones en solicitudes-http.json, sin abrir/enviar WhatsApp.
- [x] Revisar anchos 320/390/1440, etiqueta de seguimiento y acceso por teclado en navegador local; A10 parcial, teléfono físico pendiente.
- [x] Actualizar guía para Railway y registrar dueño como administrador previsto. Cuenta definitiva/capacitación A12 pendientes.
- [x] Registrar ADR 005 y crear producto 3 de ejemplo con foto Unsplash autorizada, sin precios/tallas comerciales.
- [x] Verificar visibilidad etiquetada y rechazo de cotización en pruebas locales: 12 pruebas afectadas aprobadas.
- [x] Verificar ejemplo/foto cargada en Railway, avisos/no cotización y anchos 320/390/1440; versión final 9e9c9ff2-9177-4df1-8593-bdee7dda04cf SUCCESS.

- [x] Preparar procedimiento de respaldo/recuperación separado de persistencia, sin exportaciones ni cambios remotos. Ejecución y restauración siguen pendientes de destino/responsables/autorización.

## Revisión del Admin en navegador remoto

Login/logout ejecutados con teclado; ficha 3 abierta sin guardar cambios. Secuencia Tab recorre descripción, categoría, tallas, foto/limpiar, descripción de foto, publicado y orden. Todos los campos de datos tienen etiqueta; botones submit usan su texto como nombre accesible. Anchos 320/390/1440 sin desbordamiento horizontal. Evidencia admin-browser.json y .local/design-review/admin-movil-railway.png. No se editaron productos ni permisos; no sustituye teléfono físico, selector de archivos/errores completos por teclado ni capacitación A12.

## Lectura inicial de consumo Railway

Consulta de solo lectura del proyecto jyz-revision: Usage muestra USD 0.00 actual/estimado redondeados; detalle inicial memoria 0.0003, CPU 0.0000 y egreso 0.0001 USD. Son datos de un servicio recién creado, no una factura ni una previsión mensual válida, y no incluyen Supabase/dominio/otros proyectos. No se cambia plan, presupuesto, alertas ni límites. Evidencia consumo-inicial.json/png y metricas-revision.png. Seguimiento de consumo representativo y presupuesto del dueño sigue pendiente.

## Hoodies y consulta de posibilidades — revisión de Marielos

Instrucción transmitida por el usuario: hoodies en lugar de gorras y una opción para consultar qué se puede personalizar. ADR 006 registrado antes de implementar. No había gorras en la página actual; el catálogo menciona camisetas/hoodies como ideas y añade una tarjeta independiente «¿Qué puedo personalizar?». Enlace al WhatsApp confirmado con consulta preparada sobre prendas/materiales/opciones; no envío automático, sin nuevos pedidos/productos ni escrituras de catálogo. Once pruebas afectadas aprobadas. Versión 6c407cf3-7f60-43af-8653-7ad298ded74b SUCCESS. Navegador remoto: título/texto con hoodies, consulta al +50247233834 codificada correctamente y sin desbordamiento en 320/390/1440. Evidencia consulta-personalizacion.json y captura .local/design-review/hoodies-y-personalizacion-railway.png. Sin apertura/envío del chat, migraciones ni cambios en vibrant-perfection.

## Próxima etapa — información del dueño y aceptación humana

- [x] Auditar estado de cierre: prueba técnica/últimos cambios verificados y archivos esenciales del paquete consistentes; no hay despliegue en curso.
- [ ] Recibir usuario deseado del dueño y responsable de WhatsApp; no solicitar contraseñas por chat.
- [ ] Recibir comprobación en teléfono del chat/mensaje de la nueva consulta de personalización.
- [ ] Incorporar catálogo/fotos reales cuando estén disponibles y acordar el acceso/recuperación/dominio antes de entrega.

La falta de datos comerciales no se resuelve cambiando ejemplos a reales. Revisar criterio por criterio en revision-aceptacion-railway.md; mantener la meta activa hasta resolver dependencias.

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
