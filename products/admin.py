from django.contrib import admin
from .models import Products, ProductOption, ProductVariation, ProductImages

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductOption)
admin.site.register(ProductVariation) 
admin.site.register(ProductImages) 
