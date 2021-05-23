from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from apps.estoque.models import Produto

def editar_produto(request, produto_codigo):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o produto do banco de dados pela primary key '''

    produto = get_object_or_404(Produto, pk=produto_codigo)

    ''' Criando um dicionario com os dados '''

    produto_a_editar = {'produto': produto}

    return render(request, 'estoque/edita_produto.html', produto_a_editar)

def editar_produto_com_codigo(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nome = request.POST['nome']
        embalagem = request.POST['embalagem']
        tamanho = request.POST['tamanho']
        quantidade = request.POST['quantidade']
        preco = request.POST['preco']

        p = get_object_or_404(Produto, pk=codigo)

        p.nome = nome
        p.embalagem = embalagem
        p.tamanho = tamanho
        p.quantidade = quantidade
        p.preco = preco

        p.save()
    return redirect('estoque')