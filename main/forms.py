from .models import Task
from django.forms import ModelForm,TextInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","task"]
        widgets={
            "task":TextInput(attrs={
                'class':'form-control',
                'placeholder':"Введите название"
        }),
            "title": Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : "Введите описание"
        })
        }