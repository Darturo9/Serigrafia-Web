#!/usr/bin/env python3
"""Genera inventario y SQL de revisión utilizando SOLO PostgreSQL local."""
import os
from pathlib import Path
import sys
from io import StringIO

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
secret_file = ROOT / ".local" / "postgres.env"
if not secret_file.exists():
    raise SystemExit("Primero preparar PostgreSQL local.")
password = secret_file.read_text().strip().partition("=")[2]
os.environ.update(DJANGO_SETTINGS_MODULE="config.settings", DB_BACKEND="postgres", PGHOST="127.0.0.1",
                  PGPORT="55439", PGDATABASE="serigrafia_local", PGUSER="serigrafia_local",
                  PGPASSWORD=password, PGSSLMODE="disable")
import django
django.setup()
from django.db import connection
from django.db.migrations.loader import MigrationLoader
from django.core.management import call_command

assert connection.settings_dict["HOST"] == "127.0.0.1"
loader = MigrationLoader(connection=None)
order = []
for leaf in loader.graph.leaf_nodes():
    for node in loader.graph.forwards_plan(leaf):
        if node not in order:
            order.append(node)
lines = ["# Migraciones de la aplicación existente", "", "Generado para revisión, no aplicado en remoto.",
         "", "Destino propuesto: esquema jyz_prueba en el proyecto kcahxuvfmrzxzlnpezyf.", "",
         "Orden derivado del grafo de Django; incluye migraciones Python y post_migrate.",
         "Aplicar con migrate en entorno autorizado, nunca ejecutando este inventario como SQL.", ""]
for app, name in order:
    migration = loader.get_migration(app, name)
    lines.append(f"- `{app}.{name}`: " + ", ".join(type(op).__name__ for op in migration.operations))
lines += ["", "El SQL del catálogo se entrega por separado. Usuarios/permisos/grupo requieren los pasos",
          "Django correspondientes. No copiar credenciales ni datos locales automáticamente.", ""]
(ROOT / "ops" / "migraciones-django.md").write_text("\n".join(lines))
stream = StringIO()
call_command("sqlmigrate", "catalogo", "0001", stdout=stream)
(ROOT / "ops" / "catalogo-0001.revision.sql").write_text(
    "-- REVISIÓN: SQL generado contra PostgreSQL local. No aplicar directamente en remoto.\n"
    "-- El esquema remoto se fija al ejecutar migrate con search_path=jyz_prueba.\n" + stream.getvalue())
print(f"Inventario de {len(order)} migraciones y SQL del catálogo preparados; sin cambios de base.")
