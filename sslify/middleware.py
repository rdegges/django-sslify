"""Django middlewares."""


try:
    # Python 2.x
    from urlparse import urlsplit, urlunsplit
except ImportError:
    # Python 3.x
    from urllib.parse import urlsplit
    from urllib.parse import urlunsplit

from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class SSLifyMiddleware(object):
    """Force all requests to use HTTPs. If we get an HTTP request, we'll just
    force a redirect to HTTPs.

    .. note::
        You can also disable this middleware when testing by setting
        ``settings.SSLIFY_DISABLE`` to True.
    """
    def process_request(self, request):
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
            url_secure_split = (scheme, "%s:%d" % (url_split.hostname or '', ssl_port)) + url_split[2:]
            secure_url = urlunsplit(url_secure_split)

            return HttpResponsePermanentRedirect(secure_url)
