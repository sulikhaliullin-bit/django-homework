from django.db import models

class MyNewModel(models.Model):
    title = models.CharField(max_length=100)  # Заголовок
    content = models.TextField()               # Текст объявления

    def __str__(self):
        return self.title