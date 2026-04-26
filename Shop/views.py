from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView
from django.utils import timezone
from .models import Bb, Rubric
from .forms import BbForm


class BbIndexView(ListView):
    model = Bb
    template_name = 'Shop/index.html'
    context_object_name = 'bbs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()

        context['test_list'] = ['django', 'python', 'web', 'framework']
        context['current_date'] = timezone.now()


        context['user_name'] = 'sulik'
        context['long_text'] = 'Это очень длинный текст, который мы обрежем с помощью фильтра truncatewords.'
        context['price'] = 1500.50
        context['items_count'] = 5

        return context

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class MyRedirectView(RedirectView):
    url = '/'