from django import forms
from Shop.models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'content', 'course', 'order')
        labels = {
            'title': 'Название урока',
            'content': 'Содержание',
            'course': 'Курс',
            'order': 'Порядок',
        }