from django.db import models

# Create your models here.


class Transaction(models.Model):
    currency = models.CharField(max_length= 10)
    amount = models.FloatField(blank=True, null=True, default=0.00)
    status = models.CharField(max_length= 10)
    txn_date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length= 256)
    cutomer_id = models.CharField(max_length= 256)
    cutomer_f_name = models.CharField(max_length= 256)
    cutomer_l_name = models.CharField(max_length= 256)
    customer_email = models.EmailField()

    class Meta:
        ordering = ['txn_date']