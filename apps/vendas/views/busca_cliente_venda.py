from django.db.models import Q
from django.shortcuts import render, redirect
from apps.clientes.models import Cliente


def busca_cliente_venda(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    '''Buscar clientes'''

    lista_clientes = Cliente.objects.order_by('nome')

    '''Pega o campo buscar e busca como filtro'''

    if request.method == 'POST':
        nome_a_buscar = request.POST['buscar']
        if nome_a_buscar:
            lista_clientes = lista_clientes.filter(Q(nome__icontains=nome_a_buscar)|Q(cpf__icontains=nome_a_buscar))

    '''Cria dicionario com os dados'''

    dados = {
        'clientes': lista_clientes
    }
    return render(request, 'vendas/selecionar_cliente.html', dados)


