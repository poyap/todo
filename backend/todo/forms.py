from django import forms
from .models import Todo


class CreateUpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title',  'description', 'dead_line',]
        widgets = {
            'dead_line': forms.widgets.DateInput(attrs={'type':'date'}),
        }

