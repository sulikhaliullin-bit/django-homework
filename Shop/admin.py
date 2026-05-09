from django.contrib import admin
from .models import Product, IceCream, IceCreamKiosk, Parent, Child

admin.site.register(Product)
admin.site.register(IceCream)
admin.site.register(IceCreamKiosk)
admin.site.register(Parent)
admin.site.register(Child)