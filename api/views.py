from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from customers.models import Cart, Customer
from Transactions.models import Transaction
from marchants.models import Marchant
from orders.models import Orders
from products.models import Products, ProductImages, ProductVariation
from .serializers import CartSerializer, CustomerSerializer, OrderSerializer,  ProductSerializer, ProductImagesSerializer, ProductVariationSerializer, ProductOptionSerializer, TransactionSerializer

# Create your views here.
class StoreCustomersList(APIView):
    def get(self, request, format=None):
        customer_list = Customer.objects.all()
        serializer = CustomerSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerCartView(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = CartSerializer(request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=True):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerCartDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['items', 'id', 'customer']
    def get(self, request, format=None):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Orders(APIView):
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['status', 'id']
     def get(self, request, format=True):
        ordereditems = Orders.objects.all()
        serializer = OrderSerializer(ordereditems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Createorders(APIView):
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrdersDetail(APIView):
    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=True):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StoreProducts(APIView):##ensure to add permission class
     filter_backends = [DjangoFilterBackend]
     filterset_fields = ['id', 'name']
     def get(self, request, format=None):
         get_products = Products.objects.all().order_by('-id')
         serializer = ProductSerializer(get_products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)


class AddProducts(APIView):##ensure to add permission class
     def post(self, request, format=None):
         serializer = ProductSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductImages(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request, pk, format=None):
        images = ProductImages.objects.filter(product=pk)
        serializer = ProductImagesSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductImagesSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductVariation(APIView):
    def get(self, request, pk, format=None):
        variation = ProductVariation.objects.filter(product=pk)
        serializer = ProductVariationSerializer(variation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductVariationSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductOption(APIView):
    def get(self, request, pk, format=None):
        option = ProductOption.objects.filter(product=pk)
        serializer = ProductOptionSerializer(option, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
         serializer = ProductOptionSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class StoreProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        getproduct = self.get_object(pk)
        serializer = ProductSerializer(getproduct)
        return Response(serializer.data) 

    def put(self, request, pk, format=None):
        updateproduct = self.get_object(pk)
        serializer = ProductSerializer(updateproduct, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        delproduct = self.get_object(pk) 
        delproduct.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class SalesView(APIView):
    def get(self, request, format=None):
        wallet = Orders.objects.values('date_created').annotate(daily_sales=Sum('total_cost'))
        serializer = OrderSerializer(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransactionHistory(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['txn_date']
    def get(self, request, format=None):
        trxn = Transaction.objects.all()
        serializer = TransactionSerializer(trxn, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        trxn = Transaction.objects.get(pk=pk)
        trxn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class StoreDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user']

    def get(self, request, format=None):
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StoreUpdate(APIView):
    parser_classes = [MultiPartParser]

    try:
        def get_object(self, pk):
            return Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        raise Http404
    
    def put(self, request, pk, format=None):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'email']
    
    def get(self, request, format=None):
        user = Marchant.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class UserUpdate(APIView):
    try:
        def get_object(self, pk):
            return Marchant.objects.get(pk=pk)
    except Marchant.DoesNotExist:
        raise Http404
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
