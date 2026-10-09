# ADR 008. Identidad visual del panel JYZ

Fecha: 8 de octubre de 2026. Estado: autorizado por «Procede»; implementación verificada localmente y por HTTPS en Railway; aprobación visual humana pendiente.

Personalizar Django Admin existente para lista, edición, entrada y portada: logo recibido, naranja/tinta/papel y fuentes locales; miniaturas, estados textuales y campos agrupados. Una persona del negocio actualiza prendas durante el día en computadora o teléfono: usar superficies claras en modo claro, conservar modo oscuro, controles familiares y acentos de marca. Antonio solo para encabezados, Barlow para controles y lectura.

Retirar nombres históricos «prueba local» del panel sin transformar productos sintéticos en reales. Mantener permisos, CSRF, sesiones, validaciones, rollback y WebP existentes. Sin nuevo panel, API, dependencias o migraciones. Miniaturas privadas mediante URLs firmadas y error comprensible si Storage falla. No eliminar fotos ni datos. Revisar visualmente esta propuesta antes de extender a otras superficies.

La instrucción pide además explicar pendientes para presentar el sitio funcional; no autoriza retirar la protección, publicar ejemplos como reales, comprar dominio ni borrar recursos. Mantener el dominio Railway aprobado y vibrant-perfection intacto. Vinculado a R07/R08/R09/R10 y A02/A05/A10/A12.

## Evidencia local

43 pruebas existentes pasan; check sin errores. Portada/lista/ficha vistas en navegador integrado, miniaturas cargadas y bloques de formulario presentes. Sin desbordamiento de página en 320/390 px; la tabla conserva desplazamiento horizontal propio. Modos claro y oscuro inspeccionados visualmente; no equivale a auditoría WCAG ni teléfono físico. Capturas locales en .local/design-review/admin-jyz-*.png. Se mantienen productos sintéticos claramente identificados.

## Evidencia remota

Versión a8450427-575e-47cf-8e48-8431a305ee23 SUCCESS; once comprobaciones HTTPS aprobadas con script railway_admin_design_probe.py y resultado admin-jyz-http.json. CSS/fuentes, login, portada/lista/ficha y restricciones comprobados. Capturas visuales locales; aprobación del usuario pendiente. No se edita contenido comercial ni se retira protección.
