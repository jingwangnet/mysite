from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField(max_length=20, unique=True)
    text = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("pages", args=[self.url])

    def __str__(self):
        return self.title
