"""Tests."""


try:
    # Python 2.x
    from urlparse import urlsplit
except ImportError:
    # Python 3.x
    from urllib.parse import urlsplit

from django.http import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test.client import RequestFactory

from sslify.middleware import SSLifyMiddleware


class SSLifyMiddlwareTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_perma_redirects_http_to_https(self):
        request = self.factory.get('/woot/')
        self.assertTrue(request.build_absolute_uri().startswith('http://'))

        middleware = SSLifyMiddleware()
        result = middleware.process_request(request)

        self.assert_https_redirect(result)
        self.assertEqual(443, urlsplit(result['Location']).port)

    def test_custom_ssl_port(self):
        custom_port = 8443
        with self.settings(SSLIFY_PORT=custom_port):
            request = self.factory.get('/woot/')
            middleware = SSLifyMiddleware()
            request = middleware.process_request(request)

            self.assertEqual(custom_port, urlsplit(request['Location']).port)

    def test_disable_for_tests(self):
        with self.settings(SSLIFY_DISABLE=True):
            request = self.client.get('/woot/')
            self.assertEqual(404, request.status_code)

    def test_disable_for_url(self):
        def sslify_disable(request):
            return request.get_full_path().startswith('/disabled')

        with self.settings(SSLIFY_DISABLE_FOR_REQUEST=[sslify_disable]):
            middleware = SSLifyMiddleware()
            request = self.factory.get('/disabled/')
            request = middleware.process_request(request)
            self.assertIsNone(request)

            request = self.factory.get('/enabled/')
            result = middleware.process_request(request)
            self.assert_https_redirect(result)

    def assert_https_redirect(self, result):
        self.assertIsInstance(result, HttpResponsePermanentRedirect)
        self.assertTrue(result['Location'].startswith('https://'))

    def tearDown(self):
        del self.factory
