from io import BytesIO
from PIL import Image, ImageDraw
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import Producto


def exigir_base_local():
    database = settings.DATABASES["default"]
    if not settings.DEBUG or database["ENGINE"] != "django.db.backends.postgresql" or database["NAME"] != "serigrafia_local" or database["HOST"] != "127.0.0.1" or str(database["PORT"]) != "55439":
        raise CommandError("Este comando solo admite PostgreSQL local de Serigrafia-Web.")


class Command(BaseCommand):
    help = "Crea un producto claramente marcado como ejemplo, únicamente en la base local."

    def handle(self, *args, **options):
        exigir_base_local()
        product, created = Producto.objects.get_or_create(nombre="Producto de prueba local", es_ejemplo=True, defaults={"descripcion": "Dato de ejemplo para verificar Django Admin, PostgreSQL y fotos. No representa un producto del emprendimiento.", "tallas": ["S", "M", "L"], "publicado": True})
        if created:
            image = Image.new("RGB", (640, 400), "#e5e5e5")
            ImageDraw.Draw(image).text((40, 180), "PRUEBA LOCAL / SIN FOTO COMERCIAL", fill="#333333", font_size=25)
            buffer = BytesIO()
            image.save(buffer, format="PNG")
            product.foto.save("prueba-local.png", ContentFile(buffer.getvalue()), save=False)
            product.texto_foto = "Imagen de prueba local, no corresponde al emprendimiento"
            product.save()
        self.stdout.write(self.style.SUCCESS("Producto de ejemplo local preparado."))
