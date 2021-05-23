from django.contrib import messages
from django.shortcuts import redirect, render
from apps.vendas.models import Venda, Produto_Venda


def finalizar_venda(request, venda_id):
    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando venda do db '''
    venda = Venda.objects.get(pk=venda_id)

    dados = {
        'venda': venda
    }

    ''' Requests da pagina '''
    if request.method == 'POST':
        modo_de_pagamento = request.POST['modo_de_pagamento']
        valor_pago = request.POST['valor_pago']

        for char in valor_pago:
            if char.isalpha():
                messages.error(request, 'Coloque apenas numeros e a virgula')
                return redirect('/vendas/finalizar_venda/{}'.format(venda_id))

        valor_pago = float(valor_pago.replace(",", "."))

        venda.valor_pago = valor_pago
        venda.forma_de_pagamento = modo_de_pagamento

        if venda.valor_total > venda.valor_pago:
            messages.error(request, 'O valor pago é menor do que o valor total')
            return redirect('/vendas/finalizar_venda/{}'.format(venda_id))

        venda.troco = valor_pago - venda.valor_total
        venda.troco = float("{:.2f}".format(venda.troco))
        venda.save()

        venda = Venda.objects.get(pk=venda_id)

        dados = {
            'venda': venda,
        }

        ''' Pegando a lista de produtos da tabela auxiliar '''
        lista_produtos = Produto_Venda.objects.order_by('venda_id')

        ''' Filtrando os produtos, deixando só os compativeis com o id da venda '''
        lista_produtos = lista_produtos.filter(venda_id=venda_id)

        for produto in lista_produtos:
            produto.produto_id.quantidade = int(produto.produto_id.quantidade)
            produto.produto_id.quantidade -= produto.quantidade
            produto.produto_id.save()

        return render(request, 'vendas/resultado_da_venda.html', dados)

    return render(request, 'vendas/finalizar_venda.html', dados)