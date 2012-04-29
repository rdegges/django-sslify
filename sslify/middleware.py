from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class SSLifyMiddleware(object):
    """Force all requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        This will only take effect if ``settings.DEBUG`` is False.
    """
    def process_request(self, request):
        if not any((settings.DEBUG, request.is_secure(), request.META.get('HTTP_X_FORWARDED_PROTO', '') == 'https')):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(secure_url)
