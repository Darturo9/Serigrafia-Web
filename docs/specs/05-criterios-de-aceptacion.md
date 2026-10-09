# 05. Criterios de aceptación

Estado vigente: A02–A06 tienen evidencia técnica de HTTP real en Railway con Supabase y persistencia tras segundo despliegue, con datos sintéticos; ver ../plan/evidencia-railway-prueba.md. A11/A13 solo parciales. Revisión humana final y aceptación comercial A01–A13 pendientes. Los registros locales/Workers posteriores se conservan como historial.

| ID | Requisitos | Comprobación | Resultado esperado |
|---|---|---|---|
| A01 | R01, R06 | Revisar textos, logo, fotos y contactos | Contenido confirmado, sin información ficticia publicada |
| A02 | R07 | Entrar sin sesión y con usuario autorizado | Acceso restringido y solo permisos necesarios |
| A03 | R02, R08 | Crear y editar un producto | Datos guardados y visibles correctamente en catálogo |
| A04 | R02, R08 | Ocultar y volver a publicar | El producto aparece solo cuando está publicado |
| A05 | R08 | Cargar/reemplazar foto válida y rechazar archivo inválido | Foto correcta y error comprensible sin perder la anterior |
| A06 | R02, R08 | Reiniciar o desplegar de nuevo | Datos y fotos conservados |
| A07 | R03 | Solicitud válida con acentos y tallas | WhatsApp correcto y mensaje legible, sin envío automático |
| A08 | R03 | Cantidad inválida o tallas que no suman | Mensaje de validación y corrección antes de continuar |
| A09 | R04, R05 | Diseño y contacto | Diseño se adjunta en WhatsApp; contacto desde footer sin formulario ni estados de seguimiento (ADR 010) |
| A10 | R09 | Celular, computadora y teclado | Contenido legible, navegación y formularios utilizables |
| A11 | R02, R08 | Catálogo vacío, producto ocultado y fallo de almacenamiento | Estado comprensible y ninguna promesa de disponibilidad falsa |
| A12 | R10 | Persona del negocio actualiza producto siguiendo guía | Puede actualizar y verificar el catálogo con su acceso |
| A13 | Todos | Revisar configuración antes de lanzamiento | Dominio, planes, responsables, recuperación y permisos confirmados |

## Evidencia

Para cada comprobación registrar fecha, entorno, resultado, captura o salida pertinente y limitaciones en estado/tareas. No poner contraseñas ni tokens en evidencias.

La prueba técnica de alojamiento cubre A02–A06 y partes de A11/A13 en un entorno autorizado; ver `../plan/prueba-alojamiento.md`. A07 corresponde a WhatsApp y tiene +502 confirmado; necesita implementación y prueba del recorrido. Si no pasa, documentar el bloqueo y revisar la arquitectura antes de extender la implementación.

## Publicación

Requiere contenido real, enlaces válidos, comprobaciones aprobadas, costos y acceso a cuentas acordados, revisión final y autorización de publicación. La documentación compartida asigna revisión a Henry y gestión de publicación a Roger, sujetos a confirmar su coordinación.

Workers local: 25 comprobaciones HTTP y 21 pruebas nativas aportan evidencia adicional a A02–A05 y partes de A11/A13. Fotos en memoria: A06 remoto permanece pendiente. Ver ../plan/evidencia-workers-local.md; no sustituye revisión visual ni aceptación final.

## Evidencia adicional — 8 de octubre de 2026

Supabase autorizado y probado desde Django nativo: 19 migraciones, 11 tablas protegidas con RLS en esquema no expuesto por Data API, bucket privado, carga/lectura PNG/JPEG/WebP y 14 comprobaciones del panel aprobadas. A02–A05 tienen evidencia adicional con datos remotos; A06 solo lectura desde segundo proceso. Workers/Hyperdrive remoto, redespliegue y aceptación final siguen pendientes. Ver [evidencia Supabase](../plan/evidencia-supabase-prueba.md). Suite nativa local actual: 31 pruebas; no confundir con las 25 comprobaciones HTTP Workers previas.

## Auditoría de aceptación vigente

Ver [revisión criterio por criterio](../plan/revision-aceptacion-railway.md). A07/A08 tienen evidencia HTTP adicional y A10 evidencia adaptable local parcial. A12 conserva capacitación pendiente aunque la guía esté actualizada. Dueño confirmado como administrador previsto; WhatsApp/roles nominales y contenido real todavía faltan.

