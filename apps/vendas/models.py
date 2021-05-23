from django.db import models
from apps.clientes.models import Cliente
from apps.estoque.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    volume_de_compra = models.IntegerField()
    forma_de_pagamento = models.CharField(max_length=100, blank=True)
    valor_total = models.FloatField()
    valor_pago = models.FloatField(blank=True, null=True, default=0.00)
    troco = models.FloatField(blank=True, null=True, default=0.00)


class Produto_Venda(models.Model):
    venda_id = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto_id = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    total = models.FloatField()