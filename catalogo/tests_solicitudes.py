from urllib.parse import parse_qs, urlsplit
from django.test import TestCase
from .models import Producto
from .solicitudes import CotizacionForm, SeguimientoForm


class SolicitudesTests(TestCase):
    def test_todas_las_tallas_recoge_solicitud_sin_inventar_opciones(self):
        producto = Producto.objects.create(nombre='Camiseta local', descripcion='Fixture',
                                          publicado=True, tallas=['Todas las tallas'])
        form = CotizacionForm(producto.pk, data={'cantidad': 3, 'tallas_solicitadas': '2 M y 1 L'})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertNotIn('talla_0', form.fields)
        self.assertIn('Tallas solicitadas: 2 M y 1 L', form.mensaje())
        self.assertIn('confirmen disponibilidad, precio y entrega', form.mensaje())
        self.assertFalse(CotizacionForm(producto.pk, data={'cantidad': 0}).is_valid())

    def setUp(self):
        # Datos exclusivos de la base temporal de tests, no catálogo comercial.
        self.producto = Producto.objects.create(
            nombre="Prenda & diseño ñ de prueba", descripcion="Fixture", publicado=True,
            tallas=["S", "M"],
        )

    def test_mensaje_y_destino_con_acentos_y_saltos(self):
        form = CotizacionForm(self.producto.pk, data={"cantidad": 3, "talla_0": 1, "talla_1": 2})
        self.assertTrue(form.is_valid(), form.errors)
        url = urlsplit(form.url_whatsapp())
        self.assertEqual((url.scheme, url.netloc, url.path), ("https", "wa.me", "/50247233834"))
        mensaje = parse_qs(url.query)["text"][0]
        self.assertIn(self.producto.nombre, mensaje)
        self.assertIn("- M: 2\n", mensaje)
        self.assertNotIn("Colores de impresión", mensaje)
        self.assertIn("directamente en este chat", mensaje)
        self.assertEqual(Producto.objects.count(), 1)

    def test_distribucion_debe_sumar_total(self):
        form = CotizacionForm(self.producto.pk, data={"cantidad": 3, "talla_0": 1, "talla_1": 1})
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValueError):
            form.url_whatsapp()

    def test_rechaza_cantidades_invalidas(self):
        for datos in ({"cantidad": 0}, {"cantidad": "1.5"},
                      {"cantidad": 1, "talla_0": -1}):
            with self.subTest(datos=datos):
                self.assertFalse(CotizacionForm(self.producto.pk, data=datos).is_valid())

    def test_producto_oculto_o_ejemplo_no_solicitable(self):
        for campo in ("publicado", "es_ejemplo"):
            setattr(self.producto, campo, campo == "es_ejemplo")
            self.producto.save()
            self.assertFalse(CotizacionForm(self.producto.pk, data={"cantidad": 1}).is_valid())
            self.producto.publicado, self.producto.es_ejemplo = True, False

    def test_ocultacion_o_cambio_tallas_durante_validacion(self):
        for cambios in ({"publicado": False}, {"tallas": ["L"]}):
            form = CotizacionForm(self.producto.pk, data={"cantidad": 1, "talla_0": 1})
            Producto.objects.filter(pk=self.producto.pk).update(**cambios)
            self.assertFalse(form.is_valid())
            self.producto.save()

    def test_opciones_sin_confirmar_y_colores_retirados(self):
        self.producto.tallas = []
        self.producto.save()
        form = CotizacionForm(self.producto.pk, data={"cantidad": 2, "colores": 3})
        self.assertTrue(form.is_valid())
        self.assertIn("Tallas/opciones: necesito consultarlas.", form.mensaje())
        self.assertNotIn("colores", form.fields)
        self.assertNotIn("Colores de impresión", form.mensaje())

    def test_seguimiento_no_inventa_estado(self):
        for ref in ("", "JYZ-ñ & 1"):
            form = SeguimientoForm(data={"referencia": ref})
            self.assertTrue(form.is_valid())
            self.assertIn(ref, parse_qs(urlsplit(form.url_whatsapp()).query)["text"][0])
            self.assertNotIn("completado", form.mensaje())
        self.assertFalse(SeguimientoForm(data={"referencia": "uno\ndos"}).is_valid())
