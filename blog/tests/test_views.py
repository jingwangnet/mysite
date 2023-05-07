from django.test import TestCase
from django.urls import resolve
from blog.views import home_page
from django.http import HttpRequest
from functional_tests.const import HOME_TITLE
from django.urls import reverse
from blog.models import Post


class HomePageTest(TestCase):
    def test_home_page_using_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "blog/home.html")

    def create_post(self, title, content):
        Post.objects.create(title=title, content=content)

    def test_display_all_post(self):
        first_title = "The first title"
        first_content = "first content"
        second_title = "The second title"
        second_content = "second content"

        self.create_post(first_title, first_content)
        self.create_post(second_title, second_content)

        response = self.client.get(reverse("home"))
        self.assertContains(response, first_title)
