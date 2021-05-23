from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from apps.vendas.models import Produto_Venda, Venda

def deletar_produto_venda(request, produto_id):
    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o usuario do banco de dados pela primary key '''

    produto = get_object_or_404(Produto_Venda, pk=produto_id)
    venda = get_object_or_404(Venda, pk=produto.venda_id.id)

    valor_total_dos_produtos = float(produto.produto_id.preco.replace(",", ".")) * int(produto.quantidade)

    venda.valor_total -= valor_total_dos_produtos
    venda.volume_de_compra -= int(produto.quantidade)

    venda.save()

    ''' Deletando o cliente do banco de dados '''

    produto.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('/vendas/adicionar_produto/{}'.format(produto.venda_id.id))