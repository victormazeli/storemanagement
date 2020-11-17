from django.db import models
from customers.models import Customer, Cart

# Create your models here.

class Orders(models.Model):
    order_id = models.CharField(max_length=126, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    unpaid = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    cancelled = models.IntegerField(default=0)
    opened = models.IntegerField(default=0)
    shipping_cost = models.FloatField(default=0.00)
    total_cost = models.FloatField(default=0.00)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']