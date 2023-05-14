from django.test import TestCase
from django.urls import resolve
from blog.views import home_page, post_detail
from django.http import HttpRequest
from functional_tests.const import HOME_TITLE
from django.urls import reverse
from blog.models import Post


first_title = "The first title"
first_content = "first content"
second_title = "The second title"
second_content = "second content"


class HomePageTest(TestCase):
    def test_home_page_using_template(self):
        response = self.client.get(reverse("blog:home"))
        self.assertTemplateUsed(response, "blog/home.html")

    def create_post(self, title, content):
        Post.objects.create(title=title, content=content)

    def test_display_all_post(self):
        self.create_post(first_title, first_content)
        self.create_post(second_title, second_content)

        response = self.client.get(reverse("blog:home"))
        self.assertContains(response, first_title)


class PostDetailTest(TestCase):
    def setUp(self):
        Post.objects.create(title=first_title, content=first_content)

    def test_post_detail_page_using_template(self):
        post = Post.objects.first()
        response = self.client.get(reverse("blog:detail", args=[post.pk]))
        self.assertTemplateUsed(response, "blog/detail.html")

    def test_post_detail_pass_post(self):
        post = Post.objects.first()
        response = self.client.get(reverse("blog:detail", args=[post.pk]))
        pass_post = response.context["post"]
        self.assertEqual(pass_post, post)
