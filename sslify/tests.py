try:
    # Python 2.x
    from urlparse import urlsplit
except ImportError:
    # Python 3.x
    from urllib.parse import urlsplit

from django.http import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test.client import RequestFactory

from sslify.middleware import SSLifyMiddleware as _SSLifyMiddleware


class SSLifyMiddlware(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_perma_redirects_http_to_https(self):
        request = self.factory.get('/woot/')
        self.assertTrue(request.build_absolute_uri().startswith('http://'))

        middleware = _SSLifyMiddleware()
        request = middleware.process_request(request)

        self.assertIsInstance(request, HttpResponsePermanentRedirect)
        self.assertTrue(request['Location'].startswith('https://'))
        self.assertEqual(443, urlsplit(request['Location']).port)

    def test_custom_ssl_port(self):
        custom_port = 8443
        with self.settings(SSL_PORT=custom_port):
            request = self.factory.get('/woot/')
            middleware = _SSLifyMiddleware()
            request = middleware.process_request(request)

            self.assertEqual(custom_port, urlsplit(request['Location']).port)

    def test_disable_for_tests(self):
        """If disabled, we get a 404"""
        with self.settings(SSLIFY_DISABLE=True):
            request = self.client.get('/woot/')
            self.assertEqual(404, request.status_code)

    def tearDown(self):
        del self.factory
