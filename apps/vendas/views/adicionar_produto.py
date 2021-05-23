from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from apps.clientes.models import Cliente
from apps.vendas.models import Venda, Produto_Venda

def adicionar_produto(request, venda_id):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando a lista de produtos da tabela auxiliar '''
    lista_produtos = Produto_Venda.objects.order_by('venda_id')

    ''' Filtrando os produtos, deixando só os compativeis com o id da venda '''
    lista_produtos = lista_produtos.filter(venda_id=venda_id)

    ''' Pegando venda do db '''
    try:
        venda = Venda.objects.get(pk=venda_id)
    except Venda.DoesNotExist:
        messages.error(request, 'Essa venda não existe ou foi apagada')
        return redirect('vendas')

    ''' Pegando o cliente do banco de dados pela primary key '''
    cliente = get_object_or_404(Cliente, pk=venda.cliente.pk)

    ''' Fazendo um dicionario com os dados '''
    dados = {
        'produtos': lista_produtos,
        'cliente': cliente,
        'venda': venda
    }

    return render(request, 'vendas/adicionar_produto.html', dados)