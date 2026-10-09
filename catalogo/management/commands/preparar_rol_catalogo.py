from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prepara el rol local de catálogo sin administrar usuarios ni borrar productos."

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name="Responsable de catálogo")
        group.permissions.set(Permission.objects.filter(content_type__app_label="catalogo", content_type__model__in=["producto", "productoimagen", "galeriaimagen"], codename__in=["view_producto", "add_producto", "change_producto", "view_productoimagen", "add_productoimagen", "change_productoimagen", "view_galeriaimagen", "add_galeriaimagen", "change_galeriaimagen"]))
        self.stdout.write(self.style.SUCCESS("Rol preparado. Asignar a un usuario staff desde el administrador."))
