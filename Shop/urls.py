from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductArchiveView,
    ProductCreateView, PrivatePageView, ManageProductsView,
    IceCreamCreateView, IceCreamListView
)

# Маршруты объединены по префиксу icecream/ и product/
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/manage/', ManageProductsView.as_view(), name='manage_products'),
    path('product/archive/', ProductArchiveView.as_view(), name='product_archive'),
    path('private/', PrivatePageView.as_view(), name='private_page'),
    path('icecream/', IceCreamListView.as_view(), name='icecream_list'),
    path('icecream/create/', IceCreamCreateView.as_view(), name='icecream_create'),
]