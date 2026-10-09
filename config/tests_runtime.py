"""Pruebas locales: bindings simulados y HTTP simulado; no acceden a Supabase."""
from io import BytesIO
from types import SimpleNamespace
from unittest.mock import patch

import httpx
from PIL import Image
from django.contrib.auth.models import User, Group
from django.core.exceptions import ImproperlyConfigured, SuspiciousFileOperation
from django.core.files.base import ContentFile
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .runtime_settings import PROJECT_URL, build_worker_settings
from .storage.supabase import MAX_BYTES, PhotoStorageError, SupabasePrivateStorage
from catalogo.models import Producto
from catalogo.tests import foto


def environment(local=False):
    return SimpleNamespace(
        JYZ_WORKER_LOCAL="true" if local else "false",
        DJANGO_SECRET_KEY="x" * 64,
        JYZ_REVIEW_ORIGIN="http://127.0.0.1:8787" if local else "https://revision.example.test",
        JYZ_REVIEW_USER="review-test", JYZ_REVIEW_PASSWORD="y" * 32,
        SUPABASE_URL=PROJECT_URL, SUPABASE_STORAGE_KEY="secret-only-for-test",
        HYPERDRIVE=SimpleNamespace(host="binding.test", port=5432, user="test", password="test", database="test"),
    )


class RuntimeSettingsTests(SimpleTestCase):
    def test_remote_is_private_and_has_no_filesystem_backend(self):
        result = build_worker_settings(environment())
        self.assertFalse(result["DEBUG"])
        self.assertTrue(result["SESSION_COOKIE_SECURE"])
        self.assertTrue(result["CSRF_COOKIE_SECURE"])
        self.assertEqual(result["DATABASES"]["default"]["OPTIONS"]["options"], "-c search_path=jyz_prueba")
        self.assertEqual(result["DATABASES"]["default"]["CONN_MAX_AGE"], 0)
        self.assertIn("SupabasePrivateStorage", result["STORAGES"]["default"]["BACKEND"])

    def test_remote_fails_closed_for_missing_secrets_and_wrong_project(self):
        for key, value in [("DJANGO_SECRET_KEY", "short"), ("SUPABASE_STORAGE_KEY", ""),
                           ("SUPABASE_URL", "https://other.supabase.co"),
                           ("JYZ_REVIEW_ORIGIN", "http://revision.example.test"),
                           ("JYZ_REVIEW_PASSWORD", "short"), ("JYZ_DB_SCHEMA", "public")]:
            with self.subTest(key=key):
                env = environment()
                setattr(env, key, value)
                with self.assertRaises(ImproperlyConfigured):
                    build_worker_settings(env)

    def test_local_only_accepts_loopback(self):
        env = environment(local=True)
        self.assertIn("InMemoryStorage", build_worker_settings(env)["STORAGES"]["default"]["BACKEND"])
        env.JYZ_REVIEW_ORIGIN = "http://public.example.test"
        with self.assertRaises(ImproperlyConfigured):
            build_worker_settings(env)


