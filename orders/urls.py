from django.urls import path, include
from orders import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.createorder, name='create-order'),
    path('checkout', views.checkout, name='checkout'),
    
  

] 
