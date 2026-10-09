from pathlib import Path
from io import BytesIO
from tempfile import TemporaryDirectory
from unittest.mock import patch, PropertyMock
from PIL import Image
from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase, override_settings
from .models import GaleriaImagen
from .tests import foto
from config.storage.supabase import PhotoStorageError, SupabasePrivateStorage
from config.runtime_settings import PROJECT_URL


class GaleriaTests(TestCase):
    def setUp(self):
        self.media = TemporaryDirectory()
        self.addCleanup(self.media.cleanup)
        override = override_settings(MEDIA_ROOT=self.media.name)
        override.enable()
        self.addCleanup(override.disable)
        call_command("preparar_rol_catalogo", verbosity=0)
        self.editor = User.objects.create_user("editor-galeria", is_staff=True)
        self.editor.groups.add(Group.objects.get(name="Responsable de catálogo"))
        self.client.force_login(self.editor)
        self.data = {"titulo": "Trabajo propio", "descripcion": "Playera blanca estampada", "orden": 0, "activo": "on"}

    def test_admin_edita_ordena_y_oculta_con_seccion_publica_suspendida(self):
        self.assertEqual(self.client.post('/admin/catalogo/galeriaimagen/add/', {**self.data, "foto": foto()}).status_code, 302)
        primera = GaleriaImagen.objects.get()
        GaleriaImagen.objects.create(titulo="Primero", descripcion="Otra prenda", foto=foto(), orden=0)
        self.assertEqual(self.client.post(f'/admin/catalogo/galeriaimagen/{primera.pk}/change/', {**self.data, "titulo": "Editado", "orden": 5}).status_code, 302)
        self.assertEqual(list(GaleriaImagen.objects.values_list('titulo', flat=True)), ['Primero', 'Editado'])
        response = self.client.get('/')
        self.assertNotContains(response, 'id="trabajos"')
        self.assertNotContains(response, 'href="#trabajos"')
        self.assertNotContains(response, '>Primero</h3>')
        self.assertNotContains(response, '>Editado</h3>')
        hidden = {**self.data, "titulo": "Editado", "orden": 5}
        hidden.pop("activo")
        self.assertEqual(self.client.post(f'/admin/catalogo/galeriaimagen/{primera.pk}/change/', hidden).status_code, 302)
        self.assertNotContains(self.client.get('/'), '>Editado</h3>')
        primera.refresh_from_db()
        self.assertFalse(primera.activo)
        self.assertTrue(Path(primera.foto.path).exists())

    def test_vacia_sin_enlace_y_no_reaparecen_referencias(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'id="trabajos"')
        self.assertNotContains(response, 'href="#trabajos"')
        self.assertNotContains(response, 'galeria-jyz/')

    def test_permisos_sin_borrado_ni_usuarios(self):
        self.assertContains(self.client.get('/admin/'), 'Galería')
        self.assertTrue(self.editor.has_perm('catalogo.add_galeriaimagen'))
        self.assertTrue(self.editor.has_perm('catalogo.change_galeriaimagen'))
        self.assertFalse(self.editor.has_perm('catalogo.delete_galeriaimagen'))
        imagen = GaleriaImagen.objects.create(**{k:v for k,v in self.data.items() if k != 'activo'}, foto=foto())
        self.assertEqual(self.client.get(f'/admin/catalogo/galeriaimagen/{imagen.pk}/delete/').status_code, 403)
        self.assertEqual(self.client.get('/admin/auth/user/').status_code, 403)
        otro = User.objects.create_user('staff-sin-galeria', is_staff=True)
        self.client.force_login(otro)
        self.assertEqual(self.client.get('/admin/catalogo/galeriaimagen/add/').status_code, 403)

    def test_imagen_invalida_y_fallo_storage_conservan_edicion_y_foto(self):
        imagen = GaleriaImagen.objects.create(titulo='Anterior', descripcion='Antes', foto=foto())
        before = imagen.foto.name
        path = f'/admin/catalogo/galeriaimagen/{imagen.pk}/change/'
        invalid = SimpleUploadedFile('rota.png', b'invalid')
        self.assertEqual(self.client.post(path, {**self.data, 'foto':invalid}).status_code, 200)
        with patch.object(GaleriaImagen._meta.get_field('foto').storage, 'save', side_effect=PhotoStorageError('fallo')):
            response = self.client.post(path, {**self.data, 'foto':foto()}, follow=True)
        self.assertContains(response, 'No se guardaron los cambios')
        imagen.refresh_from_db()
        self.assertEqual(imagen.titulo, 'Anterior')
        self.assertEqual(imagen.foto.name, before)
        self.assertTrue(Path(imagen.foto.path).exists())

    def test_galeria_suspendida_no_emite_contenido_y_fallo_foto_no_rompe_inicio(self):
        imagen = GaleriaImagen.objects.create(titulo='<script>uno</script>', descripcion='Foto', foto=foto())
        response = self.client.get('/')
        self.assertNotContains(response, '&lt;script&gt;uno&lt;/script&gt;')
        self.assertNotContains(response, '<script>uno</script>')
        with patch.object(type(imagen.foto), 'url', new_callable=PropertyMock, side_effect=PhotoStorageError('fallo')):
            response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'id="trabajos"')

    def test_carga_inicial_no_modifica_galeria_existente(self):
        call_command('cargar_galeria_inicial', aplicar=True, verbosity=0)
        fotos = list(GaleriaImagen.objects.values_list('pk','foto'))
        primera = GaleriaImagen.objects.first()
        primera.titulo='Edición del dueño';primera.save()
        call_command('cargar_galeria_inicial', aplicar=True, verbosity=0)
        self.assertEqual(list(GaleriaImagen.objects.values_list('pk','foto')), fotos)
        self.assertEqual(GaleriaImagen.objects.first().titulo,'Edición del dueño')

    def test_carga_de_galeria_usa_webp_del_backend_sin_red(self):
        stream = BytesIO()
        Image.new('RGB', (2000,1000), '#f5f5f5').save(stream, 'JPEG')
        upload = SimpleUploadedFile('foto.jpeg',stream.getvalue(),content_type='image/jpeg')
        storage = SupabasePrivateStorage(PROJECT_URL,'jyz-prueba-fotos','solo-test')
        with patch.object(GaleriaImagen._meta.get_field('foto'),'storage',storage), patch.object(storage,'_request') as request:
            imagen = GaleriaImagen.objects.create(titulo='Carga',descripcion='Prenda',foto=upload)
        self.assertTrue(imagen.foto.name.endswith('.webp'))
        data=request.call_args.kwargs['data']
        self.assertEqual(request.call_args.kwargs['content_type'],'image/webp')
        with Image.open(BytesIO(data)) as converted:
            self.assertEqual(converted.format,'WEBP')
            self.assertEqual(converted.size,(1600,800))
        self.assertLessEqual(len(data),500*1024)
