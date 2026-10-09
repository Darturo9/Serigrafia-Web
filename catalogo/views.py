from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Producto, GaleriaImagen
from config.storage.supabase import PhotoStorageError


def catalogo(request):
    productos = list(Producto.objects.filter(publicado=True))
    for producto in productos:
        producto.foto_url = ""
        producto.foto_error = False
        if producto.foto:
            try:
                producto.foto_url = producto.foto.url
            except PhotoStorageError:
                producto.foto_error = True
    return render(request, "catalogo/catalogo.html", {"productos": productos})


def inicio(request):
    from .solicitudes import CotizacionForm, IdeaForm, enlace_whatsapp
    consulta = productos_visibles().prefetch_related("imagenes")
    productos = list(consulta)
    for producto in productos:
        fotos = fotos_visibles(producto, solo_portada=True)
        producto.foto_url = fotos[0]["url"] if fotos else ""
        producto.foto_alt = fotos[0]["descripcion"] if fotos else producto.nombre
    seleccion = request.POST.get("producto") if request.method == "POST" else request.GET.get("producto")
    try:
        producto_id = int(seleccion) if seleccion else None
    except (ValueError, TypeError):
        producto_id = None
    accion = request.POST.get("accion") if request.method == "POST" else None
    cotizacion = CotizacionForm(producto_id, data=request.POST if accion == "cotizar" else None) if seleccion or accion == "cotizar" else None
    mensaje, enlace = "", ""
    idea = IdeaForm(data=request.POST if accion == "idea" else None)
    form = cotizacion if accion == "cotizar" else idea if accion == "idea" else None
    if form is not None and form.is_valid():
        mensaje, enlace = form.mensaje(), form.url_whatsapp()
    galeria = []
    for imagen in GaleriaImagen.objects.filter(activo=True):
        if not imagen.foto:
            continue
        try:
            galeria.append({"titulo": imagen.titulo, "descripcion": imagen.descripcion,
                            "url": imagen.foto.url})
        except PhotoStorageError:
            continue
    return render(request, "catalogo/inicio.html", {
        "galeria": galeria,
        "productos": productos, "productos_cotizables": any(not p.es_ejemplo for p in productos),
        "cotizacion": cotizacion, "idea": idea,
        "mensaje": mensaje, "enlace_mensaje": enlace, "accion": accion,
        "personalizacion_url": enlace_whatsapp("Hola JYZ, quisiera consultar qué puedo personalizar. Me interesan camisetas, hoodies u otra idea. ¿Qué prendas, materiales y opciones pueden trabajar?"),
        "whatsapp_url": enlace_whatsapp("Hola JYZ, quisiera conversar sobre una idea para personalizar."),
    })


def productos_visibles():
    consulta = Producto.objects.filter(publicado=True)
    if not getattr(settings, "JYZ_SHOW_REVIEW_EXAMPLES", False):
        consulta = consulta.filter(es_ejemplo=False)
    return consulta


def fotos_visibles(producto, solo_portada=False):
    imagenes = [i for i in producto.imagenes.all() if i.activo]
    imagenes.sort(key=lambda i: (i.pk != producto.portada_id, i.orden, i.pk))
    fuentes = [(i.foto, i.descripcion) for i in imagenes]
    if not fuentes and producto.foto and not producto.imagenes.exists():
        fuentes = [(producto.foto, producto.texto_foto)]
    fotos = []
    for archivo, descripcion in fuentes[:6]:
        if not archivo:
            continue
        try:
            fotos.append({"url": archivo.url, "descripcion": descripcion or producto.nombre})
        except PhotoStorageError:
            continue
        if solo_portada and fotos:
            break
    return fotos


def producto_detalle(request, pk):
    from .solicitudes import CotizacionForm, enlace_whatsapp
    producto = get_object_or_404(productos_visibles().prefetch_related("imagenes"), pk=pk)
    cotizacion = None if producto.es_ejemplo else CotizacionForm(producto.pk, data=request.POST if request.method == "POST" else None)
    mensaje, enlace = "", ""
    if request.method == "POST" and cotizacion is not None and cotizacion.is_valid():
        mensaje, enlace = cotizacion.mensaje(), cotizacion.url_whatsapp()
    return render(request, "catalogo/producto_detalle.html", {
        "producto": producto, "fotos": fotos_visibles(producto), "cotizacion": cotizacion,
        "mensaje": mensaje, "enlace_mensaje": enlace,
        "whatsapp_url": enlace_whatsapp("Hola JYZ, quisiera conversar sobre una idea para personalizar."),
    })


def robots(request):
    from django.http import HttpResponse
    if not getattr(settings, "JYZ_PUBLIC_LAUNCH", False):
        return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")
    origin = request.build_absolute_uri("/").rstrip("/")
    return HttpResponse(f"User-agent: *\nDisallow: /admin\nDisallow: /catalogo/\nDisallow: /media/\nDisallow: /static/admin/\nSitemap: {origin}/sitemap.xml\n", content_type="text/plain")


def sitemap(request):
    from django.http import HttpResponse
    from xml.sax.saxutils import escape
    from django.urls import reverse
    paths = ["/"]
    if getattr(settings, "JYZ_PUBLIC_LAUNCH", False):
        paths += [reverse("producto_detalle", args=[pk]) for pk in productos_visibles().values_list("pk", flat=True)]
    urls = "".join(f"<url><loc>{escape(request.build_absolute_uri(path))}</loc></url>" for path in paths)
    return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>',content_type="application/xml")
