from django.shortcuts import render, redirect, get_object_or_404
from .models import CftvOrcamento, Cabo, Equipamentocftv, Fabricante
from .forms import OrcamentoCftvModel, FabricanteModel
from django.contrib import messages


def list_orcamento(request):
    orcamento = CftvOrcamento.objects.all().order_by('-id')
    context = {'orcamentos': orcamento}
    return render(request, 'cftv/orcamento_list.html', context)


def new_orcamento_cftv(request):
    if str(request.method) == 'POST':
        form = OrcamentoCftvModel(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item cadastrado com sucesso!')
            return redirect('orcamento_cftv')
        else:
            messages.error(request, 'Erro ao adicionar o item')

    else:
        form = OrcamentoCftvModel()
    context = {'form': form}
    return render(request, 'cftv/new_orcamento_cftv.html', context)


def update_orcamento(request, id):
    orcamento = get_object_or_404(CftvOrcamento, id=id)
    form = OrcamentoCftvModel(request.POST or None, instance=orcamento)
    if form.is_valid():
        orcamento = form.save()
        orcamento.save()
        return redirect('orcamento_cftv')
    context = {'form': form}
    return render(request, 'cftv/update_orcamento_cftv.html', context)


def delete_orcamento(request, id):
    orcamento = get_object_or_404(CftvOrcamento, id=id)
    if request.method == 'POST':
        orcamento.delete()
        return redirect('orcamento_cftv')
    context = {'orcamento': orcamento}
    return render(request, 'cftv/delete_orcamento_cftv.html', context)


def detail_orcamento(request, id):
    orcamento = get_object_or_404(CftvOrcamento, id=id)
    context = {'orcamento': orcamento}
    return render(request, 'cftv/detail_orcamento_cftv.html', context)



def new_fabricante(request):
    if str(request.method) == 'POST':
        form = FabricanteModel(request.POST, request.files, None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fabricante cadastrado com sucesso')
            return redirect('list_fabricante')
        else:
            messages.error(request, 'Erro ao cadastrar Fabricante')
        context = {'form': form}
        return render(request, 'cftv/new_fabricante')