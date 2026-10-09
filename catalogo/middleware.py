from config.publicacion import pagina_indexable
class ReviewOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not pagina_indexable(request, response):
            response["X-Robots-Tag"] = "noindex, nofollow"
        elif "X-Robots-Tag" in response:
            del response["X-Robots-Tag"]
        return response
