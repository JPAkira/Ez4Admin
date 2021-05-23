from django.shortcuts import render, redirect
from apps.estoque.models import Produto

def estoque(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Resgatando todos os clientes do banco de dados '''
    produtos = Produto.objects.order_by('nome')

    print(type(produtos))

    ''' Criando um dicionario com os dados '''
    dados = {
        'produtos': produtos
    }

    return render(request, 'estoque/estoque.html', dados)