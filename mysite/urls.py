from django.contrib import admin
from django.urls import path, include
from Shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('data/', views.get_data),
]