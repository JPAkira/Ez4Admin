from django.db.models import Q
from django.shortcuts import render, redirect
from apps.estoque.models import Produto


def buscar(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    '''Buscar produtos'''

    lista_produtos = Produto.objects.order_by('nome')

    '''Pega o campo buscar e busca como filtro'''

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_produtos = lista_produtos.filter(nome__icontains=nome_a_buscar)

    '''Cria dicionario com os dados'''

    dados = {
        'produtos': lista_produtos
    }
    return render(request, 'estoque/estoque.html', dados)


