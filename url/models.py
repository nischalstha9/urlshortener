from django.db import models

# Create your models here.
class urls(models.Model):
    nlong = models.URLField(max_length=400, unique=True)
    short = models.CharField(max_length=100, unique=True)
