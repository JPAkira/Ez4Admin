# Generated by Django 3.1.6 on 2021-02-20 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0002_auto_20210215_1844'),
        ('clientes', '0007_auto_20210213_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_de_compra', models.IntegerField()),
                ('forma_de_pagamento', models.CharField(max_length=100)),
                ('valor_total', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto_Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estoque.produto')),
                ('venda_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.venda')),
            ],
        ),
    ]
