from django.shortcuts import render, redirect
from .forms import ProductFormSet

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
    from .models import Product
    products = Product.objects.all()
    return render(request, 'Shop/index.html', {'products': products})