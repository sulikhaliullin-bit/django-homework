from django.views.generic.list import ListView
from .models import Bb, Rubric, Task

class BbIndexView(ListView):
    model = Bb
    template_name = 'Shop/index.html'
    context_object_name = 'bbs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['user_name'] = 'sulik'
        context['long_text'] = 'Это очень длинный текст, который мы обрежем'
        context['price'] = 1500.50
        context['items_count'] = 5
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'Shop/task_list.html'
    context_object_name = 'tasks'