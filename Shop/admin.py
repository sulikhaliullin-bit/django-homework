from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    # Укажи только те поля, которые ТОЧНО есть в моделях выше
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'status')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)