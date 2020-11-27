from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    tagline = models.CharField(max_length=256, null=True, blank=True)