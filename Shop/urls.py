# Shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('manual-list/', views.lesson_list_manual, name='manual_list'),
]