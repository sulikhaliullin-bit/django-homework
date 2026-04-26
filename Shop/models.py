from django.db import models
from django.core.exceptions import ValidationError

# Эта функция обязательна, так как она прописана в твоих файлах миграций
def validate_even_number(value):
    if value % 2 != 0:
        raise ValidationError('Число должно быть четным')

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, verbose_name='Рубрика')
    # Поля, которые ищет админка и миграции
    count = models.IntegerField(default=0, validators=[validate_even_number], verbose_name='количество')
    status = models.CharField(max_length=10, default='new', verbose_name='статус')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']