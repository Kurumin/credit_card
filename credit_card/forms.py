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

    monthly_income = forms.CharField(label='Renda Mensal', widget=forms.TextInput(attrs={
        'placeholder': 'Renda Mensal',
        'class': 'form-control',
        'autocomplete': 'off',
        'onkeypress': '$(this).mask("000000000.09",{reverse: true})',
    }))
