import logging
from django.contrib import admin, messages

logger = logging.getLogger(__name__)
from django.shortcuts import redirect
from django.utils.html import format_html
from config.storage.supabase import PhotoStorageError
from .forms import ProductoAdminForm, ProductoImagenAdminForm, ProductoImagenFormSet, GaleriaImagenAdminForm
from .models import Producto, ProductoImagen, GaleriaImagen

class PhotoStorageAdminMixin:
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        request._jyz_uploaded_photos = []
        try:
            return super().changeform_view(request, object_id, form_url, extra_context)
        except PhotoStorageError:
            if request.method != "POST":
                raise
            if request._jyz_uploaded_photos:
                logger.warning("Fotos subidas antes de rollback; revisar referencias antes de cualquier limpieza: %s", request._jyz_uploaded_photos)
            # El Admin revierte su transacción antes de llegar aquí; la foto anterior permanece.
            self.message_user(request, "No se guardaron los cambios porque la foto no pudo almacenarse. "
                              "La imagen anterior se conserva. Vuelva a seleccionar la foto e intente de nuevo.",
                              level=messages.ERROR)
            return redirect(request.path)


class ProductoImagenInline(admin.StackedInline):
    model = ProductoImagen
    fk_name = "producto"
    form = ProductoImagenAdminForm
    formset = ProductoImagenFormSet
    extra = 1
    can_delete = False
    fields = ("foto", "descripcion", "orden", "activo")
    verbose_name_plural = "Fotos: hasta seis visibles; desactive para retirar"


@admin.register(Producto)
class ProductoAdmin(PhotoStorageAdminMixin, admin.ModelAdmin):
    form = ProductoAdminForm
    inlines = (ProductoImagenInline,)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if "portada" in form.base_fields:
            form.base_fields["portada"].queryset = ProductoImagen.objects.filter(producto=obj, activo=True) if obj else ProductoImagen.objects.none()
        return form

    def save_model(self, request, obj, form, change):
        anterior = Producto.objects.get(pk=obj.pk).foto.name if change else ""
        super().save_model(request, obj, form, change)
        if "foto" in form.changed_data and obj.foto:
            request._jyz_uploaded_photos.append(obj.foto.name)
        if change and anterior and "foto" in form.changed_data:
            # Compatibilidad: reemplazos de la foto antigua actualizan su referencia registrada.
            fotos = obj.imagenes.filter(foto=anterior)
            if obj.foto:
                fotos.update(foto=obj.foto.name, descripcion=obj.texto_foto)
            else:
                if fotos.filter(pk=obj.portada_id).exists():
                    obj.portada = None
                    obj.save(update_fields=["portada"])
                fotos.update(activo=False)

    def save_formset(self, request, form, formset, change):
        if "foto" in form.changed_data and change:
            for image_form in formset.forms:
                if image_form.instance.pk and "foto" not in image_form.changed_data:
                    image_form.instance.foto = ProductoImagen.objects.get(pk=image_form.instance.pk).foto
        for instancia in formset.save(commit=False):
            carga = bool(instancia.foto and not instancia.foto._committed)
            instancia.save()
            if carga:
                request._jyz_uploaded_photos.append(instancia.foto.name)
        formset.save_m2m()

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("imagenes")

    def foto_portada(self, obj):
        if not obj:
            return None
        imagenes = [i for i in obj.imagenes.all() if i.activo]
        imagenes.sort(key=lambda i: (i.pk != obj.portada_id, i.orden, i.pk))
        if imagenes:
            return imagenes[0].foto
        return obj.foto if not obj.imagenes.exists() else None

    @admin.display(description="Foto")
    def miniatura(self, obj):
        archivo = self.foto_portada(obj)
        if not archivo:
            return "Sin foto"
        try:
            return format_html('<img class="jyz-thumbnail" src="{}" alt="{}" width="64" height="64" loading="lazy">',
                               archivo.url, obj.texto_foto or obj.nombre)
        except PhotoStorageError:
            return "Foto no disponible"

    @admin.display(description="Visibilidad", ordering="publicado")
    def visibilidad(self, obj):
        state = "visible" if obj.publicado else "hidden"
        label = "Publicado" if obj.publicado else "Oculto"
        return format_html('<span class="jyz-status jyz-status-{}">{}</span>', state, label)

    @admin.display(description="Contenido", ordering="es_ejemplo")
    def tipo_contenido(self, obj):
        return format_html('<span class="jyz-kind">{}</span>', "Ejemplo" if obj.es_ejemplo else "Catálogo")

    @admin.display(description="Foto actual")
    def vista_foto(self, obj):
        archivo = self.foto_portada(obj)
        if not archivo:
            return "Todavía no hay una foto. Puede agregarla en el campo de abajo."
        try:
            return format_html('<img class="jyz-photo-preview" src="{}" alt="{}" width="320" height="320">',
                               archivo.url, obj.texto_foto or obj.nombre)
        except PhotoStorageError:
            return "No se pudo mostrar la foto. El archivo anterior se conserva."

    list_display = ("miniatura", "nombre", "categoria", "visibilidad", "tipo_contenido", "actualizado")
    list_display_links = ("nombre",)
    list_per_page = 20
    list_filter = ("publicado", "es_ejemplo", "categoria")
    search_fields = ("nombre", "descripcion")
    readonly_fields = ("vista_foto",)
    fieldsets = (
        ("Información del producto", {"fields": ("nombre", "descripcion", "categoria")}),
        ("Tallas y opciones", {"fields": ("tallas",)}),
        ("Fotografía", {"fields": ("vista_foto", "foto", "texto_foto", "portada"),
                         "description": "La foto anterior se conserva. Agregue fotos debajo; después de guardar puede elegir una portada. Cada carga se optimiza para la web."}),
        ("Publicación", {"fields": ("publicado", "orden", "es_ejemplo"),
                           "description": "Oculte un producto cuando no deba aparecer. Los ejemplos deben seguir identificados."}),
    )

