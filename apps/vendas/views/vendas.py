from django.shortcuts import render, redirect

from apps.vendas.models import Venda


def vendas(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    vendas = Venda.objects.order_by('pk')

    dados = {
        'vendas': vendas
    }

    return render(request, 'vendas/vendas.html', dados)