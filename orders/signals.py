from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Orders
from .utiity import unique_order_id_generator



def pre_save_create_order_id(sender, instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id = unique_order_id_generator(instance)

