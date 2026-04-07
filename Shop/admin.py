from django.contrib import admin
from .models import Bb

class BbAdmin(admin.ModelAdmin):
    # Оставляем только те поля, которые точно есть в твоей модели Bb
    list_display = ('title', 'content', 'price')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)