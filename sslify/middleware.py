from django.conf import settings
from django.core import mail
from django.http import HttpResponsePermanentRedirect


class SSLifyMiddleware(object):
    """Force all requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        This will only take effect if ``settings.DEBUG`` is False.

    .. note::
        You can also disable this middleware when testing by setting
        ``settings.SSLIFY_DISABLE`` to True
    """
    def process_request(self, request):
        # disabled for test mode?
        if getattr(settings, 'SSLIFY_DISABLE', False) and \
                hasattr(mail, 'outbox'):
            return None

        # proceed as normal
        if not any((settings.DEBUG, request.is_secure())):
            path  = request.path
            exempt_urls = getattr(settings,'SSLIFY_EXEMPT_PATHS', [])
            if path not in exempt_urls:
                url = request.build_absolute_uri(request.get_full_path())
                secure_url = url.replace('http://', 'https://')
                return HttpResponsePermanentRedirect(secure_url)