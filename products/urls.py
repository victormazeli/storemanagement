from django.urls import path, include
from products import views


urlpatterns = [

    path('<int:pk>', views.product_detail, name='detail'),
    path('', views.collection, name='collection'),
  

] 




 