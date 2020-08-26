from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtext = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(auto_now=True)