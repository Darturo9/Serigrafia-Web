"""Seguridad del perfil nativo y protección; nunca conecta a Railway/Supabase."""
import base64
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from django.core.exceptions import DisallowedHost, ImproperlyConfigured
from django.db import DatabaseError
from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase, override_settings

from .railway_middleware import ReviewAccessMiddleware
from .railway_settings import APP_USER, POOLER, PROJECT_URL, build_railway_settings


def environment(ca):
    return {"DJANGO_SECRET_KEY": "x" * 64, "JYZ_REVIEW_ORIGIN": "https://review.up.railway.app",
            "PGHOST": POOLER, "PGUSER": APP_USER, "PGDATABASE": "postgres", "PGPORT": "5432",
            "PGPASSWORD": "not-a-real-password", "PGSSLROOTCERT": str(ca), "JYZ_DB_SCHEMA": "jyz_prueba",
            "SUPABASE_URL": PROJECT_URL, "SUPABASE_STORAGE_KEY": "fake-storage-key",
            "JYZ_REVIEW_USER": "review-test", "JYZ_REVIEW_PASSWORD": "y" * 32}


class RailwaySettingsTests(SimpleTestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.ca = self.root / "ca.crt"
        self.ca.write_text("public-test-placeholder")

    def test_limited_role_tls_private_storage_and_secure_cookies(self):
        result = build_railway_settings(environment(self.ca), self.root)
        self.assertFalse(result["DEBUG"])
        self.assertTrue(result["SESSION_COOKIE_SECURE"])
        self.assertTrue(result["CSRF_COOKIE_SECURE"])
        db = result["DATABASES"]["default"]
        self.assertEqual(db["USER"], APP_USER)
        self.assertEqual(db["OPTIONS"]["sslmode"], "verify-full")
        self.assertEqual(db["OPTIONS"]["options"], "-c search_path=jyz_prueba")
        self.assertEqual(result["STORAGES"]["default"]["OPTIONS"]["bucket"], "jyz-prueba-fotos")
        self.assertNotIn("*", result["ALLOWED_HOSTS"])

    def test_missing_secrets_or_changed_destinations_fail_closed(self):
        for name, value in (("PGPASSWORD", ""), ("PGUSER", "postgres"), ("JYZ_DB_SCHEMA", "public"),
                            ("PGHOST", "other.supabase.co"), ("PGPORT", "6543"),
                            ("SUPABASE_URL", "https://other.supabase.co"), ("SUPABASE_STORAGE_KEY", ""),
                            ("DJANGO_SECRET_KEY", "short"), ("JYZ_REVIEW_PASSWORD", "short"),
                            ("PGSSLROOTCERT", str(self.root / "missing.crt"))):
            with self.subTest(name=name):
                env = environment(self.ca)
                env[name] = value
                with self.assertRaises(ImproperlyConfigured):
                    build_railway_settings(env, self.root)

    def test_origin_cannot_allow_http_wildcards_credentials_or_paths(self):
        for origin in ("http://review.up.railway.app", "https://*", "https://user:pass@review.test",
                       "https://review.test/path", "https://review.test?key=x", "https://review.test:443"):
            with self.subTest(origin=origin):
                env = environment(self.ca)
                env["JYZ_REVIEW_ORIGIN"] = origin
                with self.assertRaises(ImproperlyConfigured):
                    build_railway_settings(env, self.root)


@override_settings(ALLOWED_HOSTS=["review.up.railway.app", "healthcheck.railway.app"],
                   JYZ_REVIEW_USER="review-test", JYZ_REVIEW_PASSWORD="y" * 32)
class RailwayAccessTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.auth = "Basic " + base64.b64encode(("review-test:" + "y" * 32).encode()).decode()
        self.calls = []
        def downstream(request):
            self.calls.append(request.path)
            return HttpResponse("protected")
        self.middleware = ReviewAccessMiddleware(downstream)

    def request(self, path, **kwargs):
        return self.factory.get(path, HTTP_HOST="review.up.railway.app", secure=True, **kwargs)

    def test_public_pages_open_without_review(self):
        for path in ("/", "/inicio/", "/productos/4/", "/static/catalogo/inicio.css"):
            response = self.middleware(self.request(path))
            self.assertEqual(response.status_code, 200)
            self.assertIn("noindex", response["X-Robots-Tag"])
        self.assertEqual(self.calls, ["/", "/inicio/", "/productos/4/", "/static/catalogo/inicio.css"])

    def test_technical_catalogue_requires_review_before_downstream(self):
        for path in ("/catalogo/",):
            response = self.middleware(self.request(path))
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response["Cache-Control"], "no-store")
            self.assertIn("noindex", response["X-Robots-Tag"])
        self.assertFalse(self.calls)
        for auth in ("Basic invalid", "Bearer " + self.auth, "Basic ü"):
            self.assertEqual(self.middleware(self.request("/catalogo/", HTTP_AUTHORIZATION=auth)).status_code, 401)

    def test_admin_and_assets_reach_django_without_basic_challenge(self):
        for path in ("/admin/", "/admin/login/", "/static/admin/css/base.css"):
            response = self.middleware(self.request(path))
            self.assertEqual(response.status_code, 200)
            self.assertNotIn('WWW-Authenticate', response)
            self.assertIn('noindex', response['X-Robots-Tag'])

    def test_valid_review_does_not_bypass_django_authentication(self):
        response = self.middleware(self.request("/admin/login/", HTTP_AUTHORIZATION=self.auth))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.calls, ["/admin/login/"])
        self.assertIn("noindex", response["X-Robots-Tag"])

    def test_healthcheck_is_exact_checks_db_and_sanitizes_failure(self):
        with patch("config.railway_middleware.connection") as conn:
            response = self.middleware(self.request("/healthz/"))
            self.assertEqual(response.status_code, 200)
            conn.cursor.return_value.__enter__.return_value.execute.assert_called_once_with("SELECT 1")
        with patch("config.railway_middleware.connection") as conn:
            conn.cursor.side_effect = DatabaseError("password-private-example")
            response = self.middleware(self.request("/healthz/"))
            self.assertEqual(response.status_code, 503)
            self.assertNotIn(b"password-private-example", response.content)
        self.assertFalse(self.calls)
        # Otra ruta bajo /healthz/ no ejecuta el chequeo; sigue a Django (que responde 404).
        self.middleware(self.request("/healthz/anything"))
        self.assertEqual(self.calls, ["/healthz/anything"])

    def test_host_validation_and_health_host_cannot_open_the_site(self):
        with self.assertRaises(DisallowedHost):
            self.middleware(self.factory.get("/healthz/", HTTP_HOST="evil.test"))
        response = self.middleware(self.factory.get("/inicio/", HTTP_HOST="healthcheck.railway.app",
                                                  secure=True, HTTP_AUTHORIZATION=self.auth))
        self.assertEqual(response.status_code, 404)
        self.assertFalse(self.calls)

    def test_http_never_accepts_basic_credentials(self):
        response = self.middleware(self.factory.get("/inicio/", HTTP_HOST="review.up.railway.app",
                                                  HTTP_AUTHORIZATION=self.auth))
        self.assertEqual(response.status_code, 400)
        self.assertFalse(self.calls)

    @override_settings(JYZ_PUBLIC_LAUNCH=True)
    def test_lanzamiento_conserva_panel_privado_y_noindex_en_post_y_errores(self):
        self.assertNotIn('X-Robots-Tag',self.middleware(self.request('/')))
        self.assertIn('noindex',self.middleware(self.request('/admin/login/'))['X-Robots-Tag'])
        request=self.factory.post('/',HTTP_HOST='review.up.railway.app',secure=True)
        self.assertIn('noindex',self.middleware(request)['X-Robots-Tag'])


