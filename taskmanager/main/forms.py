from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "event_date_time"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "event_date_time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату добавления заметки'
            }),
        }
