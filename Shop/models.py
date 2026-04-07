from django.db import models
from django.core.exceptions import ValidationError


def validate_even_number(value):
    if value % 2 != 0:
        raise ValidationError('число должно быть четным')

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='товар')
    content = models.TextField(null=True, blank=True, verbose_name='описание')
    price = models.FloatField(null=True, blank=True, verbose_name='цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='опубликовано')
    count = models.IntegerField(default=0, validators=[validate_even_number], verbose_name='количество')

    class Meta:
        verbose_name_plural = 'объявления'
        verbose_name = 'объявление'
        ordering = ['-published']