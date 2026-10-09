"""Carga las tres fotos recibidas solo si la galería está vacía; no elimina objetos."""
import logging
from pathlib import Path
from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from catalogo.models import GaleriaImagen

FOTOS = (
    ("playera-blanca-ilustracion.jpeg", "Ilustración y color.", "Playera blanca con ilustración de personajes y fondo azul, verde y amarillo"),
    ("playera-negra-oliver-tree.jpeg", "Diseños que se expresan.", "Playera negra con estampado de Oliver Tree y retrato sobre fondo azul"),
    ("playera-negra-wos.jpeg", "Estampados con carácter.", "Playera negra con ilustración de una boca y texto WOS, Oscuro Éxtasis"),
)


class Command(BaseCommand):
    help = "Prepara o carga las tres fotos entregadas. Requiere --aplicar para escribir."

    def add_arguments(self, parser):
        parser.add_argument("--aplicar", action="store_true")
        parser.add_argument("--directorio", type=Path, default=settings.BASE_DIR / "assets/jyz-fotos-recibidas")

    def handle(self, *args, **options):
        if GaleriaImagen.objects.exists():
            self.stdout.write("La galería ya contiene fotos; no se modifica ni duplica contenido.")
            return
        folder = options["directorio"]
        if any(not (folder / name).is_file() for name, _, _ in FOTOS):
            raise CommandError("Faltan las tres fotos originales; no se carga contenido parcial.")
        if not options["aplicar"]:
            self.stdout.write("Preparadas tres fotos; sin escrituras. Use --aplicar únicamente en el entorno autorizado.")
            return
        uploaded = []
        try:
            with transaction.atomic():
                for orden, (name, title, description) in enumerate(FOTOS):
                    image = GaleriaImagen(titulo=title, descripcion=description, orden=orden, activo=True)
                    with (folder / name).open("rb") as stream:
                        image.foto.save(name, File(stream), save=False)
                    uploaded.append(image.foto.name)
                    image.full_clean()
                    image.save()
        except Exception:
            if uploaded:
                logging.getLogger("catalogo.admin").warning("Carga inicial revertida; objetos conservados para revisión: %s", uploaded)
            raise
        self.stdout.write("Tres fotos registradas. Archivos originales conservados.")
