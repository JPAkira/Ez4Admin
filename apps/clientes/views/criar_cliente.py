from django.contrib import messages
from django.shortcuts import render, redirect
import requests
from validate_docbr import CPF
from apps.clientes.models import Cliente


def cria_cliente(request):

    '''Autenticando o acesso a pagina'''
    if not request.user.is_authenticated:
        return redirect('login')

    ''' Requests da pagina '''
    if request.method == 'POST':
        cpf_check = request.POST['cpf']
        nome = request.POST['nome']
        email = request.POST['email']
        dd = request.POST['dd']
        numero = request.POST['numero']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        complemento = request.POST['complemento']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        cep = request.POST['cep']
        data_de_nascimento = request.POST['data_de_nascimento']
        cliente_ativo = request.POST.get('cliente_ativo')

        '''Transformando o campo vazio em None, para se adaptar ao modelo do banco de dados'''
        if campo_vazio(data_de_nascimento):
            data_de_nascimento = None

        '''Se colocou o cep mas não o endereço ele pesquisa pelo cep'''
        if campo_vazio(endereco):
            if cep:

                '''Cria cliente temporario sem o endereço'''
                cliente = Cliente.objects.create(cpf=cpf_check,  nome=nome, email=email, dd=dd, telefone=telefone, cep=cep,
                                                 data_de_nascimento=data_de_nascimento)
                cliente.save()
                '''Recupera os clientes e pega o ultimo'''

                lista_clientes = Cliente.objects.order_by('-id')

                cliente = lista_clientes[0]

                '''Pesquisa o cep na api e retorna o endereço'''
                url = "https://viacep.com.br/ws/{}/json/".format(cep)
                r = requests.get(url)
                dados = r.json()

                ''' Se o cep não for encontrado, será necessario preencher manualmente o endereço'''
                if 'erro' in dados:
                    messages.error(request, 'CEP Não Encontrado')
                    cliente_a_editar = {'cliente': cliente}
                    return render(request, 'clientes/edita_cliente.html', cliente_a_editar)

                ''' Passando os dados para o objeto já criado '''
                cliente.endereco = dados['logradouro']
                cliente.bairro = dados['bairro']
                cliente.cidade = dados['localidade']
                cliente.estado = dados['uf']

                '''Cria dicionario com os dados'''
                cliente_a_editar = {'cliente': cliente}

                return render(request, 'clientes/edita_cliente.html', cliente_a_editar)

        ''' Checkando o CPF '''
        if cpf_check:
            cpf = CPF()
            if cpf.validate(cpf_check) == False:
                messages.error(request, 'CPF Invalido')
                return redirect('cria_cliente')

        ''' Verificando se a checkbox está preenchida ou não'''
        if cliente_ativo == None:
            cliente_ativo = False
        else:
            cliente_ativo = True

        ''' Criando cliente '''
        cliente = Cliente.objects.create(cpf=cpf_check, nome=nome, email=email, dd=dd, telefone=telefone, endereco=endereco,
                                         numero=numero, complemento=complemento, bairro=bairro,
                                         cidade=cidade, estado=estado, cep=cep,
                                         data_de_nascimento=data_de_nascimento, cliente_ativo=cliente_ativo)

        ''' Salvando o cliente no banco de dados'''
        cliente.save()
        return redirect('clientes')

    else:
        return render(request, 'clientes/cria_cliente.html')

def campo_vazio(campo):
    return not campo.strip()