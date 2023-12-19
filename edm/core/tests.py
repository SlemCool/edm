from http import HTTPStatus

from django.test import TestCase


class ErrorPagesTests(TestCase):
    def test_not_found_page(self):
        response = self.client.get('/nonexist-page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertTemplateUsed(response, 'core/404.html')
