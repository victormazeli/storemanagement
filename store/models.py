from django.db import models
from django.contrib.auth import get_user_model
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.

class Shop(TenantMixin):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    tagline = models.CharField(max_length=256, null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Domain(DomainMixin):
    pass