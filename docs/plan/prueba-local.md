# Guía de la prueba local

Estado: verificado localmente el 7 de octubre de 2026. Esta guía no configura Supabase ni Cloudflare.

## Iniciar y revisar

Desde Terminal:

```sh
cd /Users/danilo/Documents/Serigrafia-Web
.venv/bin/python scripts/local.py db-start
.venv/bin/python scripts/local.py migrate
.venv/bin/python scripts/local.py role
.venv/bin/python scripts/local.py serve
```

El último comando mantiene el servidor abierto. Si ya está iniciado, no ejecutar otra instancia. Abrir http://127.0.0.1:8000/ para el catálogo y http://127.0.0.1:8000/admin/ para el panel.

## Crear tu acceso local

En otra terminal, ejecutar una vez:

```sh
cd /Users/danilo/Documents/Serigrafia-Web
.venv/bin/python scripts/local.py admin
```

Ingresar usuario y contraseña en la terminal. No existe una cuenta administrativa predeterminada. Este superusuario sirve para configurar la prueba. Para un responsable del catálogo, crear un usuario desde el panel, activar «Es staff», asignar el grupo «Responsable de catálogo» y mantener «Es superusuario» desactivado. El grupo permite consultar, crear y editar productos; no borrar ni administrar usuarios.

Crear un producto, agregar una foto válida y activar «Publicado». Guardar y revisar el catálogo. Desactivar «Publicado» para ocultarlo. Las tallas se ingresan como una lista JSON, por ejemplo `["S", "M", "L"]`; esta interfaz provisional se ajustará con los materiales reales.

## Verificación reproducible

```sh
.venv/bin/python scripts/local.py check
.venv/bin/python scripts/local.py test
.venv/bin/python scripts/local.py persistencia
```

El último comando asegura un producto ficticio con foto de prueba y lo consulta desde otro proceso. Registra versiones y hash de la imagen en `.local/persistencia.json`, sin credenciales. No demuestra recuperación de respaldo ni compatibilidad con Workers.

Resultado de esta sesión: 10 pruebas pasaron en PostgreSQL 16.14, validando permisos, operaciones del panel, fotos, archivos inválidos, tallas, escape HTML y CSRF. Catálogo y foto visibles en navegador; acceso anónimo al panel redirige al login.

## Datos locales y cierre

- PostgreSQL: contenedor `serigrafia-web-postgres`, puerto `127.0.0.1:55439`, base `serigrafia_local`, volumen `serigrafia-web_postgres_local`.
- Credencial generada exclusivamente para esta prueba en `.local/postgres.env`, con permisos restringidos. No compartir ni incluir en Git.
- Fotos: `.local/media/`; deben preservarse por separado del volumen PostgreSQL.
- Dependencias: `.venv/` y versiones fijadas en `requirements.txt`.
- Imagen Docker oficial ya presente; el inicio no descarga imágenes. Se mantuvieron los demás proyectos de Docker separados.
- El reemplazo de foto no elimina automáticamente el archivo anterior; falta definir limpieza para el almacenamiento definitivo.

Detener el servidor con Ctrl+C en su terminal y detener únicamente esta base con:

```sh
.venv/bin/python scripts/local.py db-stop
```

El comando conserva el volumen. No usar opciones que borren volúmenes si se desean preservar datos.

## Pendiente

Integración de Supabase/PostgreSQL y Storage con Django en Workers; diseño y materiales reales; formulario WhatsApp; galería; revisión móvil; respaldo; capacitación y publicación autorizada. Las pruebas locales no completan los criterios de aceptación del alojamiento final.
