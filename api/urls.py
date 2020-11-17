from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('customers/list/', views.StoreCustomersList.as_view()),
    path('cart/list/', views.CustomerCartDetail.as_view()),
    path('cart/update/<int:pk>/', views.CustomerCartView.as_view()),
    path('cart/add/', views.CustomerCartView.as_view()),
    path('cart/delete/<int:pk>/', views.CustomerCartView.as_view()),
    path('list/order/', views.Orders.as_view()),
    path('details/order/<int:pk>/', views.OrdersDetail.as_view()),
    path('delete/order/<int:pk>/', views.OrdersDetail.as_view()),
    path('create/order/', views.Createorders.as_view()),
    path('add_product/', views.AddProducts.as_view()),
    path('get_products/', views.StoreProducts.as_view()),
    path('product_detail/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_update/<int:pk>/', views.StoreProductDetail.as_view()),
    path('product_delete/<int:pk>/', views.StoreProductDetail.as_view()),
    path('get_images/<int:pk>/', views.ProductImages.as_view()),
    path('add_images/', views.ProductImages.as_view()),
    path('add_variation/', views.ProductVariation.as_view()),
    path('get_variation/<int:pk>/', views.ProductVariation.as_view()),
    path('add_options/', views.ProductOption.as_view()),
    path('get_options/<int:pk>/', views.ProductOption.as_view()),
    path('sales/', views.SalesView.as_view()),
    path('get_transactions/', views.TransactionHistory.as_view()),
    path('delete_transactions/<int:pk>/', views.TransactionHistory.as_view()),
    path('get_store/', views.StoreDetail.as_view()),
    path('update_store/', views.StoreUpdate.as_view()),
    path('user_update/', views.UserUpdate.as_view()),
    path('user_detail/', views.UserDetail.as_view()),

  

]

urlpatterns = format_suffix_patterns(urlpatterns)