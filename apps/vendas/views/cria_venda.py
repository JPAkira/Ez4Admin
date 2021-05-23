from django.shortcuts import render, redirect, get_object_or_404
from apps.clientes.models import Cliente


def selecionar_cliente(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Resgatando todos os clientes do banco de dados '''
    clientes = Cliente.objects.order_by('nome')

    ''' Criando um dicionario com os dados '''
    dados = {
        'clientes': clientes
    }
    return render(request, 'vendas/selecionar_cliente.html', dados)


def cria_venda(request, cliente_id):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o cliente do banco de dados pela primary key '''
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    ''' Criando um dicionario com os dados '''
    cliente = {'cliente': cliente}

    return render(request, 'vendas/cria_venda.html', cliente)

