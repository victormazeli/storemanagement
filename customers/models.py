from django.db import models
from products.models import Products, ProductVariation

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, null=True, blank=True)
    phone_no = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=124, null=True, blank=True)
    city = models.CharField(max_length=124, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Products)
    item_option = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    total = models.FloatField(default=0.00)
    updated_date = models.DateTimeField(auto_now=True)