from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from apps.vendas.models import Venda, Produto_Venda


def deleta_venda(request, venda_id):

    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o usuario do banco de dados pela primary key '''

    venda = get_object_or_404(Venda, pk=venda_id)

    ''' Pegando a lista de produtos da tabela auxiliar '''
    lista_produtos = Produto_Venda.objects.order_by('venda_id')

    ''' Filtrando os produtos, deixando só os compativeis com o id da venda '''
    lista_produtos = lista_produtos.filter(venda_id=venda_id)

    ''' Deletando os itens da venda do banco de dados '''
    lista_produtos.delete()

    ''' Deletando a venda do banco de dados '''
    venda.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('vendas')