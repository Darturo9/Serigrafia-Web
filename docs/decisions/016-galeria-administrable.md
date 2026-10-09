# ADR 016. Galería administrable

Fecha: 8 de octubre de 2026. Estado: módulo y paquete remoto autorizados; implementados y verificados en Railway/Supabase.

El usuario aprueba administrar «Ideas que toman forma» desde Django Admin: subir fotografías, editar título/descripción, ordenar y mostrar/ocultar. Se mantiene separada de productos y cotizaciones. No se crea panel personalizado ni API.

GaleriaImagen contiene título, descripción accesible de la imagen, foto requerida, orden, visible y actualización. Las nuevas cargas usan el mismo Storage privado y optimización WebP de ADR 007. Lista con miniatura y visibilidad; permisos de ver/agregar/cambiar para el responsable de catálogo, sin borrar ni administrar usuarios. Ocultar conserva registro y archivo. Los reemplazos conservan objetos anteriores; una carga fallida revierte la edición y muestra un aviso.

Inicio consulta únicamente fotos visibles, ordenadas por orden y clave. Sin fotos visibles se omite la sección y el enlace «Trabajos», sin reintroducir imágenes estáticas ni ejemplos. Ante una foto inaccesible se omite esa foto, manteniendo el resto de la página.

Las tres fotos entregadas deben cargarse como registros iniciales, preservando originales y referencias estáticas. La preparación incluye una migración aditiva, rol ampliado con tres permisos de galería y carga inicial idempotente. No se cambia ningún producto.

Aplicación remota propuesta: catalogo.0004 en jyz_prueba (kcahxuvfmrzxzlnpezyf), RLS en tabla privada, permisos del rol existente, tres cargas al bucket privado jyz-prueba-fotos y despliegue únicamente jyz-web/jyz-revision. Sin nuevas compras, recursos, borrado, commit/push ni cambios en vibrant-perfection. Antes de pedir aprobación: implementación, pruebas, SQL y capturas locales terminados.

Verificar A02/A05/A10/A11/A12: edición/orden/ocultación en Admin reflejadas públicamente, permisos negativos, imagen inválida y fallo de Storage conservan estado, optimización WebP y continuidad de las tres fotos actuales. La prueba local no acredita aplicación remota.

Aplicación remota terminada el 8 de octubre: catalogo.0004, RLS/permisos acotados, tres registros/fotos privadas y despliegue 324fc0e1-108a-4519-b15e-1c5e1a120208 SUCCESS. Edición/orden/ocultación reflejados por HTTPS y valores restaurados; productos y objetos anteriores preservados. Ver resultado y límites en [galería administrable](../plan/galeria-administrable.md). Capacitación del dueño continúa pendiente.
