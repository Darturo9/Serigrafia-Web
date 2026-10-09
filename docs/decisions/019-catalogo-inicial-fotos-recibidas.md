# ADR 019. Catálogo inicial con fotos recibidas

Fecha: 8 de octubre de 2026. Solicitud directa: incorporar fotos de /Users/danilo/Documents/fotos galeria jyz al catálogo público, mejorar las pixeladas mediante GPT Imagen 2.5, mostrar todas las tallas y entregar usuario/contraseña Admin por chat.

La carpeta contiene 17 archivos, 16 únicos por SHA-256; conservar originales y duplicado sin repetir ficha. Crear una ficha por foto única, nombres/descripciones visuales sin precios, material, técnica ni stock inventados. Usuario autoriza publicación de estas fotos como catálogo; galería y registros anteriores conservados. Todas las tallas se registra como opción general ["Todas las tallas"], sin inventar rango XS/XXL, infantil/adulto ni medidas. El formulario ofrece texto opcional para tallas solicitadas, manteniendo validaciones existentes para listas concretas. Precio/medidas/entrega se conversan en WhatsApp.

El generador integrado no ofrece selector de modelo ni confirmación GPT Imagen 2.5; comunicar esa limitación. Probar restauración en copias de mockups claramente pixelados, preservar estampados y no publicar resultados que cambien el diseño. Imagen original permanece como fuente si la restauración no conserva fidelidad. Reducir copias de más de 16 megapíxeles antes del backend existente, sin modificar originales.

Autoriza cargas nuevas y altas de productos exclusivamente en Supabase kcahxuvfmrzxzlnpezyf, jyz_prueba/bucket existente y despliegue de código exclusivo JYZ; sin migraciones, cambios de permisos, borrar, comprar, instalar, DNS, commit/push ni proyectos ajenos. Verificar catálogo/fichas/fotos/mensaje HTTPS y sesión/permisos de la cuenta existente. Entrega de credenciales del panel por chat autorizada explícitamente; nunca claves de servidor/Supabase/PostgreSQL.

## Instrucción posterior vigente

El usuario acepta inicialmente la herramienta disponible y, tras rechazos de generación moderation_blocked/output/categoría other sin explicación específica, indica: «entonces solo usa las que no esten pixeleadas». Sustituye la mejora IA por selección visual: 11 aceptadas, cinco excluidas por pixelación de las 16 únicas; duplicado omitido. Se revisó individualmente cada foto. No se publican resultados IA ni las cinco excluidas. Originales conservados. Selección/hash/justificación en assets/catalogo-recibido/seleccion.json.
