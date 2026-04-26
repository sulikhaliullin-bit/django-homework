from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bb, Rubric, Task
from .forms import BbForm

class BbIndexView(ListView):
    model = Bb
    template_name = 'Shop/index.html'
    context_object_name = 'bbs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        # Твои данные для фильтров
        context['user_name'] = 'Sulik'
        context['long_text'] = 'Это очень длинный текст, который мы обрежем'
        context['price'] = 1500.50
        context['items_count'] = 5
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'Shop/task_list.html'
    context_object_name = 'tasks'

class BbCreateView(CreateView):
    template_name = 'Shop/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context