from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),


    path('lesson_4/', views.show_params, name='lesson_4'),


    path('buy/', views.buy_item, name='buy_item'),
]