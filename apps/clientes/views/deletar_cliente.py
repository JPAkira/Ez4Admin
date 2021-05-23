from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from apps.clientes.models import Cliente


def deleta_cliente(request, cliente_id):

    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o usuario do banco de dados pela primary key '''

    cliente = get_object_or_404(Cliente, pk=cliente_id)

    ''' Deletando o cliente do banco de dados '''

    cliente.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('clientes')