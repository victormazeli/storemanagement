from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Cart
from marchants.models import Marchant
from products.models import Products
import json
# Create your views here.

def cart_view(request):
    return render(request, 'cart.html')

# Cart.objects.select_related('customer').filter(customer=request.user)

def addtocart(request):
    if request.is_ajax and request.method == 'POST':
        user_id = int(float(request.POST.get('customer')))
        item_id = int(float(request.POST.get('items')))
        qty = int(float(request.POST.get('qty')))
        total = int(float(request.POST.get('total')))
        user = Marchant.objects.get(pk=user_id)
        product = Products.objects.get(pk=item_id)
        cart = Cart(customer=user, items=product, qty=qty, total=total)
        cart.save()
        ser_insatnce = serializers.serialize('json', Cart.objects.filter(pk=cart.id))
        return JsonResponse({'instance':ser_insatnce}, status=200, safe=False)
    return JsonResponse({'error': 'could not add item to cart' }, status=400)


def getcart(request):
    if request.is_ajax and request.method == 'GET':
        cart = Cart.objects.all()
        ser_insatnce = serializers.serialize('json', cart)
        return JsonResponse({'instance':ser_insatnce}, status=200, safe=False)
    return JsonResponse({'error': 'could not get cart' }, status=400)