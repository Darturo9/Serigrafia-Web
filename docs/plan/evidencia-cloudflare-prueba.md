# Prueba remota Cloudflare y resultado

Fecha: 8 de octubre de 2026, Guatemala. Estado: recursos y primera versión aplicados con autorización; aceptación técnica fallida en Workers Free por CPU. No se confirmó ADR 001 ni se cambió de plan/proveedor.

## Acceso y recursos verificados

- Wrangler OAuth autenticado por el usuario. Cuenta bdc73f4bbbc036a160e49f5f9cc86b62, subdominio giron605.workers.dev. Dashboard muestra Free como Current plan. API de suscripciones fue rechazada por scope; no se interpretó como ausencia de suscripción.
- CA pública Supabase Root 2021 subida como jyz-supabase-prueba-ca, ID a49c9d58-9d1e-4134-8eba-0003b263fa53, vigente hasta abril de 2031.
- Hyperdrive jyz-prueba, ID 0b4d3142b2354c2d832c44bf1f0fde4a, origen directo db.kcahxuvfmrzxzlnpezyf.supabase.co:5432, base postgres, usuario jyz_app. verify-full con CA, caché desactivada y límite cinco conexiones. Creación exitosa verifica conectividad inicial; no prueba ORM ni sesiones.
- Worker jyz-prueba desplegado, versión 10db0a9f-cb3c-4212-ae88-1de6361d2522. Runtime compatibilidad 2026-10-07, python_workers, bundle 44377.92 KiB, startup informado 899 ms. Origen de revisión https://jyz-prueba.giron605.workers.dev, previews desactivadas.
- Cuatro secretos se enviaron en la misma primera versión mediante archivo local 0600: DJANGO_SECRET_KEY, JYZ_REVIEW_USER, JYZ_REVIEW_PASSWORD y SUPABASE_STORAGE_KEY. Valores excluidos de documentación/código/browser. API de settings verifica nombres y tipo secret_text sin imprimir valores.

## Resultado HTTP y CPU

Primera petición sin credencial de revisión: 401 y noindex. En la comprobación final, una petición anónima devolvió 500: no afirmar protección HTTP estable ni disponibilidad tras los fallos de CPU. No se obtuvo contenido de aplicación con esa petición. Petición autorizada a /inicio/: 500, página Cloudflare Error 1101. /admin/login/: 503. No aceptar respuestas de despliegue exitoso como prueba de aplicación funcional.

Wrangler tail confirma dos fallos: primera petición outcome exception, cpuTime 2003 ms y CpuLimitExceeded al importar django.core.wsgi/get_wsgi_application (la traza llega a django.core.serializers.python). Otra petición outcome exceededCpu, cpuTime 16 ms. Mensajes: Python Worker exceeded CPU time limit / Worker exceeded CPU time limit. No se observó una consulta ORM remota exitosa.

El plan Free de esta cuenta muestra máximo 10 ms CPU por petición. Estos datos demuestran que la versión actual no supera la prueba en ese plan. No demuestran que Paid ya funcione ni descartan otros fallos posteriores de ORM, memoria o carga de fotos. El arranque 899 ms está cerca del límite documentado de un segundo; merece nueva medición si se autoriza continuar.

## Evidencia

Archivos locales sin claves: .local/cloudflare-prueba/inspeccion.json, ca.json, hyperdrive-create.json, deploy-1.log, http-inicial.json, diagnostico.json y estado-remoto.json. Diagnóstico conserva outcomes, CPU y excepciones con valores sensibles filtrados; no conserva headers, cookies, cuerpo de requests ni URLs firmadas. Captura dashboard: .local/design-review/hyperdrive-creado.jpg.

## Pendientes y decisión necesaria

P5 parcial: recursos/versión existentes y protección comprobada, aplicación fallida. A02 solo evidencia inicial de barrera de revisión, sin funcionamiento estable; login Django, A03–A06 y A11/A13 remotos no aprobados. Segundo despliegue suspendido: no tiene sentido acreditar persistencia de una aplicación que aún no funciona. Supabase nativo y Storage WASM local mantienen su evidencia previa independiente.

Se detiene la etapa sin contratar nada, conforme al paquete autorizado. Workers Paid tiene mínimo USD 5 por mes por cuenta y cargos por exceso; no es garantía de costo total ni compatibilidad. Para continuar, el usuario debe decidir si autoriza evaluar con Paid y contratarlo él mismo, o revisar una alternativa documentada de alojamiento Django. No cambiar proveedor ni debilitar PBKDF2/TLS para forzar Free. No hubo compra, cambio de plan, DNS/dominio, commit, push ni eliminación de recursos. Conservar recursos para diagnóstico hasta instrucción del usuario.

Fuentes: [Precio Workers](https://developers.cloudflare.com/workers/platform/pricing/), [límites Workers](https://developers.cloudflare.com/workers/platform/limits/), [TLS Hyperdrive](https://developers.cloudflare.com/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/).
