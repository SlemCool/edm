from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse


class UsersURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()

    def test_user_url_desired_location(self):
        """URL-адрес доступен."""
        url_names = {
            '/auth/login/': HTTPStatus.OK,
            '/auth/signup/': HTTPStatus.OK,
            '/auth/password_reset/': HTTPStatus.OK,
            '/auth/password_reset/done/': HTTPStatus.OK,
            '/auth/logout/': HTTPStatus.OK,
        }
        for url, expected_code in url_names.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, expected_code)

    def test_users_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        url_names = {
            '/auth/login/': 'users/login.html',
            '/auth/signup/': 'users/signup.html',
            '/auth/password_reset/': 'users/password_reset_form.html',
            '/auth/password_reset/done/': 'users/password_reset_done.html',
            '/auth/logout/': 'users/logged_out.html',
        }
        for url, template in url_names.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertTemplateUsed(response, template)

    def test_users_names_uses_correct_template(self):
        """При запросе по имени, применяется нужный шаблон"""
        url_names = {
            'users:login': 'users/login.html',
            'users:logout': 'users/logged_out.html',
            'users:signup': 'users/signup.html',
            'users:password_reset_form': 'users/password_reset_form.html',
            'users:password_reset_done': 'users/password_reset_done.html',
            'users:password_reset_complete':
                'users/password_reset_complete.html',
        }
        for url, template in url_names.items():
            with self.subTest(url=url):
                response = self.guest_client.get(reverse(url))
                self.assertTemplateUsed(response, template)
