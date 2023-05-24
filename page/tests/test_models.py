from django.test import TestCase
from ..models import Page


class TestPageModels(TestCase):
    def test_Page_model_creation_and_reatrieve(self):
        page = Page()
        page.title = "about me"
        page.permalink = "/about/"
        page.text = "content"
        page.save()

        self.assertEqual(1, Page.objects.count())
        saved_page = Page.objects.first()
        self.assertEqual(saved_page.title, "about me")
        self.assertEqual(saved_page.permalink, "/about/")
        self.assertEqual(saved_page.text, "content")
