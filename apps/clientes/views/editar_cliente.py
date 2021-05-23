from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from validate_docbr import CPF
from apps.clientes.models import Cliente

def editar_cliente(request, cliente_id):

    '''Autenticando o acesso a pagina'''

    if not request.user.is_authenticated:
        return redirect('login')

    ''' Pegando o cliente do banco de dados pela primary key '''

    cliente = get_object_or_404(Cliente, pk=cliente_id)

    ''' Criando um dicionario com os dados '''

    cliente_a_editar = {'cliente': cliente}
    return render(request, 'clientes/edita_cliente.html', cliente_a_editar)

def atualizar_cliente(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        ''' Resgatando o cliente do banco de dados, para atualizar '''

        id = request.POST['cliente_id']
        c = get_object_or_404(Cliente, pk=id)

        c.cpf = request.POST['cpf']
        c.nome = request.POST['nome']
        c.email = request.POST['email']
        c.dd = request.POST['dd']
        c.telefone = request.POST['telefone']
        c.numero = request.POST['numero']
        c.endereco = request.POST['endereco']
        c.complemento = request.POST['complemento']
        c.bairro = request.POST['bairro']
        c.cidade = request.POST['cidade']
        c.estado = request.POST['estado']
        c.cep = request.POST['cep']
        c.data_de_nascimento = request.POST['data_de_nascimento']
        cliente_ativo = request.POST.get('cliente_ativo')

        ''' Checkando o CPF '''

        if c.cpf:
            cpf = CPF()
            if cpf.validate(c.cpf) == False:
                messages.error(request, 'CPF Invalido')
                return redirect('editar_cliente', cliente_id=c.id)


        ''' Pegando dado da checkbox None=False, on=True '''

        if cliente_ativo == None:
            c.cliente_ativo = False
        else:
            c.cliente_ativo = True

        ''' Salvando no banco de dados '''

        c.save()
        return redirect('clientes')
    else:
        return render(request, 'clientes/editar_cliente.html')

def campo_vazio(campo):
    return not campo.strip()