from django.test import TestCase
from .settings_base import MIDDLEWARE as BASE_MIDDLEWARE


@override_settings(ALLOWED_HOSTS=['testserver'], JYZ_REVIEW_USER='review-test',
                   JYZ_REVIEW_PASSWORD='y' * 32,
                   MIDDLEWARE=['config.railway_middleware.ReviewAccessMiddleware', *BASE_MIDDLEWARE])
class AdminSingleLoginTests(TestCase):
    def test_django_authentication_and_permissions_remain_required(self):
        from django.contrib.auth.models import User, Permission
        from catalogo.models import Producto
        self.assertEqual(self.client.get('/admin/', secure=True).status_code, 302)
        login = self.client.get('/admin/login/', secure=True)
        self.assertEqual(login.status_code, 200)
        self.assertNotIn('WWW-Authenticate', login)
        self.assertIn('noindex', login['X-Robots-Tag'])
        self.assertEqual(self.client.get('/admin/catalogo/producto/', secure=True).status_code, 302)
        user = User.objects.create_user('editor-local', password='local-only-test', is_staff=True)
        user.user_permissions.add(Permission.objects.get(codename='view_producto'))
        self.assertTrue(self.client.login(username='editor-local', password='local-only-test'))
        self.assertEqual(self.client.get('/admin/catalogo/producto/', secure=True).status_code, 200)
        self.assertEqual(self.client.get('/admin/auth/user/', secure=True).status_code, 403)
        product = Producto.objects.create(nombre='Fixture', descripcion='Prueba local')
        self.assertEqual(self.client.get(f'/admin/catalogo/producto/{product.pk}/delete/', secure=True).status_code, 403)