class StorageTests(SimpleTestCase):
    def storage(self, handler):
        client = httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=False)
        self.addCleanup(client.close)
        return SupabasePrivateStorage(PROJECT_URL, "jyz-prueba-fotos", "secret-only-for-test", client=client)

    def test_upload_uses_verified_mime_new_key_and_never_upserts(self):
        calls = []
        def handler(request):
            calls.append(request)
            return httpx.Response(200, json={"Key": "ok"})
        storage = self.storage(handler)
        for fmt, mime, suffix in [("JPEG", "image/jpeg", ".jpg"), ("PNG", "image/png", ".png"), ("WEBP", "image/webp", ".webp")]:
            stream = BytesIO()
            Image.new("RGB", (8, 8), "white").save(stream, format=fmt)
            name = storage.save("productos/original.jpg", ContentFile(stream.getvalue()))
            self.assertTrue(name.endswith(".webp"))
            self.assertEqual(calls[-1].headers["content-type"], "image/webp")
            with Image.open(BytesIO(calls[-1].content)) as saved:
                self.assertEqual(saved.format, "WEBP")
                self.assertEqual(saved.size, (8, 8))
            self.assertEqual(calls[-1].headers["x-upsert"], "false")
            self.assertEqual(calls[-1].headers["authorization"], "Bearer secret-only-for-test")
        self.assertEqual(len(calls), 3)
        self.assertNotIn("secret-only-for-test", repr(storage))

    def test_upload_rejects_invalid_large_or_disallowed_before_http(self):
        calls = []
        storage = self.storage(lambda request: calls.append(request))
        for data in [b"broken", b"0" * (MAX_BYTES + 1)]:
            with self.assertRaises(PhotoStorageError):
                storage.save("productos/prueba.png", ContentFile(data))
        stream = BytesIO()
        Image.new("RGB", (8, 8)).save(stream, format="GIF")
        with self.assertRaises(PhotoStorageError):
            storage.save("productos/prueba.gif", ContentFile(stream.getvalue()))
        self.assertFalse(calls)

    def test_optimization_resizes_corrects_orientation_and_removes_exif(self):
        calls = []
        storage = self.storage(lambda r: calls.append(r) or httpx.Response(200))
        source = Image.new("RGB", (2400, 1200), "red")
        exif = Image.Exif(); exif[274] = 6; exif[315] = "private metadata"
        stream = BytesIO(); source.save(stream, format="JPEG", exif=exif)
        storage.save("source.jpg", ContentFile(stream.getvalue()))
        with Image.open(BytesIO(calls[0].content)) as saved:
            self.assertEqual(saved.size, (800, 1600))
            self.assertFalse(saved.getexif())
        self.assertLessEqual(len(calls[0].content), 500 * 1024)

    def test_transparency_survives_and_output_weight_is_bounded(self):
        calls = []
        storage = self.storage(lambda r: calls.append(r) or httpx.Response(200))
        stream = BytesIO(); Image.new("RGBA", (40, 20), (255, 0, 0, 0)).save(stream, format="PNG")
        storage.save("alpha.png", ContentFile(stream.getvalue()))
        with Image.open(BytesIO(calls[0].content)) as saved:
            self.assertEqual(saved.size, (40, 20))
            self.assertEqual(saved.getpixel((0, 0))[3], 0)
        # Reducir un archivo que supera el presupuesto sin bajar la calidad fijada.
        noise = Image.effect_noise((1600, 1600), 100)
        stream = BytesIO(); noise.save(stream, format="PNG")
        storage.save("noise.png", ContentFile(stream.getvalue()))
        self.assertLessEqual(len(calls[1].content), 500 * 1024)
        with Image.open(BytesIO(calls[1].content)) as saved:
            self.assertLess(max(saved.size), 1600)

    def test_animation_and_encoder_failure_do_not_upload(self):
        calls = []
        storage = self.storage(lambda r: calls.append(r) or httpx.Response(200))
        stream = BytesIO()
        Image.new("RGB", (8, 8), "red").save(stream, format="WEBP", save_all=True,
            append_images=[Image.new("RGB", (8, 8), "blue")], duration=100)
        with self.assertRaises(PhotoStorageError):
            storage.save("animated.webp", ContentFile(stream.getvalue()))
        stream = BytesIO(); Image.new("RGB", (8, 8)).save(stream, format="PNG")
        with patch.object(Image.Image, "save", side_effect=OSError("private encoder detail")):
            with self.assertRaises(PhotoStorageError) as error:
                storage.save("source.png", ContentFile(stream.getvalue()))
            self.assertNotIn("private", str(error.exception))
        self.assertFalse(calls)

    def test_private_url_is_signed_same_origin_and_expires(self):
        def handler(request):
            self.assertEqual(request.method, "POST")
            self.assertIn(b'"expiresIn": 300', request.content)
            return httpx.Response(200, json={"signedURL": "/object/sign/jyz-prueba-fotos/productos/prueba.png?token=temporary"})
        storage = self.storage(handler)
        url = storage.url("productos/prueba.png")
        self.assertEqual(url, PROJECT_URL + "/storage/v1/object/sign/jyz-prueba-fotos/productos/prueba.png?token=temporary")
        self.assertNotIn("secret-only-for-test", url)

    def test_bad_signed_url_does_not_leak_key_or_redirect(self):
        for url in ["https://evil.test/photo", "//evil.test/photo", "/object/public/other/photo?token=x"]:
            with self.subTest(url=url):
                storage = self.storage(lambda request: httpx.Response(200, json={"signedURL": url}))
                with self.assertRaises(PhotoStorageError):
                    storage.url("productos/prueba.png")

    def test_http_failures_are_sanitized_and_not_reported_as_missing(self):
        for status in [302, 403, 500]:
            with self.subTest(status=status):
                storage = self.storage(lambda request: httpx.Response(status, text="secret-only-for-test", headers={"location":"https://evil.test"}))
                with self.assertRaises(PhotoStorageError) as error:
                    storage.exists("productos/prueba.png")
                self.assertNotIn("secret-only-for-test", str(error.exception))
        def network_error(request):
            raise httpx.ConnectError("secret-only-for-test", request=request)
        with self.assertRaises(PhotoStorageError) as error:
            self.storage(network_error).url("productos/prueba.png")
        self.assertNotIn("secret-only-for-test", str(error.exception))
        self.assertFalse(self.storage(lambda request: httpx.Response(404)).exists("productos/prueba.png"))

    def test_read_and_size_use_authenticated_api(self):
        def handler(request):
            # El transporte WASM no admite body nulo de HEAD; usar metadatos GET.
            self.assertEqual(request.method, "GET")
            if "/object/info/" in request.url.path:
                return httpx.Response(200, json={"size": 3, "metadata": {"size": "dato de usuario sin confiar"}})
            return httpx.Response(200, content=b"abc")
        storage = self.storage(handler)
        self.assertTrue(storage.exists("productos/prueba.png"))
        self.assertEqual(storage.open("productos/prueba.png").read(), b"abc")
        self.assertEqual(storage.size("productos/prueba.png"), 3)
        with self.assertRaises(SuspiciousFileOperation):
            storage.url("../secret")
        with self.assertRaises(NotImplementedError):
            storage.delete("productos/prueba.png")


