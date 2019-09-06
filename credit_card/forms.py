from .models import Client
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['current_score']

    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={
        'placeholder': 'Nome',
        'aria-describedby': 'nome',
        'autocomplete': 'off'
    }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'aria-describedby': 'nome',
        'autocomplete': 'off'
    }))

    cpf = forms.EmailField(label='CPF', widget=forms.TextInput(attrs={
        'placeholder': 'CPF',
        'autocomplete': 'off',
        'onkeypress': '$(this).mask("000.000.000-09")',
    }))

    monthly_income = forms.CharField(label='Renda Mensal', widget=forms.TextInput(attrs={
        'placeholder': 'Renda Mensal',
        'class': 'form-control',
        'autocomplete': 'off',
        'onkeypress': '$(this).mask("000000000,09")',
    }))
