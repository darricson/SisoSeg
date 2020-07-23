from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from cliente.forms import ClienteModel
from django.contrib import messages
from .models import Cliente


def new_cliente(request):
    if str(request.method) == 'POST':
        form = ClienteModel(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'CLiente cadastrado com sucesso')
            form = ClienteModel()
            return redirect('cliente_list')
        else:
            messages.error(request, 'Erro ao cadastrar o cliente')
    else:
        form = ClienteModel()
    context = {'form': form}
    return render(request, 'cliente/new_cliente.html', context)


def list_cliente(request):
    clientes = Cliente.objects.all().order_by('-id')

    context = {
        'cliente': clientes
    }
    return render(request, 'cliente/cliente_list.html', context)