class StorageFailureAdminTests(TestCase):
    def setUp(self):
        call_command("preparar_rol_catalogo", verbosity=0)
        user = User.objects.create_user("storage-editor", is_staff=True)
        user.groups.add(Group.objects.get(name="Responsable de catálogo"))
        self.client.force_login(user)
        self.product = Producto.objects.create(nombre="Prueba existente", descripcion="Descripción anterior",
                                               foto="productos/anterior.png", publicado=True)
        self.storage = self.product.foto.storage

    def test_failed_upload_rolls_back_edit_and_keeps_previous_reference(self):
        url = reverse("admin:catalogo_producto_change", args=[self.product.pk])
        with patch.object(self.storage, "save", side_effect=PhotoStorageError("simulado")):
            response = self.client.post(url, {"nombre": "No debe guardarse", "descripcion": "Nueva",
                                              "tallas": "[]", "orden": 0, "foto": foto(), "publicado": "on", "imagenes-TOTAL_FORMS": 0, "imagenes-INITIAL_FORMS": 0})
        self.assertRedirects(response, url, fetch_redirect_response=False)
        self.product.refresh_from_db()
        self.assertEqual(self.product.nombre, "Prueba existente")
        self.assertEqual(self.product.foto.name, "productos/anterior.png")
        self.assertContains(self.client.get(url), "No se guardaron los cambios")

    def test_signing_failure_keeps_catalog_and_admin_available(self):
        with patch.object(self.storage, "url", side_effect=PhotoStorageError("simulado")):
            self.assertContains(self.client.get(reverse("catalogo")), "La foto no está disponible temporalmente")
            self.assertEqual(self.client.get(reverse("admin:catalogo_producto_change", args=[self.product.pk])).status_code, 200)
