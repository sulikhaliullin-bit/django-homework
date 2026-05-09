from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value < 0:
        raise ValidationError(f'{value} должно быть положительным числом или 0')


class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class IceCream(models.Model):
    kiosk = models.ForeignKey(IceCreamKiosk, on_delete=models.CASCADE, related_name='icecreams', null=True, blank=True)
    name = models.CharField(max_length=200)
    flavor = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_id_and_name(self):
        return f'{self.id} - {self.name}'

    @classmethod
    def get_total_price(cls):
        return sum(p.price for p in cls.objects.all())