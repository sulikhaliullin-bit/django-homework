from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200) # Заголовок поста
    text = models.TextField()                # Текст поста

    def __str__(self):
        return self.title