## Optimización y dominio — evidencia vigente

ADR 007: 43 pruebas locales y carga HTTPS Admin de una foto de ejemplo prueban conversión WebP, límite de salida y conservación de foto ante reemplazo inválido. Resultado remoto: 399222 → 49098 bytes, 1600 × 1067 px, MIME image/webp; objeto previo conservado. Evidencia .local/railway-prueba/webp-http.json. Esto amplía A05/A11 técnicos, no sustituye aceptación comercial ni revisión humana.

A13 admite el dominio predeterminado jyz-web-production.up.railway.app por decisión expresa del usuario. Comprar/conectar un dominio propio queda aplazado y no bloquea la web funcional.

## Galería administrable aprobada — ADR 016

El usuario aprueba administrar fotos de «Ideas que toman forma» desde Django Admin, separadas del catálogo: título/descripción, foto, orden y visible. Backend privado/WebP existente; permisos ver/agregar/cambiar sin borrar. GaleriaImagen y migración 0004 aplicados con autorización en Supabase; carga inicial conserva las tres fotos entregadas. Edición/orden/ocultación verificados por HTTPS en Railway, valores iniciales restaurados y productos/objetos anteriores conservados. Inicio consulta solo visibles; si no hay fotos disponibles omite sección y enlace. A02/A05/A10/A11/A12 requieren edición pública reflejada, permisos negativos y conservación ante fallos; pruebas locales no sustituyen aplicación remota. Ver [paquete y evidencia](../plan/galeria-administrable.md).

## Entrega operativa autorizada — ADR 017

El usuario difiere el catálogo real hasta recibir el sitio y autoriza avanzar con el resto: cuenta Mryoan acotada, ocultación de fichas sintéticas conservando datos/fotos, revisión técnica móvil, respaldo cifrado y recuperación PostgreSQL local aislada, guía y despliegue público sin avisos/noindex de revisión. Catálogo comercial deja de ser requisito previo de esta entrega. No se asumen realizadas capacitación humana ni prueba en teléfono físico; se registrará evidencia técnica y lo pendiente del negocio. No compra, DNS, borrados, commit/push ni cambios en vibrant-perfection necesarios.

## Confirmación humana ADR 017

El usuario confirmó revisión física en teléfono (galería y apertura WhatsApp) y práctica del responsable con Mryoan (entrar, ordenar, ocultar y volver a mostrar una foto comprobando la web). A10 y práctica inicial de administración tienen evidencia humana. El ejercicio A12 con productos comerciales se difiere hasta la carga del catálogo después de recibir el sitio, por instrucción directa del usuario. Primera copia/recuperación real comprobada; no afirmar backups automáticos/custodia externa completados.

## Vista previa al compartir — ADR 018

A01/A13: inicio y fichas públicas incluyen título, descripción y og:image absoluto con logo confirmado bajo https://jyzgt.com. El JPEG responde 200 anónimo, MIME/dimensiones correctos; raíz/alias conservan canónica raíz y fichas su ruta, sin datos del formulario. Verificación de HTML/recurso no sustituye la vista previa real en WhatsApp.

## Catálogo inicial verificado — ADR 019

A01/A03/A05/A07/A08/A10: once fotos seleccionadas tras revisión individual publicadas en fichas nuevas, sin precios y con todas las tallas generales; cinco pixeladas excluidas por instrucción posterior. Once GET/fotos/POST HTTPS aprobados con hashes y tallas libres; 53 pruebas locales y revisión visual en navegador, sin enviar WhatsApp. Admin conserva permisos y los cuatro productos/fotos previos y galería se mantienen idénticos. Ver registro final y selección.json.

## Acceso vigente al panel — ADR 020

El usuario solicita un solo login: HTTP Basic retirado de Admin y sus estáticos; Django mantiene autenticación, sesiones, CSRF, HTTPS, noindex y permisos. Anónimo redirige desde panel/listas al login; login/formulario y estilos accesibles. Mryoan conserva permisos acotados. Verificar login real sin Basic y denegación de usuarios/borrado.


## Cambio aprobado — ADR 021

Trabajos y su enlace de navegación quedan comentados temporalmente mediante etiquetas Django. La página pública no debe emitir la sección, su enlace ni las fotos de galería. Galería sigue disponible en Admin y sus archivos/registros se conservan.
