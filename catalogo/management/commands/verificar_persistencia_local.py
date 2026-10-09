import hashlib
import json
from pathlib import Path
import subprocess
import sys
import django
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection
from django.test import Client
from catalogo.models import Producto
from .crear_demo_local import exigir_base_local

class Command(BaseCommand):
    help = "Verifica producto y foto en un segundo proceso, sin tocar servicios externos."

    def add_arguments(self, parser):
        parser.add_argument("--read-only", action="store_true")

    def handle(self, *args, **options):
        exigir_base_local()
        if not options["read_only"]:
            call_command("crear_demo_local")
        product = Producto.objects.get(nombre="Producto de prueba local", es_ejemplo=True)
        assert product.publicado, "El producto de ejemplo debe estar publicado."
        photo_bytes = Path(product.foto.path).read_bytes()
        digest = hashlib.sha256(photo_bytes).hexdigest()
        response = Client().get("/catalogo/", HTTP_HOST="localhost")
        assert response.status_code == 200
        assert product.nombre.encode() in response.content
        assert product.foto.url.encode() in response.content
        if options["read_only"]:
            self.stdout.write(digest)
            return
        child = subprocess.run([sys.executable, str(settings.BASE_DIR / "manage.py"), "verificar_persistencia_local", "--read-only"], check=True, capture_output=True, text=True)
        assert child.stdout.strip() == digest, "La foto cambió al leer desde otro proceso."
        with connection.cursor() as cursor:
            cursor.execute("SHOW server_version")
            version = cursor.fetchone()[0]
        result = {"estado": "verificado localmente", "python": sys.version.split()[0], "django": django.get_version(), "postgresql": version, "base": "serigrafia_local", "producto": product.pk, "foto_sha256": digest, "segundo_proceso": True, "catalogo_http": 200, "workers": "pendiente", "supabase": "pendiente"}
        report = settings.BASE_DIR / ".local" / "persistencia.json"
        report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        self.stdout.write(self.style.SUCCESS("Verificada persistencia PostgreSQL y foto en un segundo proceso local."))
