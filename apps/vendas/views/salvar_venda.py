from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from apps.clientes.models import Cliente
from apps.estoque.models import Produto
from apps.vendas.models import Venda, Produto_Venda

def salvar_venda(request, cliente_id):
    ''' Verificando se está postando dados ou se apenas está renderizando '''
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        codigo = request.POST['codigo']
        quantidade = request.POST['quantidade']

        ''' Procurando o produto, caso não existe retorna erro'''
        try:
            produto = Produto.objects.get(pk=codigo)
        except Produto.DoesNotExist:
            messages.error(request, 'Produto não encontrado')
            return redirect('/vendas/cria_venda/{}'.format(cliente_id))

        ''' Calculando o total (quantidade * preço unitario)'''
        total = float(produto.preco.replace(",", ".")) * int(quantidade)

        ''' Retornando um dado melhor formatado, apenas 2 digitos além da virgula '''
        total = float("{:.2f}".format(total))

        ''' Criando usuario e salvando'''
        venda = Venda.objects.create(cliente=cliente, volume_de_compra=quantidade, valor_total=total)
        venda.save()

        ''' Resgatando o id da venda recem criada '''
        venda = Venda.objects.latest('pk')

        venda.save()

        ''' Criando a venda do produto na tabela auxiliar '''
        venda_produto = Produto_Venda.objects.create(venda_id=venda, produto_id=produto, quantidade=quantidade, total=total)
        venda_produto.save()

        return redirect('adicionar_produto', venda.id)