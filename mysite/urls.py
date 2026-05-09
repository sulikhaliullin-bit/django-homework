from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('Shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # встроенные urls авторизации
    path('', lambda request: redirect('icecream_list')),
]