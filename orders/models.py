from django.db import models
from cart.models import Cart
from products.models import Products
from django.contrib.auth import get_user_model

# Create your models here.

class Orders(models.Model):
    order_id = models.CharField(max_length=126, blank=True)
    customer_details = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    unpaid = models.BooleanField(default=0)
    paid = models.BooleanField(default=0)
    cancelled = models.BooleanField(default=0)
    opened = models.BooleanField(default=0)
    shipping_cost = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)