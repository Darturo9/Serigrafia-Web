# Prueba de Django en Railway

Fecha: 8 de octubre de 2026. Estado vigente: Hobby activo; paquete de revisión autorizado y desplegado en jyz-revision/jyz-web, con tres versiones y prueba técnica HTTP/persistencia aprobadas. El usuario eligió build directamente en Railway, sin instalación local. Ver evidencia-railway-prueba.md. Compras/cambio de plan por el agente excluidos; los pasos siguientes documentan el plan y su historial.

## Preparación local siguiente

1. Crear un perfil de settings nativo independiente de Workers y del perfil Mac de Supabase. Reutilizar settings compartidos y backend Storage existentes. Exigir secretos por entorno, DEBUG=False, host/CSRF concretos, cookies seguras y configuración de HTTPS detrás del proxy.
2. Conectar psycopg con el rol limitado jyz_app al pooler autorizado, esquema jyz_prueba, TLS verify-full y CA pública. Conservar bucket privado jyz-prueba-fotos y proyecto kcahxuvfmrzxzlnpezyf. No usar rol migrador para servir peticiones.
3. Preparar Gunicorn/WhiteNoise con versiones fijadas, collectstatic, arranque en el PORT proporcionado y configuración Railway o Docker revisable. No instalar dependencias nuevas sin autorización. Excluir .local, .env, claves, entornos, paquetes WASM y referencias ajenas al runtime del contexto de construcción.
4. Añadir protección de revisión a todo el sitio y assets, noindex y comprobación de salud sin secretos. La protección de Worker no existe en Railway: debe implementarse en el servidor nativo. Probar orden del middleware, login/CSRF y assets del Admin.
5. Comprobar configuración y paquete localmente, con datos sintéticos y sin escrituras remotas adicionales. Presentar archivos, comandos, variables, destino y límites antes de solicitar ejecución remota.

La configuración de despliegue no incluirá migrate automático ni creará administradores al arrancar. Las fotos y sesiones no dependerán del disco efímero del servicio. La CA es pública; las contraseñas y clave Storage se transfieren únicamente por configuración segura del servidor.

## Paquete remoto autorizado, pendiente de plan activo y comprobación local

El usuario informó que ya pagó Railway. Verificar el plan activo y crear JYZ separado. **Nunca borrar ni modificar `vibrant-perfection`, ID 53241be7-2641-4ab2-9ac5-82c3943af5fa**, ni sus servicios bot-AI/Redis. Es una instrucción expresa del usuario, no un recurso disponible para la prueba.

- Identificar cuenta/workspace, plan, titularidad y presupuesto disponible; no cambiar suscripción ni comprar.
- Crear un único servicio Django de revisión en un proyecto/entorno acordado, sin base ni volumen Railway nuevos.
- Cargar secretos de servidor: Django, credenciales del rol jyz_app, Storage y acceso de revisión; configurar origen HTTPS/hosts/CSRF y CA pública. No cargar el rol migrador.
- Realizar primer despliegue protegido mediante CLI local o GitHub. GitHub requiere primero commit/push autorizados; la elección de Railway no los autoriza.
- Ejecutar A02–A05 y A11 parciales con producto/fotos sintéticos; esto requiere autorización explícita para esas escrituras en el destino existente.
- Realizar segundo despliegue y verificar A06: datos, fotos y acceso conservados. Medir arranque, memoria, CPU, errores y costo observado; no confundir mínimo del plan con factura estimada.
- Registrar resultados y límites; cualquier SQL/migración, compra, dominio/DNS, borrado de recursos o lanzamiento comercial requiere autorización independiente.

## Evidencia requerida

| Criterio | Comprobación |
|---|---|
| A02 | Revisión restringida, login/logout, sesión, CSRF y permisos de catálogo |
| A03–A04 | Crear/editar, publicar/ocultar ejemplo y comprobar catálogo |
| A05/A11 | PNG/JPEG/WebP, rechazo de archivo inválido y conservación de foto ante fallo |
| A06 | Releer datos y fotos después del segundo despliegue |
| A13 parcial | TLS, secretos de servidor, logs sin credenciales y recursos/costos observados |

Pendientes comerciales y aceptación visual/móvil permanecen separados. Esta prueba no publica productos ficticios como reales ni envía WhatsApp automáticamente.

Fuentes consultadas: [Django en Railway](https://docs.railway.com/guides/django), [planes y consumo](https://docs.railway.com/pricing/plans). Documentación consultada no equivale a integración probada.
