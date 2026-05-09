from django.forms import modelformset_factory
from .models import Product

ProductFormSet = modelformset_factory(
    Product,
    fields=('name', 'price', 'description'),
    extra=2,
    can_delete=True
)