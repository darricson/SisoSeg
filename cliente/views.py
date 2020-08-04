from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from cliente.forms import ClienteModel
from django.contrib import messages
from .models import Cliente


# function create new client
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


# function list all client  4004 2900
def list_cliente(request):
    clientes = Cliente.objects.all().order_by('-id')

    context = {
        'cliente': clientes
    }
    return render(request, 'cliente/cliente_list.html', context)


# function update client
def update_cliente(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    form = ClienteModel(request.POST or None, instance=clientes)
    if form.is_valid():
        clientes = form.save()
        clientes.save()
        return redirect('cliente_list')
    context = {'form': form}
    return render(request, 'cliente/cliente_update.html', context)


# function delete cliente
def delete_cliente(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        clientes.delete()
        return redirect('cliente_list')
    context = {'cliente': clientes}
    return render(request, 'cliente/delete_cliente.html', context)


# function detail clients
def detail_cliente(request, id):
    clientes = get_object_or_404(Cliente, id=id)
    context = {'cliente': clientes}
    return render(request, 'cliente/detail_cliente.html', context)



