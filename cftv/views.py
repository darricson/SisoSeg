from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CftvOrcamento, Cabo, Equipamentocftv, Fabricante


class OrcamentocftvList(ListView):
    model = CftvOrcamento
    context_object_name = 'orcamentos'
    template_name = 'cftv/orcamento_list.html'


#class OrcamentoDetail
