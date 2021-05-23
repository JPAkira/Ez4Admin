from django.shortcuts import redirect, get_object_or_404
from apps.estoque.models import Produto


def adicionar_estoque_com_codigo(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Requests da pagina '''
    if request.method == 'POST':
        codigo = request.POST['codigo']
        quantidade = request.POST['quantidade']

        ''' Resgatando o produto do banco de dados '''
        p = get_object_or_404(Produto, pk=codigo)

        ''' Transformando uma string em integer '''
        p.quantidade = int(p.quantidade)
        quantidade = int(quantidade)

        ''' Somando o atual estoque com as novas unidades '''
        p.quantidade += quantidade

        ''' Salvando no banco de dados '''
        p.save()

        return redirect('estoque')