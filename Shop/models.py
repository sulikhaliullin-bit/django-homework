from django.db import models

# ДОБАВЬ ЭТОТ БЛОК:
def validate_even_number(value):
    pass

# Твоя модель задач:
class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title