from django.db import models

# Заглушка для старой миграции, чтобы не было ошибки
def validate_even_number(value):
    pass

class Task(models.Model):
    # Варианты для списка (choices)
    CATEGORY_CHOICES = [
        ('work', 'Работа'),
        ('home', 'Дом'),
        ('study', 'Учеба'),
    ]

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", blank=True)
    # Поле со списком
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='work',
        verbose_name="Категория"
    )

    def __str__(self):
        return self.title