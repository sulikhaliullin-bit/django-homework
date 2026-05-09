from django.urls import path
from .views import ProductListView, ProductDetailView, ProductArchiveView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('archive/', ProductArchiveView.as_view(), name='product_archive'),
    path('manage/', views.manage_products, name='manage_products'),
]