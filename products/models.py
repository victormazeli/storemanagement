from django.db import models
from django_resized import ResizedImageField

# Create your models here.

#ensure to add a price formatted field
class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    # discounted_price = models.FloatField(default=0.00)
    quantity_in_stock = models.IntegerField(default=0)
    # unit = models.CharField(max_length=20)
    sales = models.IntegerField(default=0) 
    extra_detail = models.CharField(max_length=255, blank=True, null=True)
    image = ResizedImageField(size=[312, 312], upload_to='product_images', force_format='JPEG', quality=75)
    in_stock = models.BooleanField(default=False)
    slug  = models.SlugField()
    # variation = models.ManyToManyField('ProductVariation', related_name='product_variations')


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = ResizedImageField(size=[312, 312], upload_to='product_images', force_format='JPEG',  quality=75)
    


class ProductOption(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)


class ProductVariation(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, blank=True, null=True)
    # price = models.FloatField(default=0.00)
    # quantity = models.IntegerField(default=0)