from django.db import models

class Produto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20)
    nome = models.CharField(max_length=100)
    embalagem = models.CharField(max_length=50, blank=True)
    tamanho = models.CharField(max_length=20, blank=True)
    quantidade = models.CharField(max_length=20)
    preco = models.CharField(max_length=20)

    def __str__(self):
        return self.nome