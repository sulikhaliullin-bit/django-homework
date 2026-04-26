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
        # Данные для задания №22
        context['test_list'] = ['django', 'python', 'web', 'framework']
        context['current_date'] = timezone.now()
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