admin.site.site_header = "JYZ · Administración"
admin.site.site_title = "Panel JYZ"
admin.site.index_title = "Tu catálogo y galería"
admin.site.site_url = "/"


@admin.register(GaleriaImagen)
class GaleriaImagenAdmin(PhotoStorageAdminMixin, admin.ModelAdmin):
    form = GaleriaImagenAdminForm
    list_display = ("miniatura", "titulo", "orden", "activo", "actualizado")
    list_display_links = ("titulo",)
    list_editable = ("orden", "activo")
    list_filter = ("activo",)
    search_fields = ("titulo", "descripcion")
    readonly_fields = ("vista_foto",)
    list_per_page = 20
    fieldsets = (
        ("Contenido de la galería", {"fields": ("titulo", "descripcion")}),
        ("Fotografía", {"fields": ("vista_foto", "foto"),
                         "description": "Cada carga se optimiza a WebP. Al reemplazar se conserva el archivo anterior."}),
        ("Publicación", {"fields": ("orden", "activo"),
                           "description": "Se muestra en Ideas que toman forma. Desactive visible para ocultar sin borrar."}),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        carga = bool(obj.foto and not obj.foto._committed)
        super().save_model(request, obj, form, change)
        if carga:
            request._jyz_uploaded_photos.append(obj.foto.name)

    @admin.display(description="Foto")
    def miniatura(self, obj):
        try:
            return format_html('<img class="jyz-thumbnail" src="{}" alt="{}" width="64" height="64" loading="lazy">',
                               obj.foto.url, obj.descripcion)
        except (PhotoStorageError, ValueError):
            return "Foto no disponible"

    @admin.display(description="Foto actual")
    def vista_foto(self, obj):
        if not obj or not obj.foto:
            return "Seleccione una foto para la galería."
        try:
            return format_html('<img class="jyz-photo-preview" src="{}" alt="{}" width="320" height="320">',
                               obj.foto.url, obj.descripcion)
        except (PhotoStorageError, ValueError):
            return "No se pudo mostrar la foto. El archivo anterior se conserva."
