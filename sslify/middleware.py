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
        This will only take effect if ``settings.DEBUG`` is False.

    .. note::
        You can also disable this middleware when testing by setting
        ``settings.SSLIFY_DISABLE`` to True.
    """
    def process_request(self, request):
        # If the user has explicitly disabled SSLify, do nothing.
        if getattr(settings, 'SSLIFY_DISABLE', settings.DEBUG):
            return None

        # Evaluate callables that can disable SSL for the current request
        per_request_disables = getattr(settings, 'SSLIFY_DISABLE_FOR_REQUEST', [])
        for should_disable in per_request_disables:
            if should_disable(request):
                return None

        try:
            shorten_to_root_domain = getattr(settings, 'SSLIFY_SHORTEN_TO_ROOT_DOMAIN', False)

            hostname = url_split.hostname

            if shorten_to_root_domain:
                hostname = hostname.replace('www.', '')
        except Exception, e:
                print e.message

        # If we get here, proceed as normal.
        if not request.is_secure():
            try:
                url = request.build_absolute_uri(request.get_full_path())
                url_split = urlsplit(url)

                scheme = 'https' if url_split.scheme == 'http' else url_split.scheme

                ssl_port = getattr(settings, 'SSLIFY_PORT', 443)

                url_secure_split = (scheme, "%s:%d" % (hostname or '', ssl_port)) + url_split[2:]
                secure_url = urlunsplit(url_secure_split)
            except Exception, e:
                print e.message

            return HttpResponsePermanentRedirect(secure_url)
