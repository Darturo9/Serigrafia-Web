# ADR 015. La raíz muestra el inicio

Fecha: 8 de octubre de 2026. El usuario detecta que `/` mostraba «Productos publicados» (catálogo técnico de la prueba inicial) en vez del inicio.

`/` sirve la página de inicio (nombre de URL `inicio`); `/inicio/` se conserva como alias. El catálogo técnico pasa a `/catalogo/` y en Railway exige la clave de revisión, igual que `/admin`. Django Admin «Ver sitio» apunta a `/`. Scripts locales/Workers que usaban `/` como catálogo técnico apuntan a `/catalogo/`.
