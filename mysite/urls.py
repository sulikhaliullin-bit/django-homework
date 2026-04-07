from django.contrib import admin
from django.urls import path, re_path
from Shop import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', views.hello_world),

    path('data/', views.get_data),

    path('filter/', views.filter_data),

    path('todo/', views.hello_world, name='todo_list'),
    re_path(r'^todo/(?P<task_id>\d+)/$', views.hello_world, name='todo_detail'),
]