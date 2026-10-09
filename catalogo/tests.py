from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from PIL import Image
from django.contrib.auth.models import Group, Permission, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from .forms import ProductoAdminForm
from .models import Producto


def foto(nombre="prueba.png", formato="PNG"):
    stream = BytesIO()
    Image.new("RGB", (32, 32), "#777777").save(stream, format=formato)
    return SimpleUploadedFile(nombre, stream.getvalue(), content_type="image/png")


class CatalogoTests(TestCase):
    def setUp(self):
        self.media = TemporaryDirectory()
        self.addCleanup(self.media.cleanup)
        self.override = override_settings(MEDIA_ROOT=self.media.name)
        self.override.enable()
        self.addCleanup(self.override.disable)
        call_command("preparar_rol_catalogo", verbosity=0)
        self.editor = User.objects.create_user("editor", password="clave-solo-test-27!", is_staff=True)
        self.editor.groups.add(Group.objects.get(name="Responsable de catálogo"))
        self.base = {"nombre": "Prenda de prueba", "descripcion": "Solo prueba", "categoria": "", "tallas": '["S", "M"]', "orden": "0", "publicado": "on", "es_ejemplo": "on", "texto_foto": "Imagen de prueba", "imagenes-TOTAL_FORMS": "0", "imagenes-INITIAL_FORMS": "0", "imagenes-MIN_NUM_FORMS": "0", "imagenes-MAX_NUM_FORMS": "1000"}

    def test_anonimo_no_puede_entrar_al_panel(self):
        response = self.client.get(reverse("admin:catalogo_producto_add"))
        self.assertRedirects(response, reverse("admin:login") + "?next=" + reverse("admin:catalogo_producto_add"))

    def test_rol_puede_editar_catalogo_sin_borrar_ni_administrar_usuarios(self):
        self.client.force_login(self.editor)
        self.assertEqual(self.client.get(reverse("admin:catalogo_producto_add")).status_code, 200)
        self.assertEqual(self.client.get(reverse("admin:auth_user_changelist")).status_code, 403)
        product = Producto.objects.create(nombre="Prueba", descripcion="Prueba")
        self.assertEqual(self.client.get(reverse("admin:catalogo_producto_delete", args=[product.pk])).status_code, 403)
        self.assertFalse(self.editor.has_perm("catalogo.delete_producto"))

    def test_staff_sin_permisos_no_puede_crear(self):
        user = User.objects.create_user("sinpermiso", is_staff=True)
        self.client.force_login(user)
        self.assertEqual(self.client.get(reverse("admin:catalogo_producto_add")).status_code, 403)

    def test_panel_crea_edita_foto_y_oculta_producto(self):
        self.client.force_login(self.editor)
        response = self.client.post(reverse("admin:catalogo_producto_add"), {**self.base, "foto": foto()})
        self.assertEqual(response.status_code, 302)
        product = Producto.objects.get()
        self.assertTrue(Path(product.foto.path).is_file())
        self.assertContains(self.client.get(reverse("catalogo")), product.nombre)
        self.assertContains(self.client.get(reverse("catalogo")), "Dato de ejemplo para pruebas")
        old_path = product.foto.name
        response = self.client.post(reverse("admin:catalogo_producto_change", args=[product.pk]), {**self.base, "nombre": "Producto editado", "foto": foto("segunda.png")})
        self.assertEqual(response.status_code, 302)
        product.refresh_from_db()
        self.assertEqual(product.nombre, "Producto editado")
        self.assertNotEqual(product.foto.name, old_path)
        hidden = dict(self.base)
        hidden.pop("publicado")
        response = self.client.post(reverse("admin:catalogo_producto_change", args=[product.pk]), hidden)
        self.assertEqual(response.status_code, 302)
        self.assertNotContains(self.client.get(reverse("catalogo")), "Prenda de prueba")
        product.refresh_from_db()
        self.assertFalse(product.publicado)

    def test_foto_corrupta_no_reemplaza_existente(self):
        product = Producto.objects.create(nombre="Prueba", descripcion="Prueba", foto=foto(), tallas=["S"], publicado=True)
        old_path = product.foto.name
        old_bytes = Path(product.foto.path).read_bytes()
        self.client.force_login(self.editor)
        response = self.client.post(reverse("admin:catalogo_producto_change", args=[product.pk]), {**self.base, "foto": SimpleUploadedFile("rota.png", b"no-es-imagen")})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["adminform"].form.errors.get("foto"))
        product.refresh_from_db()
        self.assertEqual(product.foto.name, old_path)
        self.assertEqual(Path(product.foto.path).read_bytes(), old_bytes)

    def test_formato_no_permitido(self):
        form = ProductoAdminForm(data=self.base, files={"foto": foto("imagen.gif", "GIF")})
        self.assertFalse(form.is_valid())
        self.assertIn("foto", form.errors)

    def test_foto_superior_a_limite(self):
        upload = foto()
        upload.size = 5 * 1024 * 1024 + 1
        form = ProductoAdminForm(data=self.base, files={"foto": upload})
        self.assertFalse(form.is_valid())
        self.assertIn("5 MB", str(form.errors))

    def test_tallas_invalidas(self):
        for tallas in ['"M"', '["S", "s"]', '["S", 2]', '[""]']:
            with self.subTest(tallas=tallas):
                form = ProductoAdminForm(data={**self.base, "tallas": tallas})
                self.assertFalse(form.is_valid())
                self.assertIn("tallas", form.errors)

    def test_catalogo_vacio_y_solo_publicados(self):
        self.assertContains(self.client.get(reverse("catalogo")), "no tiene productos publicados")
        Producto.objects.create(nombre="Oculto", descripcion="Oculto")
        product = Producto.objects.create(nombre="Visible", descripcion="<script>alert(1)</script>", publicado=True)
        response = self.client.get(reverse("catalogo"))
        self.assertContains(response, product.nombre)
        self.assertNotContains(response, "Oculto")
        self.assertNotContains(response, "<script>alert(1)</script>")
        self.assertContains(response, "&lt;script&gt;")
        self.assertEqual(response["X-Robots-Tag"], "noindex, nofollow")

    def test_admin_rechaza_post_sin_csrf(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.editor)
        response = client.post(reverse("admin:catalogo_producto_add"), self.base)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Producto.objects.count(), 0)
