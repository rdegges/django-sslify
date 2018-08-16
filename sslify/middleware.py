"""Django middlewares."""
from django.conf import settings
from django.http import HttpResponsePermanentRedirect

from sslify.compat import MiddlewareMixin, urlsplit, urlunsplit


class SSLifyMiddleware(MiddlewareMixin):
    """Force all requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        You can also disable this middleware when testing by setting
        ``settings.SSLIFY_DISABLE`` to True.
    """
    @staticmethod
    def process_request(request):
        # If the user has explicitly disabled SSLify, do nothing.
        if getattr(settings, 'SSLIFY_DISABLE', False):
            return None

        # Evaluate callables that can disable SSL for the current request
        per_request_disables = getattr(settings, 'SSLIFY_DISABLE_FOR_REQUEST', [])
        for should_disable in per_request_disables:
            if should_disable(request):
                return None

        # If we get here, proceed as normal.
        if not request.is_secure():
            url = request.build_absolute_uri(request.get_full_path())
            url_split = urlsplit(url)
            scheme = 'https' if url_split.scheme == 'http' else url_split.scheme
            ssl_port = getattr(settings, 'SSLIFY_PORT', 443)
            ssl_domain = getattr(settings, 'SSLIFY_DOMAIN', url_split.hostname)
            url_secure_split = (scheme, "%s:%d" % (ssl_domain or '', ssl_port)) + url_split[2:]
            secure_url = urlunsplit(url_secure_split)

            return HttpResponsePermanentRedirect(secure_url)
