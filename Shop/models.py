from django.db import models

class Course(models.Model): # [cite: 23]
    title = models.CharField(max_length=200, verbose_name="Название") # [cite: 26]
    description = models.TextField(verbose_name="Описание") # [cite: 27]
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания") # [cite: 28]

    def __str__(self):
        return self.title

class Lesson(models.Model): # [cite: 29]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons') # [cite: 33]
    title = models.CharField(max_length=200, verbose_name="Название") # [cite: 31]
    content = models.TextField(verbose_name="Текст урока") # [cite: 32]
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок") # [cite: 34]

    def __str__(self):
        return self.title