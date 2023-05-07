from django.test import TestCase
from django.urls import resolve
from blog.views import home_page
from django.http import HttpRequest
from functional_tests.const import HOME_TITLE


class HomePageTest(TestCase):
    def test_home_page_mapping(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correctly_content(self):
        request = HttpRequest()
        response = home_page(request)
        content = response.content.decode()
        self.assertIn(HOME_TITLE, content)
