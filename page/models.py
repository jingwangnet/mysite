from django.db import models
from django.utils import timezone


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    permalink = models.CharField(max_length=20, unique=True)
    text = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
