from django.shortcuts import render
from .models import Lesson  # Импорт модели Lesson


def lesson_list_manual(request):
    lessons_query = Lesson.objects.all().order_by('id')

    items_per_page = 5
    current_page = int(request.GET.get('page', 1))

    start = (current_page - 1) * items_per_page
    end = start + items_per_page

    page_obj = lessons_query[start:end]

    context = {
        'lessons': page_obj,
        'current_page': current_page,
        'has_next': end < lessons_query.count(),
        'has_prev': current_page > 1,
    }
    # Используем 'Shop/task_list.html', так как он есть в папке Shop
    return render(request, 'Shop/task_list.html', context)