from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product, IceCream
from .forms import ProductFormSet, IceCreamForm


class ProductListView(ListView):
    model = Product
    template_name = 'Shop/index.html'
    context_object_name = 'page_obj'
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    template_name = 'Shop/detail.html'
    context_object_name = 'product'


class ProductArchiveView(ArchiveIndexView):
    model = Product
    template_name = 'Shop/archive.html'
    context_object_name = 'products'
    date_field = 'created_at'
    allow_empty = True


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description']
    template_name = 'Shop/product_form.html'
    success_url = reverse_lazy('product_list')


class PrivatePageView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'Shop/private.html'
    context_object_name = 'products'
    login_url = '/accounts/login/'


# manage_products переписан на класс
class ManageProductsView(ListView):
    model = Product
    template_name = 'Shop/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ProductFormSet()
        return context

    def post(self, request, *args, **kwargs):
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('product_list')
        return self.get(request, *args, **kwargs)

    def redirect(self, url):
        from django.shortcuts import redirect
        return redirect(url)


# icecream_create переписан на класс
class IceCreamCreateView(CreateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'Shop/icecream_form.html'
    success_url = reverse_lazy('icecream_list')


# icecream_list переписан на класс
class IceCreamListView(ListView):
    model = IceCream
    template_name = 'Shop/icecream_list.html'
    context_object_name = 'icecreams'