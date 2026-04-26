from django.urls import path
from .views import BbIndexView, TaskListView

urlpatterns = [
    path('', BbIndexView.as_view(), name='index'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
]
