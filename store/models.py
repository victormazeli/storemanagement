from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase

# Create your models here.

class Shop(TenantBase):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    tagline = models.CharField(max_length=256, null=True, blank=True)

class Domain(DomainMixin):
    pass