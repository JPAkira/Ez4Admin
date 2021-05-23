from django.shortcuts import render, redirect
from apps.vendas.models import Venda

def busca_venda(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    '''Buscar clientes'''

    lista_vendas = Venda.objects.order_by('cliente')

    '''Pega o campo buscar e busca como filtro'''

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_vendas = lista_vendas.filter(cliente__nome__icontains=nome_a_buscar)

    '''Cria dicionario com os dados'''

    dados = {
        'vendas': lista_vendas
    }

    return render(request, 'vendas/vendas.html', dados)


