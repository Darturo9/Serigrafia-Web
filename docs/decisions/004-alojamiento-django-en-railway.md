# ADR 004. Alojamiento Django en Railway

Fecha: 8 de octubre de 2026. Estado: **Railway elegido y verificado para la prueba técnica de Django/Admin/PostgreSQL/fotos; lanzamiento comercial pendiente**.

## Contexto y decisión

Workers Free falló al cargar Django por límite de CPU, según [evidencia real](../plan/evidencia-cloudflare-prueba.md). Tras comparar alternativas, el usuario indicó: «Mejor con Railway, es la plataforma que más conozco!».

Railway reemplaza a Workers/Hyperdrive como destino de alojamiento de Django. Se mantienen Django con plantillas y Admin, PostgreSQL y Storage de Supabase, autenticación Django y atención por WhatsApp. No se reconstruye la aplicación ni se incorpora una base Railway. El alcance funcional no cambia.

Reemplaza la elección de alojamiento de ADR 001; conserva sus decisiones funcionales y de datos. ADR 003 permanece como historial de la prueba Workers, no como requisito del nuevo runtime. Las adaptaciones WASM de concurrencia y contraseñas no se trasladan al servidor nativo.

## Límites y condición de aceptación

La elección inicial cubría registrar/preparar localmente. Posteriormente el usuario reiteró «Si, railway ya esta aprobado, ese vamos a usar! Puedes proceder», autorizando avanzar con el paquete de revisión descrito en prueba-railway.md. No autoriza contratar planes, lanzamiento comercial, eliminar recursos Cloudflare o hacer commit/push. No ejecutar migraciones automáticamente en build o arranque; las 19 existentes no se vuelven a aplicar por cambiar de alojamiento. El usuario activará el plan y avisará: el workspace inspeccionado tiene trial vencido.

Viabilidad técnica confirmada con dos versiones en el proyecto separado jyz-revision: HTTPS Admin/sesiones/permisos/CSRF, ORM, fotos PNG/JPEG/WebP y persistencia tras redespliegue. A02–A06 y A11/A13 parciales registrados en [evidencia Railway](../plan/evidencia-railway-prueba.md). El usuario prefirió build directo remoto, sin instalación local. No equivale a lanzamiento comercial ni aceptación completa. Ver [plan concreto](../plan/prueba-railway.md).

## Fuentes y costos consultados

Railway documenta Django con Gunicorn y WhiteNoise. Se adaptará el proyecto existente; no ejecutar las instrucciones de creación de proyecto/base del tutorial. [Guía oficial](https://docs.railway.com/guides/django).

Hobby tiene mínimo USD 5/mes e incluye USD 5 de consumo; si se excede, se cobra la diferencia. Pro tiene mínimo USD 20 e incluye USD 20. El plan existente, uso, presupuesto y titularidad deben confirmarse antes de crear servicios. No se promete una factura de USD 5. [Precios oficiales](https://docs.railway.com/pricing/plans), consultados el 8 de octubre de 2026.
