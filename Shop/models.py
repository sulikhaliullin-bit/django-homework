from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


# Валидатор — только положительные числа включая 0
def validate_positive(value):
    if value < 0:
        raise ValidationError(f'{value} должно быть положительным числом или 0')


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    # Метод возвращает id + name
    def get_id_and_name(self):
        return f'{self.id} - {self.name}'

    # Метод возвращает сумму price всех продуктов
    @classmethod
    def get_total_price(cls):
        return sum(p.price for p in cls.objects.all())


class IceCream(models.Model):
    name = models.CharField(max_length=200)
    flavor = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])

    def __str__(self):
        return self.name

    # Метод возвращает id + flavor
    def get_id_and_flavor(self):
        return f'{self.id} - {self.flavor}'

    # Метод возвращает сумму price всех мороженых
    @classmethod
    def get_total_price(cls):
        return sum(i.price for i in cls.objects.all())