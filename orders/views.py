from django.shortcuts import render
from marchants.models import Marchant
from django.core import serializers
from django.http import JsonResponse
from cart.models import Cart
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Orders

# Create your views here.

def createorder(request):
    if request.is_ajax and request.method == 'POST':
        cart_id = request.POST.get('cart') 
        user_id = request.POST.get('customer_detail')
        unpaid = bool(request.POST.get('unpaid'))
        opened= bool(request.POST.get('opened')) 
        total = int(float(request.POST.get('total')))
        user = Marchant.objects.get(pk=user_id)
        cart = Cart.objects.get(pk=cart_id)
        order = Orders(cart=cart, customer_details=user, unpaid=unpaid, opened=opened, total_cost=total)
        order.save()
        ser_insatnce = serializers.serialize('json', Orders.objects.filter(pk=order.id))
        return JsonResponse({'instance':ser_insatnce}, status=200, safe=False)
    return JsonResponse({'error': 'could not add item to cart' }, status=400)

@login_required
def checkout(request):
    order = Orders.objects.select_related('cart', 'customer_details').filter(customer_details=request.user)
    return render(request, 'checkout.html', {'orders':order})
