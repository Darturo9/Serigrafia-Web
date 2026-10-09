from django.test import TestCase, Client, override_settings
from .models import Producto

class InicioTests(TestCase):
    def test_catalogo_comercial_excluye_ejemplos_y_ocultos(self):
        Producto.objects.create(nombre="Ejemplo que no se debe mostrar",descripcion="Fixture",publicado=True,es_ejemplo=True)
        Producto.objects.create(nombre="Oculto que no se debe mostrar",descripcion="Fixture")
        real=Producto.objects.create(nombre="Fixture publicada ñ",descripcion="<script>texto</script>",publicado=True)
        response=self.client.get("/inicio/")
        self.assertContains(response,real.nombre)
        self.assertContains(response,"&lt;script&gt;texto&lt;/script&gt;")
        self.assertNotContains(response,"Ejemplo que no se debe mostrar")
        self.assertNotContains(response,"Oculto que no se debe mostrar")
    def test_cotizacion_valida_y_error_no_crean_pedidos(self):
        producto=Producto.objects.create(nombre="Fixture",descripcion="Prueba",publicado=True,tallas=["M"])
        datos={"accion":"cotizar","producto":producto.pk,"cantidad":2,"talla_0":1}
        self.assertContains(self.client.post("/inicio/",datos),"La suma de las cantidades")
        datos["talla_0"]=2
        response=self.client.post("/inicio/",datos)
        self.assertContains(response,"Revisa tu mensaje")
        self.assertContains(response,"wa.me/50247233834?text=")
        self.assertEqual(Producto.objects.count(),1)
    def test_idea_libre_prepara_mensaje_whatsapp(self):
        self.assertContains(self.client.get("/inicio/"),'name="idea"')
        self.assertContains(self.client.post("/inicio/",{"accion":"idea","idea":"   "}),"errorlist")
        response=self.client.post("/inicio/",{"accion":"idea","nombre":"Ana","prenda":"Hoodies","cantidad":12,"fecha":"2099-12-24","idea":"Logo naranja\nen la espalda"})
        self.assertContains(response,"Revisa tu mensaje")
        mensaje=response.context["mensaje"]
        self.assertIn("Hola JYZ, soy Ana.",mensaje)
        self.assertIn("*Producto:* Hoodies",mensaje)
        self.assertIn("*Cantidad aproximada:* 12",mensaje)
        self.assertIn("*Para el:* 24/12/2099",mensaje)
        self.assertContains(self.client.post("/inicio/",{"accion":"idea","idea":"x","fecha":"2000-01-01"}),"Elige una fecha a partir de hoy.")
        self.assertIn("Logo naranja\nen la espalda",mensaje)
        self.assertIn("wa.me/50247233834?text=",response.context["enlace_mensaje"])
        self.assertEqual(Producto.objects.count(),0)
    def test_contacto_en_footer_y_csrf(self):
        self.assertEqual(Client(enforce_csrf_checks=True).post("/inicio/", {"accion": "cotizar"}).status_code, 403)
        response = self.client.get("/inicio/")
        self.assertContains(response, '<footer class="pie" id="contacto">')
        self.assertContains(response, 'href="#contacto">Contacto</a>')
        footer = response.content.decode().split('<footer')[1].split('</footer>')[0]
        self.assertIn('wa.me/50247233834?text=', footer)
        self.assertIn('WhatsApp · +502 4723 3834', footer)
        self.assertIn('https://www.instagram.com/atrevete_jyz21/', footer)
        self.assertNotContains(response, "Sigamos en contacto")
        self.assertNotContains(response, 'name="referencia"')
        response = self.client.post("/inicio/", {"accion": "seguimiento", "referencia": "JYZ-ñ 1"})
        self.assertNotContains(response, "Referencia: JYZ-ñ 1")
        self.assertNotContains(response, "Revisa tu mensaje")

    @override_settings(JYZ_SHOW_REVIEW_EXAMPLES=True)
    def test_ejemplo_de_revision_visible_pero_no_cotizable(self):
        ejemplo=Producto.objects.create(nombre="Prenda de prueba", descripcion="Referencia", publicado=True, es_ejemplo=True)
        Producto.objects.create(nombre="Ejemplo oculto", descripcion="Referencia", es_ejemplo=True)
        response=self.client.get("/inicio/")
        self.assertContains(response,ejemplo.nombre)
        self.assertContains(response,"no disponible para venta")
        self.assertNotContains(response,"Ejemplo oculto")
        self.assertNotContains(response,"Elige un producto del catálogo")
        self.assertContains(response,'name="accion" value="idea"')
        self.assertNotContains(response,f"?producto={ejemplo.pk}#cotizacion")
        response=self.client.post("/inicio/",{"accion":"cotizar","producto":ejemplo.pk,"cantidad":1})
        self.assertNotContains(response,"Revisa tu mensaje")
        self.assertContains(response,"errorlist")


class RaizTests(TestCase):
    def test_raiz_muestra_inicio_y_catalogo_tecnico_se_mueve(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "catalogo/inicio.html")
        self.assertContains(response, 'action="/#cotizacion"')
        self.assertEqual(self.client.get("/inicio/").status_code, 200)
        self.assertTemplateUsed(self.client.get("/catalogo/"), "catalogo/catalogo.html")
