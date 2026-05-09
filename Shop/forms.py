from django import forms
from django.forms import modelformset_factory
from .models import Product, IceCream



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


# Форма для Мороженого
class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price']


ProductFormSet = modelformset_factory(
    Product,
    fields=('name', 'price'),  #
    extra=2,
    can_delete=True
)