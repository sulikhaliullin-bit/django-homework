from django.urls import path
from . import views

urlpatterns = [
    # путь для главной страницы
    path('', views.index, name='index'),

    # путь для задания №1 (параметры)
    path('lesson_4/', views.show_params, name='lesson_4'),

    # путь для задания №2 (редирект)
    path('buy/', views.buy_item, name='buy_item'),
]