import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from apps.estoque.models import Produto


my_word_list = [
'Refrigerante','Doce','Guaraná',
'Frutas','Gelado','Light']


def criando_produto(quantidade_de_produtos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_produtos):
        codigo = "{}{}".format(random.randrange(4000, 9999), random.randrange(4000, 9999))
        nome = fake.sentence(ext_word_list=my_word_list)
        embalagem = 'Pet'
        tamanho = '2 L'
        quantidade = "{}".format(random.randrange(1, 999))
        preco ="9.99"
        print("{} - {}".format(nome, preco))
        p = Produto(nome=nome, codigo=codigo, embalagem=embalagem, tamanho=tamanho, quantidade=quantidade, preco=preco)
        p.save()

criando_produto(100)
print("Sucesso")