# Galería administrable — implementada y verificada

Fecha: 8 octubre 2026. ADR 016. Módulo y paquete remoto autorizados; aplicación y verificación terminadas. Los apartados de preparación siguientes conservan la evidencia anterior a la autorización; el resultado vigente está al final.

## Resultado local

- Admin → Galería: miniaturas, búsqueda, filtros, título y descripción, foto, orden y visible. Orden y visible también editables desde la lista.
- Nueva foto requerida, validación JPEG/PNG/WebP y límites existentes; usa la misma conversión WebP de Storage. No se reconstruyen diseños mediante IA.
- Sección pública lee registros visibles por orden; descripción visible y texto accesible. Galería vacía/inaccesible omite sección/enlace, sin restaurar fotos de referencia.
- Rol Responsable de catálogo: nueve permisos de productos/fotos/galería, sin borrado ni administración de usuarios. El Admin de galería tampoco permite borrar con superusuario.
- Reemplazos/ocultación conservan objetos anteriores. Fallos de Storage revierten la edición y muestran aviso. La carga inicial es transaccional y no modifica ni duplica una galería ya existente; un fallo parcial conserva objetos subidos para revisión, sin limpieza automática.
- Tres originales actuales cargados solo en demo SQLite aislada, sin cambiar productos. Demo http://127.0.0.1:8003/admin/ mientras el proceso esté activo; usuario exclusivamente local.

61 pruebas SQLite aprobadas (catálogo, Railway, runtime simulado), siete específicas de galería: edición/orden/ocultación, vacío, permisos negativos, imagen corrupta/fallo de carga, foto inaccesible/texto escapado, repetición de carga inicial y conversión WebP 2000×1000→1600×800 sin HTTP real. Salida `.local/jyz-fotos/galeria-tests-final.txt`. Navegador local verificó título/orden y ocultación desde la lista reflejados en inicio; los valores de demo se restauraron. Captura `.local/design-review/galeria-admin-local.png`.

Docker local estaba apagado: no se pudo ejecutar PostgreSQL local. SQL de tabla generado sin conexión con el backend PostgreSQL de Django; revisión estática, no prueba contra PostgreSQL. `makemigrations --check --dry-run`: sin cambios faltantes. Lectura OAuth Supabase: cuatro productos/cuatro imágenes, tabla de galería inexistente. Privilegios por defecto de jyz_migrator para jyz_app confirmados y política actual del catálogo consultada; ninguna escritura remota.

## Paquete remoto exacto para aprobar

1. Aplicar únicamente `catalogo.0004_galeriaimagen` mediante Django, rol `jyz_migrator`, search_path `jyz_prueba`, Supabase `kcahxuvfmrzxzlnpezyf`. Crea una tabla; no transforma ni borra datos actuales. Revisar `ops/catalogo-0004-galeria.revision.sql`.
2. Activar RLS en tabla nueva, política exclusiva del rol de servidor jyz_app equivalente a la existente y revocar DELETE de esta tabla a jyz_app. Esquema privado sin acceso cliente. SQL preparado en `ops/galeria-permisos.revision.sql`; no modifica políticas de productos.
3. Ejecutar `preparar_rol_catalogo` para agregar únicamente view/add/change de galería al grupo existente; mantiene sus seis permisos anteriores. No cambiar usuarios ni contraseñas.
4. Ejecutar `cargar_galeria_inicial --aplicar` con perfil Supabase jyz_app desde el entorno local autorizado: tres registros y tres fotos reales en bucket privado `jyz-prueba-fotos`. Descripciones/títulos como la galería actual. Conservar originales estáticos y archivos actuales; sin tocar productos.
5. Subir el paquete `.local/railway-galeria` exclusivamente a proyecto JYZ `db6b6a44-0a60-4ae3-b8b3-5bb4c309bc6a`, servicio `bf4d7246-eda6-4265-b649-695fa2fd5991`. Comparar paquete completo con fuentes vigentes antes de subir; conservar ADR 013/014/015, iconos y footer. No usar vibrant-perfection.
6. Verificar HTTPS anónimo inicio/fichas 200 y Admin 401; Admin autenticado permite galería y rechaza usuarios/borrado. Confirmar tres fotos firmadas, WebP/MIME/peso, edición/orden/ocultación y restauración de valores iniciales, y que referencias/productos anteriores continúan intactos. Sin enviar WhatsApp.

No se aplicaron migraciones, permisos, cargas ni despliegue de este paquete. Si falla la aplicación, conservar objetos/registros y volver al código estable sin borrar tabla ni datos. La web publicada sigue con la galería estática de tres fotos reales.

## Documentación técnica consultada

[Storage: carga estándar](https://supabase.com/docs/guides/storage/uploads/standard-uploads) y [changelog](https://supabase.com/changelog), incluido [PostgreSQL 15.19/17.11](https://supabase.com/changelog/postgres-15-19-17-11-breaking-changes). No se introduce SDK ni se actualiza versión del servidor; se reutiliza backend privado probado. Consultadas como documentación, no como evidencia de prueba remota.

## Verificación remota de galería preparada

Continúa pendiente la respuesta a la confirmación específica del paquete remoto. Se preparó scripts/railway_galeria_probe.py: acceso público/protecciones, tres fotos privadas WebP con límites, sesión del editor, formularios, lista editable y rechazo de borrado/usuarios. Compilación Python aprobada. No se ejecutó contra remoto porque la tabla/rol/versión nueva todavía no se aplicaron; esta preparación no es evidencia HTTPS. El script no cambia fotos/textos/datos, solo inicia/cierra sesión y registra resultados sin URLs firmadas/credenciales. Edición remota y preservación de fotos anteriores requieren comprobación separada tras autorización. Sin migración, cargas, despliegue, commit/push ni cambios en vibrant-perfection.

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
