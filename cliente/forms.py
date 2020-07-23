from django import forms
from .models import Cliente


class ClienteModel(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'rua',
                  'numero', 'bairro', 'cidade', 'ponto_referencia']
    