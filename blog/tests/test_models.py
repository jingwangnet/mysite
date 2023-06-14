from django.test import TestCase
from django.core.exceptions import ValidationError
from blog.models import Post, Tag
from django.urls import reverse


class PostModelTest(TestCase):
    def test_post_creation_and_retrieve(self):
        post = Post()
        post.title = "The first post"
        post.content = "content"
        post.save()

        self.assertEqual(1, Post.objects.count())
        saved_post = Post.objects.first()

        self.assertEqual(saved_post.title, "The first post")
        self.assertEqual(saved_post.content, "content")
        self.assertTrue(saved_post.publish)

    def test_str(self):
        post = Post.objects.create(title="The first post", content="content")
        self.assertEqual(str(post), "The first post")

    def test_odering(self):
        post1 = Post.objects.create(title="The first post", content="content")
        post2 = Post.objects.create(title="The first post", content="content")
        post3 = Post.objects.create(title="The first post", content="content")
        self.assertEqual([p.id for p in Post.objects.all()], [3, 2, 1])

    def test_get_absolute_url(self):
        post1 = Post.objects.create(title="The first post", content="content")
        self.assertEqual(post1.get_absolute_url(), "/1/")


class TagModelTest(TestCase):
    def test_tag_creation_and_retrieve(self):
        tag = Tag()
        tag.tag = "tag"
        tag.save()

        self.assertEqual(tag.tag, "tag")

    def test_tag_cant_be_able_as_empty(self):
        tag = Tag()
        tag.tag = ""
        with self.assertRaises(ValidationError):
            tag.full_clean()

    def test_tag_display(self):
        tag = Tag.objects.create(tag="tag")
        self.assertEqual(str(tag), "tag")
