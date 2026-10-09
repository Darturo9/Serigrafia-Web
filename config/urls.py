from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from catalogo.views import catalogo, inicio, producto_detalle, robots, sitemap

urlpatterns = [path("robots.txt", robots), path("sitemap.xml", sitemap), path("productos/<int:pk>/", producto_detalle, name="producto_detalle"), path("", inicio, name="inicio"), path("inicio/", inicio), path("catalogo/", catalogo, name="catalogo"), path("admin/", admin.site.urls)]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if getattr(settings, "JYZ_WORKER_LOCAL", False):
    from config.local_media import local_media
    from config.local_probe import local_probe
    urlpatterns += [path("media/<path:name>", local_media), path("__prueba__/runtime/", local_probe)]
