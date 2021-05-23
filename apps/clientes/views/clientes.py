from django.shortcuts import render, redirect
from apps.clientes.models import Cliente
from django.core.paginator import Paginator, EmptyPage


def clientes(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Resgatando todos os clientes do banco de dados '''
    clientes = Cliente.objects.order_by('nome')

    p = Paginator(clientes, 20)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    dados = {
        'clientes': page
    }

    return render(request, 'clientes/clientes.html', dados)
