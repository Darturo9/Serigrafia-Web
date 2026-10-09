# Evidencia de preparación Railway

Fecha: 8 de octubre de 2026. **Prueba técnica Railway ejecutada: tres despliegues y HTTP Admin/productos/fotos/persistencia aprobados.** Lanzamiento comercial y aceptación completa A01–A13 pendientes. Los apartados iniciales conservan el historial previo al despliegue; prevalece el resultado final siguiente.

## Autorización y acceso

El usuario reiteró «Railway ya está aprobado… puedes proceder». Se continúa con el paquete de revisión protegido de prueba-railway.md. Railway CLI 4.40.2 ya instalado y autenticado como giron605@gmail.com; lectura del listado de proyectos exitosa. Ningún proyecto existente se modificó.

Dashboard del workspace darturo9's Projects (578c07e8-9b24-44e5-8b86-d368f4eb0bf1) muestra TRIAL, Trial expired y solicitud de upgrade. El usuario respondió «Activaré yo el plan y te avisaré». No se contrató ni cambió plan; no se creó servicio/proyecto JYZ ni enviaron secretos. Captura local: .local/railway-prueba/trial-vencido.jpg.

## Preparación implementada

- Perfil settings_railway separado: DEBUG=False, hosts/CSRF concretos, cookies seguras, rol jyz_app, esquema jyz_prueba, pooler existente y TLS verify-full con CA pública Supabase. Bucket privado existente y secretos obligatorios por entorno; sin credenciales en código.
- Gate Basic de revisión antes de WhiteNoise y del Admin, comparación constante, noindex/no-store, validación de host y rechazo de Basic sobre HTTP. No sustituye permisos/autenticación Django.
- Healthcheck exacto /healthz/ con SELECT 1, respuesta genérica 503 si falla PostgreSQL. Excepción sin contraseña ni detalles; host healthcheck.railway.app solo admite salud. HTTPS detrás de proxy preparado; cabeceras reales de Railway aún pendientes de verificar.
- Dockerfile nativo Python 3.11.16, Gunicorn 26.2.0, WhiteNoise 6.12.0 y httpx 0.28.1; versiones existentes preservadas, dependencias resueltas con hashes en requirements.railway.txt. Una réplica/un worker inicial, PORT validado. No migrate ni creación de usuarios en build/arranque.
- collectstatic preparado con perfil independiente sin secretos/DB; CA pública preservada en ops/supabase-root-2021.crt. .dockerignore y paquete aislado excluyen secretos, entornos, datos y referencias comerciales. 41 archivos, 425587 bytes antes de build/collectstatic; no es tamaño de imagen final.
- scripts/railway_native_probe.py preparado para arranque Gunicorn local y siete comprobaciones de solo lectura contra Supabase, con credenciales en entorno del proceso y cierre del servidor. **No ejecutado.**

## Verificaciones ejecutadas y pendientes

`.local/workers-venv/bin/python manage.py test --verbosity 1`: **39 pruebas aprobadas**, 31 anteriores y 8 nuevas de settings/gate/healthcheck. Entorno existente Python 3.13.12, Django 5.2.18, Pillow 12.2.0 y httpx 0.28.1; no instaló paquetes. Las nuevas pruebas simulan DB; no prueban Gunicorn, Linux, conexión remota ni sesiones reales en Railway. La imagen prevista usa Python 3.11.16/Pillow 12.3.0; su validación permanece pendiente.

Compilación Python de archivos nuevos aprobada. Paquete creado con scripts/railway_prepare.py, JSON válido, sin patrones sb_secret_ ni claves privadas y sin migraciones en Docker/config Railway. Exclusión Git de .local confirmada. Esto no sustituye auditoría de credenciales completa ni autorización de commit/push.

Pendientes: respuesta a autorización de instalación local aislada de Gunicorn/WhiteNoise/httpx; ejecutar probe nativo y construir/probar imagen; aviso del usuario sobre plan activo; primer deploy, A02–A05 completos, segundo deploy/A06 y costo observado. No instalar ni desplegar mientras sus respectivas dependencias siguen pendientes.

