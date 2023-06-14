from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.pk])

    class Meta:
        ordering = ("-publish",)
