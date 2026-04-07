from django.urls import path
from . import views

urlpatterns = [
    path('lesson_4/', views.show_params, name='lesson_4'),
]