from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products, ProductVariation, ProductOption
# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    updated_date = models.DateTimeField(auto_now=True)