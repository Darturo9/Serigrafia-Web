"""Indexación únicamente de páginas públicas GET/HEAD exitosas."""
import re
from django.conf import settings
from django.templatetags.static import static
from urllib.parse import urljoin


def pagina_indexable(request, response):
    return (getattr(settings, 'JYZ_PUBLIC_LAUNCH', False)
            and request.method in ('GET', 'HEAD') and response.status_code == 200
            and (request.path in ('/', '/inicio/', '/robots.txt', '/sitemap.xml')
                 or re.fullmatch(r'/productos/[0-9]+/', request.path)))


def contexto_publicacion(request):
    origin = settings.JYZ_PUBLIC_ORIGIN
    path = request.path if re.fullmatch(r'/productos/[0-9]+/', request.path) else '/'
    return {
        'publicacion_activa': getattr(settings, 'JYZ_PUBLIC_LAUNCH', False),
        'url_compartir': urljoin(origin, path),
        'logo_compartir': urljoin(origin, static('catalogo/logo-jyz-del-pdf.jpg')),
    }
