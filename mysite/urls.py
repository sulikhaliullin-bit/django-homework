from django.contrib import admin
from django.urls import path, include # Проверьте наличие include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('Shop.urls')), # Убедитесь, что здесь 'Shop.urls'
]