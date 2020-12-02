from django.shortcuts import render
from marchants.models import Marchant
from django.core import serializers
from django.http import JsonResponse
from cart.models import Cart
from products.models import Products
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Orders, OrderItems

# Create your views here.

def createorder(request):
    if request.is_ajax and request.method == 'POST':
        user_id = request.POST.get('customer')
        unpaid = bool(request.POST.get('unpaid'))
        opened= bool(request.POST.get('opened')) 
        total = request.POST.get('total') 
        user = Marchant.objects.get(pk=user_id)
        order = Orders(customer_details=user, unpaid=unpaid, opened=opened, total_cost=total)
        order.save()
        ser_insatnce = serializers.serialize('json', Orders.objects.filter(pk=order.id))
        return JsonResponse({'instance':ser_insatnce}, status=200, safe=False)
    return JsonResponse({'error': 'could not create order' }, status=400)

def orderitem(request):
    if request.is_ajax and request.method == 'POST':
        product_id = request.POST.get('product') 
        qty = request.POST.get('qty')
        price_total = request.POST.get('price_total') 
        order_id = request.POST.get('order_id') 
        order = Orders.objects.get(pk=order_id)
        product = Products.objects.get(pk=product_id)
        order_item = OrderItems(product=product, order_id=order, quantity=qty, total_price=price_total)
        order_item.save()
        ser_insatnce = serializers.serialize('json', OrderItems.objects.filter(order_id=order.id))
        return JsonResponse({'instance':ser_insatnce}, status=200, safe=False)
    return JsonResponse({'error': 'could not create order' }, status=400)

@login_required
def checkout(request):
    order = OrderItems.objects.filter(order_id__customer_details=request.user, order_id__opened=True)
    orde_r = Orders.objects.filter(customer_details=request.user, opened=True)
    return render(request, 'checkout.html', {'orders':order, 'order':orde_r}) 
