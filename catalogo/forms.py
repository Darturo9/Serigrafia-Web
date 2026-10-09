from django import forms
from django.core.exceptions import ValidationError
from .models import Producto, ProductoImagen, GaleriaImagen
from django.forms.models import BaseInlineFormSet
from config.storage.supabase import PhotoStorageError


class PhotoDisplay:
    def __init__(self, name, url):
        self.name, self.url = name, url

    def __str__(self):
        return self.name


class PhotoWidget(forms.ClearableFileInput):
    def is_initial(self, value):
        return bool(value and getattr(value, "name", None))

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if context["widget"]["is_initial"]:
            try:
                context["widget"]["value"] = PhotoDisplay(value.name, value.url)
            except PhotoStorageError:
                context["widget"]["is_initial"] = False
                context["widget"]["value"] = None
        return context


class ProductoAdminForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {"foto": PhotoWidget}
        help_texts = {"foto": "JPEG, PNG o WebP estático, hasta 5 MB y 16 megapíxeles. En el alojamiento Supabase se optimiza automáticamente a WebP de hasta 1600 px y 500 KB."}

    def clean_foto(self):
        foto = self.cleaned_data.get("foto")
        if not foto or not hasattr(foto, "image"):
            return foto
        if foto.size > 5 * 1024 * 1024:
            raise ValidationError("La foto debe pesar como máximo 5 MB.")
        if foto.image.format not in {"JPEG", "PNG", "WEBP"}:
            raise ValidationError("Usa una imagen JPEG, PNG o WebP.")
        if foto.image.width * foto.image.height > 16_000_000:
            raise ValidationError("La foto no puede superar 16 megapíxeles.")
        return foto


class ProductoImagenAdminForm(ProductoAdminForm):
    class Meta(ProductoAdminForm.Meta):
        model = ProductoImagen


class GaleriaImagenAdminForm(ProductoAdminForm):
    class Meta(ProductoAdminForm.Meta):
        model = GaleriaImagen


class ProductoImagenFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return
        # El Admin ya abre una transacción; serializar ediciones del mismo producto.
        if self.instance.pk:
            Producto.objects.select_for_update().get(pk=self.instance.pk)
        activas = [f for f in self.forms if f.cleaned_data and not f.cleaned_data.get("DELETE") and f.cleaned_data.get("activo") and f.cleaned_data.get("foto")]
        representadas = [f.instance.pk for f in self.forms if f.instance.pk]
        adicionales = self.instance.imagenes.filter(activo=True).exclude(pk__in=representadas).count() if self.instance.pk else 0
        if len(activas) + adicionales > 6:
            raise ValidationError("Un producto admite hasta seis fotos visibles. Desactive otra antes de agregar esta.")
        if self.instance.portada_id and not any(f.instance.pk == self.instance.portada_id for f in activas):
            raise ValidationError("La portada debe permanecer visible. Elija otra portada o deje la selección vacía.")
