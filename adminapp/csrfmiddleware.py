from django.conf import settings

class CsrfHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.META.get('HTTP_REFERER'):
            # Set the CSRF token in the header
            request.META[settings.CSRF_HEADER_NAME] = request.META.get('CSRF_COOKIE')
        response = self.get_response(request)
        return response