from django import forms
from .models import TodoBoard


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoBoard
        fields = ('task','status')