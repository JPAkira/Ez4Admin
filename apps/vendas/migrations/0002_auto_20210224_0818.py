# Generated by Django 3.1.6 on 2021-02-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='forma_de_pagamento',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_total',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='venda',
            name='volume_de_compra',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
