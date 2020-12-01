from django.apps import AppConfig
from orders.models import Orders
from orders.signals import pre_save_create_order_id

class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        pre_save.connect(pre_save_create_order_id, sender=Orders)
