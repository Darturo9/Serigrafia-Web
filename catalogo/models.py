from pathlib import Path
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.db import models


def validar_tallas(value):
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() or len(item) > 20 for item in value):
        raise ValidationError('Ingresa una lista de tallas, por ejemplo ["S", "M", "L"].')
    if len(value) > 30 or len({item.strip().casefold() for item in value}) != len(value):
        raise ValidationError("Las tallas deben ser únicas y no superar 30 opciones.")


def ruta_foto(instance, filename):
    return f"productos/{uuid4().hex}{Path(filename).suffix.lower()}"


class Producto(models.Model):
    nombre = models.CharField("nombre", max_length=160)
    descripcion = models.TextField("descripción", max_length=2000)
    categoria = models.CharField("categoría", max_length=100, blank=True)
    tallas = models.JSONField("tallas", default=list, blank=True, validators=[validar_tallas], help_text='Ejemplo: ["S", "M", "L"]. Sin tallas: [].')
    foto = models.ImageField("foto", upload_to=ruta_foto, blank=True)
    texto_foto = models.CharField("descripción de la foto", max_length=200, blank=True)
    publicado = models.BooleanField("publicado", default=False)
    orden = models.PositiveIntegerField("orden", default=0)
    es_ejemplo = models.BooleanField("dato de ejemplo", default=False, help_text="Usar únicamente para pruebas, nunca como producto real.")
    portada = models.ForeignKey("ProductoImagen", verbose_name="portada", null=True, blank=True, on_delete=models.SET_NULL, related_name="+", help_text="Guarde primero las fotos y luego elija una portada. Sin selección se usa la primera foto activa.")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["orden", "nombre", "pk"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def clean(self):
        super().clean()
        if self.portada_id and (self.portada.producto_id != self.pk or not self.portada.activo):
            raise ValidationError({"portada": "Elija una foto activa de este producto."})

    def __str__(self):
        return self.nombre


class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="imagenes")
    foto = models.ImageField("foto", upload_to=ruta_foto)
    descripcion = models.CharField("descripción de la foto", max_length=200, blank=True)
    orden = models.PositiveIntegerField("orden", default=0)
    activo = models.BooleanField("visible", default=True, help_text="Desactive para retirar la foto sin borrar el archivo.")

    class Meta:
        ordering = ["orden", "pk"]
        verbose_name = "foto de producto"
        verbose_name_plural = "fotos del producto"

    def __str__(self):
        return self.descripcion or f"Foto {self.pk or 'nueva'}"


class GaleriaImagen(models.Model):
    titulo = models.CharField("título", max_length=160)
    descripcion = models.CharField("descripción de la foto", max_length=300,
                                   help_text="Describe lo que se ve; también se usa como texto accesible.")
    foto = models.ImageField("foto", upload_to=ruta_foto)
    orden = models.PositiveIntegerField("orden", default=0, help_text="Los números menores aparecen primero.")
    activo = models.BooleanField("visible", default=True, help_text="Desactive para ocultar sin borrar la foto.")
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["orden", "pk"]
        verbose_name = "foto de galería"
        verbose_name_plural = "Galería"

    def __str__(self):
        return self.titulo
