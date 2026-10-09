from django.db import migrations


def registrar(apps, schema_editor):
    Producto = apps.get_model("catalogo", "Producto")
    Imagen = apps.get_model("catalogo", "ProductoImagen")
    alias = schema_editor.connection.alias
    for producto in Producto.objects.using(alias).exclude(foto="").iterator():
        imagen = Imagen.objects.using(alias).create(producto_id=producto.pk, foto=producto.foto.name, descripcion=producto.texto_foto, orden=0, activo=True)
        Producto.objects.using(alias).filter(pk=producto.pk).update(portada_id=imagen.pk)


class Migration(migrations.Migration):
    dependencies = [("catalogo", "0002_productoimagen_producto_portada")]
    operations = [migrations.RunPython(registrar, migrations.RunPython.noop)]
