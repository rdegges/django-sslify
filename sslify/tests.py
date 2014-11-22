from django.http import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test.client import RequestFactory

from sslify.middleware import SSLifyMiddleware as _SSLifyMiddleware


class SSLifyMiddlware(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_perma_redirects_http_to_https(self):
        with self.settings(SSLIFY_DISABLE=False):
            request = self.factory.get('/woot/')
            self.assertTrue(request.build_absolute_uri().startswith('http://'))

            middleware = _SSLifyMiddleware()
            request = middleware.process_request(request)

            self.assertIsInstance(request, HttpResponsePermanentRedirect)
            self.assertTrue(request['Location'].startswith('https://'))

    def test_disable_for_tests(self):
        """If disabled, we get a 404"""
        with self.settings(SSLIFY_DISABLE=True):
            request = self.client.get('/woot/')
            self.assertEqual(404, request.status_code)

    def tearDown(self):
        del self.factory
