"""Compat module to provide backwards compatibility with older versions"""

try:
    # Django 1.10
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # Django <1.10
    class MiddlewareMixin(object):
        def __init__(self, get_response=None):
            self.get_response = get_response
            super(MiddlewareMixin, self).__init__()

        def __call__(self, request):
            response = None

            if hasattr(self, 'process_request'):
                response = self.process_request(request)

            if not response:
                response = self.get_response(request)

            if hasattr(self, 'process_response'):
                response = self.process_response(request, response)

            return response

try:
    # Python 2.x
    from urlparse import urlsplit, urlunsplit
except ImportError:
    # Python 3.x
    from urllib.parse import urlsplit
    from urllib.parse import urlunsplit
