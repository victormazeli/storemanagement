from rest_framework import serializers
from cart.models import Cart
from orders.models import Orders, OrderItems
from products.models import Products, ProductImages, ProductVariation, ProductOption
from Transactions.models import Transaction
from marchants.models import Marchant
from store.models import Shop



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


# class DomainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Domain
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = Marchant
      fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = '__all__'

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = '__all__'

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#       model = Customer
#       fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
      model = Cart
      fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItems
        fields = ['order_id', 'product', 'quantity', 'total_price']