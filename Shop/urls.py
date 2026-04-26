from django.urls import path
from .views import BbIndexView, BbCreateView # Импортируем классы

urlpatterns = [
    path('', BbIndexView.as_view(), name='index'), # Обязательно .as_view()
    path('add/', BbCreateView.as_view(), name='add'),
]