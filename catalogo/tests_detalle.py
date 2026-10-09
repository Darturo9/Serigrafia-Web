from importlib import import_module
from tempfile import TemporaryDirectory
from unittest.mock import patch, PropertyMock
from types import SimpleNamespace
from urllib.parse import unquote_plus
from django.apps import apps
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.db import connection, transaction
from django.forms.models import inlineformset_factory
from django.test import TestCase, Client, override_settings
from .models import Producto, ProductoImagen
from .forms import ProductoImagenAdminForm, ProductoImagenFormSet
from .tests import foto
from config.storage.supabase import PhotoStorageError


class DetalleTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(nombre="Fixture ñ", descripcion="<b>Descripción</b>", publicado=True, tallas=["M"])

    def test_publicacion_y_ejemplos_en_ruta_y_post(self):
        oculto = Producto.objects.create(nombre="Oculto", descripcion="x")
        ejemplo = Producto.objects.create(nombre="Ejemplo", descripcion="x", publicado=True, es_ejemplo=True)
        for obj in (oculto, ejemplo):
            for metodo in (self.client.get, self.client.post):
                self.assertEqual(metodo(f"/productos/{obj.pk}/").status_code, 404)
        with override_settings(JYZ_SHOW_REVIEW_EXAMPLES=True):
            respuesta = self.client.post(f"/productos/{ejemplo.pk}/", {"cantidad": 1})
            self.assertContains(respuesta, "no disponible para venta")
            self.assertNotContains(respuesta, "Quiero este producto")
            self.assertNotContains(respuesta, "Revisa tu mensaje")
        self.assertEqual(self.client.get('/productos/999999/').status_code, 404)

    def test_cotizacion_usa_producto_de_ruta_y_no_guarda_pedido(self):
        self.assertEqual(Client(enforce_csrf_checks=True).post(f"/productos/{self.producto.pk}/", {"cantidad": 1}).status_code, 403)
        otro = Producto.objects.create(nombre="Otro", descripcion="x", publicado=True)
        respuesta = self.client.post(f"/productos/{self.producto.pk}/", {"producto": otro.pk, "cantidad": 2, "talla_0": 2})
        self.assertContains(respuesta, "Revisa tu mensaje")
        self.assertContains(respuesta, "&lt;b&gt;Descripción&lt;/b&gt;")
        self.assertIn("Producto: Fixture ñ", unquote_plus(respuesta.context['enlace_mensaje']))
        self.assertNotIn("Producto: Otro", unquote_plus(respuesta.context['enlace_mensaje']))
        self.assertEqual(Producto.objects.count(), 2)
        self.assertContains(self.client.post(f"/productos/{self.producto.pk}/", {"cantidad": 2, "talla_0": 1}), "La suma de las cantidades")

    def test_cero_una_seis_fotos_portada_orden_y_desactivadas(self):
        ruta = f"/productos/{self.producto.pk}/"
        self.assertContains(self.client.get(ruta), "Fotografía pendiente")
        primera = ProductoImagen.objects.create(producto=self.producto, foto="uno.webp", descripcion="Primera", orden=9)
        self.assertNotContains(self.client.get(ruta), 'class="miniaturas"')
        imagenes = [primera]
        for n in range(5):
            imagenes.append(ProductoImagen.objects.create(producto=self.producto, foto=f"{n}.webp", descripcion=f"Vista {n}", orden=n))
        ProductoImagen.objects.create(producto=self.producto, foto="secreta.webp", activo=False)
        self.producto.portada = imagenes[3]
        self.producto.save()
        respuesta = self.client.get(ruta)
        self.assertEqual(len(respuesta.context['fotos']), 6)
        self.assertEqual(respuesta.context['fotos'][0]['descripcion'], 'Vista 2')
        self.assertNotContains(respuesta, 'secreta.webp')
        self.assertContains(respuesta, 'class="miniatura-producto"', count=6)
        with patch('django.db.models.fields.files.FieldFile.url', new_callable=PropertyMock, side_effect=PhotoStorageError('fallo')):
            self.assertContains(self.client.get(ruta), 'Fotografía pendiente')

    def test_portada_de_otro_producto_o_inactiva_rechazada(self):
        otro = Producto.objects.create(nombre="Otro", descripcion="x")
        imagen = ProductoImagen.objects.create(producto=otro, foto='otra.webp')
        self.producto.portada = imagen
        with self.assertRaises(ValidationError):
            self.producto.full_clean()
        imagen.producto = self.producto
        imagen.activo = False
        imagen.save()
        with self.assertRaises(ValidationError):
            self.producto.full_clean()

    def test_migracion_registra_referencia_sin_modificar_original(self):
        with TemporaryDirectory() as media, override_settings(MEDIA_ROOT=media):
            self.producto.foto = foto()
            self.producto.save()
            nombre, ruta = self.producto.foto.name, self.producto.foto.path
            from pathlib import Path
            contenido = Path(ruta).read_bytes()
            migracion = import_module('catalogo.migrations.0003_registrar_fotos_actuales')
            migracion.registrar(apps, SimpleNamespace(connection=connection))
            self.producto.refresh_from_db()
            self.assertEqual(self.producto.foto.name, nombre)
            self.assertEqual(self.producto.portada.foto.name, nombre)
            self.assertEqual(Path(ruta).read_bytes(), contenido)

    def test_limite_inline_y_portada_desactivada(self):
        factory = inlineformset_factory(Producto, ProductoImagen, fk_name='producto', form=ProductoImagenAdminForm, formset=ProductoImagenFormSet, extra=0, can_delete=False)
        imagenes = [ProductoImagen.objects.create(producto=self.producto, foto=f'{n}.webp') for n in range(7)]
        datos = {'imagenes-TOTAL_FORMS': '7', 'imagenes-INITIAL_FORMS': '7'}
        for n, imagen in enumerate(imagenes):
            datos.update({f'imagenes-{n}-id': imagen.pk, f'imagenes-{n}-producto': self.producto.pk, f'imagenes-{n}-orden': n, f'imagenes-{n}-activo': 'on'})
        with transaction.atomic():
            formset = factory(datos, instance=self.producto, prefix='imagenes')
            self.assertFalse(formset.is_valid())
            self.assertIn('hasta seis', str(formset.non_form_errors()))
        datos.pop('imagenes-6-activo')
        with transaction.atomic():
            self.assertTrue(factory(datos, instance=self.producto, prefix='imagenes').is_valid())
        self.producto.portada = imagenes[6]
        with transaction.atomic():
            formset = factory(datos, instance=self.producto, prefix='imagenes')
            self.assertFalse(formset.is_valid())
            self.assertIn('portada', str(formset.non_form_errors()))

    def test_admin_permisos_inline_y_fallo_conserva_referencias(self):
        call_command('preparar_rol_catalogo', verbosity=0)
        usuario = User.objects.create_user('editor', password='prueba', is_staff=True)
        usuario.groups.add(Group.objects.get(name='Responsable de catálogo'))
        self.assertTrue(usuario.has_perm('catalogo.add_productoimagen'))
        self.assertFalse(usuario.has_perm('catalogo.delete_productoimagen'))
        self.assertFalse(usuario.has_perm('auth.change_user'))
        self.client.force_login(usuario)
        ruta = f'/admin/catalogo/producto/{self.producto.pk}/change/'
        respuesta = self.client.get(ruta)
        self.assertContains(respuesta, 'imagenes-TOTAL_FORMS')
        self.assertNotContains(respuesta, 'name="imagenes-0-DELETE"')
        datos = {'nombre': self.producto.nombre, 'descripcion': 'Cambió', 'tallas': '["M"]', 'orden': 0, 'publicado': 'on', 'imagenes-TOTAL_FORMS': 1, 'imagenes-INITIAL_FORMS': 0, 'imagenes-0-orden': 0, 'imagenes-0-activo': 'on', 'imagenes-0-foto': foto()}
        with patch.object(ProductoImagen._meta.get_field('foto').storage, 'save', side_effect=PhotoStorageError('fallo')):
            self.assertEqual(self.client.post(ruta, datos).status_code, 302)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.descripcion, '<b>Descripción</b>')
        self.assertFalse(self.producto.imagenes.exists())

    def test_carga_multiple_parcial_revierte_y_registra_archivo_sin_referencia(self):
        call_command('preparar_rol_catalogo', verbosity=0)
        usuario = User.objects.create_user('editor-multiple', is_staff=True)
        usuario.groups.add(Group.objects.get(name='Responsable de catálogo'))
        self.client.force_login(usuario)
        anterior = ProductoImagen.objects.create(producto=self.producto, foto='anterior.webp')
        datos = {'nombre': self.producto.nombre, 'descripcion': 'Cambió', 'tallas': '["M"]', 'orden': 0, 'publicado': 'on', 'imagenes-TOTAL_FORMS': 3, 'imagenes-INITIAL_FORMS': 1, 'imagenes-0-id': anterior.pk, 'imagenes-0-producto': self.producto.pk, 'imagenes-0-orden': 0, 'imagenes-0-activo': 'on'}
        for n in (1, 2):
            datos.update({f'imagenes-{n}-orden': n, f'imagenes-{n}-activo': 'on', f'imagenes-{n}-foto': foto(f'{n}.png')})
        storage = ProductoImagen._meta.get_field('foto').storage
        with patch.object(storage, 'save', side_effect=['productos/subida-sin-referencia.webp', PhotoStorageError('fallo')]):
            with self.assertLogs('catalogo.admin', level='WARNING') as logs:
                respuesta = self.client.post(f'/admin/catalogo/producto/{self.producto.pk}/change/', datos)
        self.assertEqual(respuesta.status_code, 302)
        self.assertIn('subida-sin-referencia.webp', str(logs.output))
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.descripcion, '<b>Descripción</b>')
        self.assertEqual(list(self.producto.imagenes.values_list('foto', flat=True)), ['anterior.webp'])
