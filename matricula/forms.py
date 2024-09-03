from django import forms
from .models import Alunos

class AlunoForms(forms.ModelForm):

    class Meta:
        model = Alunos
        fields = '__all__'

        widgtes = {
            'nome':forms.TextInput(attrs={'class': 'form-control'}),
            'curso':forms.TextInput(attrs={'class': 'form-control'}),
            'endereço':forms.TextInput(attrs={'class': 'form-control'}),
        }