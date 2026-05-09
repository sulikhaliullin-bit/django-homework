from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductArchiveView,
    ProductCreateView, PrivatePageView, ManageProductsView,
    IceCreamCreateView, IceCreamListView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('archive/', ProductArchiveView.as_view(), name='product_archive'),
    path('manage/', ManageProductsView.as_view(), name='manage_products'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('private/', PrivatePageView.as_view(), name='private_page'),
    path('icecream/', IceCreamListView.as_view(), name='icecream_list'),
    path('icecream/create/', IceCreamCreateView.as_view(), name='icecream_create'),
]