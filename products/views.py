from django.shortcuts import render
from .models import Products, ProductImages, ProductOption, ProductVariation

# Create your views here.

def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    # product_variation = ProductVariation.objects.all()
    # variation = product.variation.all()
    thumb_images = ProductImages.objects.filter(product_id=product.id)
    return render(request, 'detail.html', {'product':product,  'image':thumb_images})

def collection(request):
    product = Products.objects.all()
    return render(request, 'collection.html', {'product_list':product} )