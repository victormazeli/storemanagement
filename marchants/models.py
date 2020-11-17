from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.

class Marchant(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    subaccount = models.CharField(max_length=256, null=True, blank=True)
    bankname = models.CharField(max_length=256, null=True, blank=True)
    bankaccount_no = models.IntegerField(null=True, blank=True)
    bankcode = models.IntegerField(null=True, blank=True)
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Shop(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    tagline = models.CharField(max_length=256, null=True, blank=True)