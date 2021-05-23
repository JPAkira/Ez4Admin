import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from apps.clientes.models import Cliente

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        dd ="{}".format(random.randrange(10, 21))
        celular = "9{}{}".format(random.randrange(4000, 9999), random.randrange(4000, 9999))
        print("{} - {}".format(nome, celular))
        cep = "{}{}".format(random.randrange(4000, 9999), random.randrange(4000, 9999))
        endereco = "Default Endereço"
        bairro = "Default Bairro"
        cidade = "Default Cidade"
        estado = "SC"
        ativo = random.choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, dd=dd, telefone=celular, cep=cep, endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, cliente_ativo=ativo)
        p.save()

criando_pessoas(100)
print("Sucesso")