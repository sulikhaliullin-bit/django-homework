from django.contrib import admin
from .models import MyNewModel  # Импортируем именно MyNewModel

admin.site.register(MyNewModel) # Регистрируем её