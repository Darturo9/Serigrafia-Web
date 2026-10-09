from django.test import TestCase, override_settings
from .models import Producto


class PublicacionTests(TestCase):
    @override_settings(JYZ_PUBLIC_LAUNCH=True, JYZ_SHOW_REVIEW_EXAMPLES=False)
    def test_logo_social_publico_con_urls_absolutas_sin_consultas(self):
        real = Producto.objects.create(nombre='Camiseta & estilo', descripcion='fixture', publicado=True)
        for path, canonical in [('/', '/'), ('/inicio/', '/'),
                                (f'/productos/{real.pk}/', f'/productos/{real.pk}/')]:
            response = self.client.get(path + '?idea=texto-privado', HTTP_USER_AGENT='facebookexternalhit/1.1')
            self.assertContains(response, 'property="og:image" content="https://jyzgt.com/static/catalogo/logo-jyz-del-pdf.jpg"')
            self.assertContains(response, f'property="og:url" content="https://jyzgt.com{canonical}"')
            self.assertContains(response, f'rel="canonical" href="https://jyzgt.com{canonical}"')
            self.assertNotContains(response, 'texto-privado')
        self.assertContains(response, 'property="og:title" content="Camiseta &amp; estilo"')

    @override_settings(JYZ_PUBLIC_LAUNCH=True, JYZ_SHOW_REVIEW_EXAMPLES=False)
    def test_publicacion_sin_ejemplos_y_rutas_privadas_no_indexables(self):
        hidden=Producto.objects.create(nombre='Oculto',descripcion='fixture')
        sample=Producto.objects.create(nombre='Ejemplo',descripcion='fixture',publicado=True,es_ejemplo=True)
        real=Producto.objects.create(nombre='Producto autorizado de prueba local',descripcion='fixture',publicado=True)
        for path in ['/', '/inicio/', f'/productos/{real.pk}/']:
            response=self.client.get(path)
            self.assertEqual(response.status_code,200)
            self.assertNotContains(response,'Vista de revisión')
            self.assertNotContains(response,'noindex')
            self.assertNotIn('X-Robots-Tag',response)
        for pk in [hidden.pk,sample.pk]:
            response=self.client.get(f'/productos/{pk}/')
            self.assertEqual(response.status_code,404)
            self.assertIn('noindex',response['X-Robots-Tag'])
        self.assertIn('noindex',self.client.get('/admin/login/')['X-Robots-Tag'])
        self.assertIn('noindex',self.client.get('/catalogo/')['X-Robots-Tag'])
        sitemap=self.client.get('/sitemap.xml')
        self.assertContains(sitemap,f'/productos/{real.pk}/')
        self.assertNotContains(sitemap,f'/productos/{sample.pk}/')
        self.assertNotContains(sitemap,f'/productos/{hidden.pk}/')
        self.assertContains(self.client.get('/robots.txt'),'Disallow: /admin')

    @override_settings(JYZ_PUBLIC_LAUNCH=True)
    def test_post_con_idea_personal_no_se_indexa_y_catalogo_vacio_es_util(self):
        response=self.client.get('/')
        self.assertContains(response,'Estamos preparando el catálogo.')
        self.assertContains(response,'name="idea"')
        response=self.client.post('/',{'accion':'idea','idea':'Idea de prueba con acento ñ'})
        self.assertContains(response,'Revisa tu mensaje')
        self.assertIn('noindex',response['X-Robots-Tag'])
        self.assertEqual(Producto.objects.count(),0)

    @override_settings(JYZ_PUBLIC_LAUNCH=False)
    def test_revision_conserva_noindex(self):
        response=self.client.get('/')
        self.assertContains(response,'Vista de revisión')
        self.assertIn('noindex',response['X-Robots-Tag'])
        self.assertContains(self.client.get('/robots.txt'),'Disallow: /')
