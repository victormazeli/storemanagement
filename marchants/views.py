from django.shortcuts import render
from products.models import Products, ProductImages
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def index(request):
    product = ProductImages.objects.select_related('product')
    return render(request, 'index.html', {'product_list':product} )


def products(request):
    if request.is_ajax and request.method == 'GET':
        ser_instance = serializers.serialize('json', Products.objects.all())
        return JsonResponse(ser_instance, status=200, safe=False)
    return JsonResponse({'error': 'could not fetch products'}, status=400)


