from django.urls import path, include
from cart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.cart_view, name='cart'),
    path('add/', views.addtocart, name='addtocart'),
  

] 
