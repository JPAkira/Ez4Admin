from django.contrib import messages
from django.shortcuts import redirect
from apps.estoque.models import Produto
from apps.vendas.models import Venda, Produto_Venda

def salvar_produto(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    '''requests da pagina'''
    venda_id = request.POST['venda_id']
    codigo = request.POST['codigo']
    quantidade = request.POST['quantidade']

    ''' Procurando o produto, caso não existe retorna erro'''
    try:
        produto = Produto.objects.get(pk=codigo)
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado')
        return redirect('adicionar_produto/{}'.format(venda_id))

    ''' Procurando venda '''
    try:
        venda = Venda.objects.get(pk=venda_id)
    except Venda.DoesNotExist:
        messages.error(request, 'Essa venda não existe ou foi apagada')
        return redirect('vendas')

    ''' Calculando o total (quantidade * preço unitario)'''
    total = float(produto.preco.replace(",", ".")) * int(quantidade)

    ''' Retornando um dado melhor formatado, apenas 2 digitos além da virgula '''
    total = float("{:.2f}".format(total))

    ''' Resgatando os valores da venda e transformando em seu respectivo tipo de dado '''
    valor_total = float(venda.valor_total)
    volume_de_compra = int(venda.volume_de_compra)

    ''' Somando o valor da venda com o produto recém adicionado '''
    venda.valor_total = valor_total + total
    venda.volume_de_compra = volume_de_compra + int(quantidade)

    ''' Salvando os novos dados '''
    venda.save()

    ''' Criando a venda do produto na tabela auxiliar '''
    venda_produto = Produto_Venda.objects.create(venda_id=venda, produto_id=produto, quantidade=quantidade,
                                                 total=total)
    venda_produto.save()
    return redirect('adicionar_produto', venda_id)