Evidencia resumida sin secretos en .local/railway-prueba/preparacion.json. Referencias oficiales consultadas: [Django](https://docs.railway.com/guides/django), [healthchecks](https://docs.railway.com/deployments/healthchecks), [Supabase/PostgreSQL](https://supabase.com/docs/guides/database/connecting-to-postgres). Changelog Supabase revisado; el cambio PostgreSQL 15.19/17.11 ya registrado no introduce una migración para este cambio de alojamiento.

## Plan activado posteriormente

Usuario informa pago y prohíbe borrar vibrant-perfection. Dashboard confirma Hobby activo; proyecto existente conservado, sin acciones de modificación/borrado. Regla registrada con ID exacto en AGENTS.md. Captura .local/railway-prueba/hobby-activo.jpg. CLI whoami/list funcionan; status en checkout responde Unauthorized: no asumir contexto listo para desplegar. Instalación local aislada sigue pendiente de respuesta; no ejecutados build/probe/deploy.

## Despliegue directo autorizado y resultados finales

El usuario eligió construir directamente en Railway, sin instalar dependencias localmente. El turno previo solo explicó esta ruta (sin progreso ejecutado); esta continuación creó recursos, desplegó y obtuvo evidencia nueva. La instalación local deja de ser una dependencia. El contexto CLI se resolvió al crear/vincular el proyecto separado; status confirmó ID/nombre antes de secretos y antes del segundo despliegue.

| Recurso | Identidad verificada |
|---|---|
| Proyecto JYZ | jyz-revision, db6b6a44-0a60-4ae3-b8b3-5bb4c309bc6a |
| Servicio | jyz-web, bf4d7246-eda6-4265-b649-695fa2fd5991 |
| Entorno Railway | production, 350cbf32-95e5-47d8-accf-3a881fb624ac; nombre de entorno, no lanzamiento comercial |
| Origen temporal protegido | https://jyz-web-production.up.railway.app |
| Primera versión | 1bdf38b6-ad0d-48cc-ba7b-f158600f7794, SUCCESS antes del redespliegue |
| Segunda versión activa | c06d3114-c026-43f4-ac4c-2cf928c2556d, SUCCESS/ACTIVE |

Docker construyó Linux amd64 con Python 3.11.16 y dependencias fijadas/hashes, sin instalar nada localmente. collectstatic: 133 archivos copiados y 397 postprocesados. Gunicorn 26.2.0 arrancó en 8080 con un worker sync; una réplica US East. Build/arranque no ejecutaron migraciones ni crearon usuarios. Secretos transferidos por stdin a variables del servicio, sin exponer valores en comandos, código o evidencias. CA pública incluida, PostgreSQL con verify-full y rol jyz_app; sin base ni volumen Railway nuevos.

HTTP real: healthz 200 con consulta PostgreSQL; /inicio/, /admin/login/ y estilos 401 sin acceso de revisión, 200 con él. Página JYZ renderizada, cookie CSRF Secure y assets disponibles. La prueba de Admin por HTTPS usó el editor sintético existente y pasó **22 comprobaciones**: login/sesión Secure+HttpOnly, permisos sin usuarios/borrado, CSRF, creación/edición, publicación/ocultación, PNG/JPEG/WebP, bytes persistidos y archivo corrupto rechazado sin perder referencia anterior, logout. Conteo verificado en .local/railway-prueba/admin-http.json.

Producto creado ID 2: sintético, es_ejemplo=True y publicado=False al terminar. Se crearon tres fotos sintéticas en el bucket privado existente; no se borraron objetos ni se modificó el producto original ID 1. Ejemplo publicado temporalmente solo en catálogo técnico protegido; /inicio/ lo excluyó en todas las comprobaciones.

Después del segundo despliegue, un proceso nuevo verificó referencia y hash privado. HTTP contra la nueva versión volvió a iniciar sesión, leer el producto oculto y pedir la URL firmada generada por ese servidor: bytes/hash correctos. Cinco verificaciones registradas en persistence-http.json. A02–A06 tienen evidencia técnica en Railway; A11 cubre imagen inválida y catálogo sin ejemplos, sin simular caída remota de Storage en esta ejecución. A13 solo parcial.

`vibrant-perfection` reconsultado al final por listado de solo lectura: ID, deletedAt=null, servicios bot-AI/Redis y updatedAt originales sin cambios. Ningún comando de borrado, modificación o redespliegue apuntó a ese proyecto. Evidencia protected-project-check.json.

Acceso de revisión entregable en archivo local .local/railway-prueba/acceso-revision.txt (0600, excluido de Git). Contiene solo origen/usuario/contraseña de revisión, no Storage ni PostgreSQL. El Admin conserva su autenticación adicional; no compartir claves de servidor.

Evidencia sin secretos: destino.json, http-initial.json, admin-http.json, deployments-final.json, persistence-http.json, protected-project-check.json y captura despliegue-confirmado.jpg. No hubo commit/push, instalaciones locales, nuevas migraciones, dominio/DNS, compras por el agente, eliminación de recursos Cloudflare ni lanzamiento comercial.

Pendientes: catálogo/fotos reales, revisión humana de frontend remoto/móvil, apertura WhatsApp real, dominio jyzgt.com solo candidato (compra no confirmada), costos medidos con suficiente tiempo, responsables, capacitación y respaldo/recuperación. No prometer factura mensual ni aceptación comercial por una prueba técnica exitosa.

## Ajuste final de configuración Railway

Railway no aplica Config as Code a servicios nuevos desde el 28 de agosto de 2026, según aviso del dashboard y [documentación oficial](https://docs.railway.com/config-as-code/reference). La revisión de los metadatos detectó healthcheck sin ruta y 10 reinicios: railway.json no era efectivo. Se conserva como referencia histórica y se excluye de nuevos paquetes. Se configuró únicamente jyz-web desde su dashboard: /healthz/, timeout 120 segundos, ON_FAILURE con 3 reintentos, una réplica. Tercera versión 455e5314-b271-4371-8244-73c07779f308: SUCCESS. Metadatos del despliegue confirman ruta, timeout y reintentos aplicados; siete comprobaciones HTTP finales aprobadas (salud 200, protección 401 y acceso de revisión/estáticos 200). Evidencia: deployment-health.json y http-health-final.json. No se modifica vibrant-perfection ni se instala software local.

## Formularios y ejemplo autorizado

Cuatro comprobaciones HTTP adicionales de seguimiento/rechazo de ejemplos aprobadas en solicitudes-http.json. El usuario autorizó después un producto de prueba con imagen Unsplash y confirmó que el dueño administrará el panel. Producto 3 creado por Admin HTTPS con rol editor: publicado/de ejemplo, tallas vacías y foto de Fallon Michael (399222 bytes), procedencia/licencia/hash en producto-demo.json. ADR 005 mantiene ejemplos exclusivamente en el perfil Railway protegido, etiqueta no venta y rechazo de cotización. Doce pruebas locales afectadas aprobadas; una corrección posterior evita enviar al catálogo para cotizar cuando solo hay ejemplos, con cuatro pruebas afectadas aprobadas. Despliegue final pendiente de comprobación.

Revisión visual del ejemplo detectó que una sola ficha se expandía a todo el ancho de escritorio; se ajustó la cuadrícula para conservar columnas de tamaño normal. No cambia campos, opciones ni permisos. Verificación final de tamaño/foto pendiente del despliegue de este CSS.

Resultado final del ejemplo: versión 9e9c9ff2-9177-4df1-8593-bdee7dda04cf SUCCESS. Navegador remoto confirma foto cargada y tarjeta de 287 px en escritorio 1440; sin desbordamiento en 320/390/1440. Producto 3 identificado como prueba/no venta, sin enlaces de cotización y rechazo de POST directo verificado. Evidencia demo-http-final.json, demo-browser.json, deployment-demo-final.json y .local/design-review/catalogo-demo-railway.png. Perfil protegido/healthcheck y configuración de reinicios conservados. Guía del dueño actualizada; propuesta de respaldo/recuperación preparada sin ejecutar. Datos/fotos comerciales, cuenta/capacitación, WhatsApp en dispositivo real, recuperación y lanzamiento siguen pendientes; no marcar objetivo completo.

## Lectura inicial de consumo Railway

Consulta de solo lectura del proyecto jyz-revision: Usage muestra USD 0.00 actual/estimado redondeados; detalle inicial memoria 0.0003, CPU 0.0000 y egreso 0.0001 USD. Son datos de un servicio recién creado, no una factura ni una previsión mensual válida, y no incluyen Supabase/dominio/otros proyectos. No se cambia plan, presupuesto, alertas ni límites. Evidencia consumo-inicial.json/png y metricas-revision.png. Seguimiento de consumo representativo y presupuesto del dueño sigue pendiente.


## Cierre de optimización WebP — 8 de octubre

Despliegue 9a8d78bc-2b1a-4e75-b31a-949c6b31503e SUCCESS. Prueba real por HTTPS Admin con producto de ejemplo 3: entrada JPEG 399222 bytes; salida WebP 49098 bytes, 1600 × 1067 px, sin EXIF (87,7 % de reducción en esta imagen). Storage privado y URL firmada sirven image/webp; objeto anterior conservado y reemplazo inválido conserva referencia válida. Evidencia: .local/railway-prueba/webp-http.json y deployment-webp.json. Suite local: 43 pruebas aprobadas. Ver ADR 007. Sin migraciones, nuevas instalaciones, conversión masiva, commit/push ni cambios en vibrant-perfection. Revisión visual nueva de esta versión no ejecutada; aceptación comercial y entrega del dueño siguen pendientes.

Dominio vigente por instrucción del usuario: jyz-web-production.up.railway.app. Puede usarse para la web funcional; compra y configuración de dominio propio quedan aplazadas hasta una nueva confirmación del usuario.

## Panel JYZ desplegado y comprobado

Versión final a8450427-575e-47cf-8e48-8431a305ee23 SUCCESS en jyz-revision/jyz-web. Once comprobaciones HTTPS aprobadas: salud, protección de revisión, título JYZ, CSS vigente (normalizando hashes de fuentes de collectstatic), fuente local, login, portada, lista/estados, edición agrupada, usuarios restringidos y logout. Evidencia .local/railway-prueba/deployment-admin-jyz.json y admin-jyz-http.json; script reproducible scripts/railway_admin_design_probe.py. Sin cambios de productos, permisos o recursos ajenos; vibrant-perfection intacto. Las capturas corresponden a navegador local con los mismos archivos, no a revisión visual remota.

La tarea de personalizar el panel y explicar pendientes está completada técnicamente. Revisión visual humana aún pendiente; no se retiró Basic/noindex ni se publicó comercialmente. Plan de presentación/limpieza en presentacion-funcional.md. Requisitos de entrega del negocio siguen abiertos y no se confunden con esta tarea concreta.

Footer desplegado: 166e41aa-f167-4434-8e91-484cc71948c2 SUCCESS. Seis comprobaciones HTTPS aprobadas: página, Instagram exacto, nueva pestaña segura, logo en footer, archivo del logo y CSS nuevo. Evidencia .local/railway-prueba/deployment-footer.json y footer-http.json; capturas visuales locales. Sin migraciones, datos editados, nuevos recursos, commit/push ni cambios en vibrant-perfection.

## Galería de referencia Pexels autorizada y desplegada

Usuario solicita fotos de prueba, principalmente playeras y gorras. Tres fotos: dos playeras y una gorra; licencia Pexels consultada y páginas/autores/hashes registrados en catalogo/static/catalogo/galeria-referencias/procedencia.json. Cada foto marcada Referencia de prueba, crédito/enlace de origen y aviso No son trabajos realizados por JYZ. Copias WebP 15248/57968/38702 bytes (111918 bytes total), originales de descarga conservados localmente. No representan productos ofertados ni portafolio real.

Versión 13de94b7-21f1-4a5c-92ef-4d9445f33067 SUCCESS. Seis comprobaciones HTTPS: página, aviso, tres etiquetas, créditos, tres fotos y bytes/MIME de archivos coincidentes con fuente. Evidencia .local/railway-prueba/deployment-galeria.json y galeria-http.json. Navegador local: tres fotos cargadas; sin desbordamiento 320/390; capturas galeria-pexels.png y galeria-pexels-movil.png. Check aprobado. No hay módulo de galería en Admin, nuevas instalaciones/migraciones ni escrituras de catálogo; revisión protegida conservada, vibrant-perfection intacto. Para versión comercial siguen pendientes trabajos propios autorizados y revisión humana.

## Catálogo centrado y propuesta de varias fotos

Usuario aprueba corregir distribución y solicita pensar opción para varias fotos. Encabezado centrado; cuadrícula auto-fit de fichas hasta 360 px, máximo 1240 px; consulta general fuera de la cuadrícula, franja debajo. Mejorado contraste de ayudas sobre fondo claro. Check y 21 pruebas de catálogo aprobadas. Navegador local con producto remoto de ejemplo: ficha centrada (360 px), sin desbordamiento 320/390; escenarios 0/3 renderizados sin escribir en base remota también sin desbordamiento de página en escritorio. Capturas catalogo-centrado.png y consulta-personalizacion-franja.png.

Versión da83999c-9b9b-4b80-946b-d31c0b802c24 SUCCESS. Seis comprobaciones HTTPS aprobadas: página, consulta independiente, encabezado centrado, identificación del ejemplo, CSS vigente y WhatsApp conservado. Evidencia .local/railway-prueba/deployment-catalogo-layout.json y catalogo-layout-http.json. No se modifican catálogo, recursos ajenos, migraciones, permisos ni protección de revisión. vibrant-perfection intacto.

ADR 009 es propuesta pendiente: portada en catálogo, ficha con miniaturas y hasta seis fotos sugeridas; administración inline/orden/portada, Storage/WebP y compatibilidad con foto actual. No se implementa todavía ni se aplica migración remota. Siguiente paso: revisar distribución y decidir si aprobar ampliación de fotos antes de preparar paquete de datos/permisos.
