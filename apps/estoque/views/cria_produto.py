from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from apps.estoque.models import Produto


def cria_produto(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Requests da pagina '''
    if request.method == 'POST':
        codigo = request.POST['codigo']

        ''' Verificando se o produto existe no banco de dados '''
        exist = Produto.objects.filter(codigo=codigo).count()

        ''' Se o produto não existir no banco de dados, é redirecionado para area de criação '''
        if exist == 0:
            codigo = {'codigo': codigo}
            return render(request, 'estoque/cria_produto_com_codigo.html', codigo)
        else:
            produto = get_object_or_404(Produto, pk=codigo)
            dados = {'produto': produto}
            return render(request, 'estoque/adicionar_estoque_com_codigo.html', dados)

    else:
        return render(request, 'estoque/cria_produto.html')


def cria_produto_com_codigo(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Requests da pagina '''
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nome = request.POST['nome']
        embalagem = request.POST['embalagem']
        tamanho = request.POST['tamanho']
        quantidade = request.POST['quantidade']
        preco = request.POST['preco']

        ''' Criando produto '''
        produto = Produto.objects.create(codigo=codigo, nome=nome, embalagem=embalagem,
                                         tamanho=tamanho, quantidade=quantidade,
                                         preco=preco)

        ''' Salvando o produto no banco de dados '''
        produto.save()
        messages.success(request, 'Produto criado com sucesso')
        return redirect('estoque')