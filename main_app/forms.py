from django import forms
from .models import Characters

class CharactersForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ['name', 'gender']
        widgets = {
            'name': forms.TextInput(
            attrs={
                'placeholder': 'Enter character name',
                'type': 'text',
            }
            ),
        }
