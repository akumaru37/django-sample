from django.test import TestCase, Client
from django.urls import reverse, resolve
from src.app import app_views


class AppViewsTest(TestCase):
    def test_input(self):
        self.client = Client()
        self.url = reverse('input')

        self.client.force_login()

        self.assertEqual(resolve(self.url).func, app_views.input)

        print(reverse('input'))
        response = self.client.get(reverse('input'))
        self.assertEqual(response.status_code, 200)
