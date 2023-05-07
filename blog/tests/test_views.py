from django.test import TestCase
from django.urls import resolve
from blog.views import home_page
from django.http import HttpRequest
from functional_tests.const import HOME_TITLE


class HomePageTest(TestCase):
    def test_home_page_using_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "blog/home.html")
