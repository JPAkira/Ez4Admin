from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from apps.estoque.models import Produto

def deletar_produto(request, produto_codigo):
    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o usuario do banco de dados pela primary key '''

    produto = get_object_or_404(Produto, pk=produto_codigo)

    ''' Deletando o cliente do banco de dados '''

    produto.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('estoque')
