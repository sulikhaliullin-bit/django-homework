from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ProductFormSet
from .models import Product


def manage_products(request):
    if request.method == 'POST':
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('product_list')
    else:
        formset = ProductFormSet()

    return render(request, 'Shop/create.html', {'formset': formset})


def product_list(request):
    products = Product.objects.all()

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Shop/index.html', {'page_obj': page_obj})