from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductFormSet


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


def manage_products(request):
    if request.method == 'POST':
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('product_list')
    else:
        formset = ProductFormSet()
    return render(request, 'Shop/create.html', {'formset': formset})