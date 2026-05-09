from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('manage/', views.manage_products, name='manage_products'),
]