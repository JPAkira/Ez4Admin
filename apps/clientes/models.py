from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, blank=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=200, blank=True)
    dd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=9)
    numero = models.CharField(max_length=5, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)
    cliente_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome