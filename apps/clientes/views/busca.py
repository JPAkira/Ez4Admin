from django.db.models import Q
from django.shortcuts import render, redirect
from apps.clientes.models import Cliente
from django.core.paginator import Paginator, EmptyPage

def buscar(request):

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

    p = Paginator(lista_clientes, 100)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    dados = {
        'clientes': page
    }
    return render(request, 'clientes/clientes.html', dados)


