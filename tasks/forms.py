from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Task


class createTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the task description'}),
            'important': CheckboxInput(attrs={'class': 'form-check-input m-auto', 'placeholder': 'Is it important?'})
        }
