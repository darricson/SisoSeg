from django import forms
from cftv.models import CftvOrcamento, Fabricante


class OrcamentoCftvModel(forms.ModelForm):
    class Meta:
        model = CftvOrcamento
        fields = ['cliente', 'ambiente', 'imagem', 'local', 'descricao']


class FabricanteModel(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome', ]

