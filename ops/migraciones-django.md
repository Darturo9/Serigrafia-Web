# Migraciones de la aplicación existente

Generado para revisión, no aplicado en remoto.

Destino propuesto: esquema jyz_prueba en el proyecto kcahxuvfmrzxzlnpezyf.

Orden derivado del grafo de Django; incluye migraciones Python y post_migrate.
Aplicar con migrate en entorno autorizado, nunca ejecutando este inventario como SQL.

- `contenttypes.0001_initial`: CreateModel, AlterUniqueTogether
- `auth.0001_initial`: CreateModel, CreateModel, CreateModel
- `admin.0001_initial`: CreateModel
- `admin.0002_logentry_remove_auto_add`: AlterField
- `admin.0003_logentry_add_action_flag_choices`: AlterField
- `contenttypes.0002_remove_content_type_name`: AlterModelOptions, AlterField, RunPython, RemoveField
- `auth.0002_alter_permission_name_max_length`: AlterField
- `auth.0003_alter_user_email_max_length`: AlterField
- `auth.0004_alter_user_username_opts`: AlterField
- `auth.0005_alter_user_last_login_null`: AlterField
- `auth.0006_require_contenttypes_0002`:
- `auth.0007_alter_validators_add_error_messages`: AlterField
- `auth.0008_alter_user_username_max_length`: AlterField
- `auth.0009_alter_user_last_name_max_length`: AlterField
- `auth.0010_alter_group_name_max_length`: AlterField
- `auth.0011_update_proxy_permissions`: RunPython
- `auth.0012_alter_user_first_name_max_length`: AlterField
- `catalogo.0001_initial`: CreateModel
- `sessions.0001_initial`: CreateModel

El SQL del catálogo se entrega por separado. Usuarios/permisos/grupo requieren los pasos
Django correspondientes. No copiar credenciales ni datos locales automáticamente.
