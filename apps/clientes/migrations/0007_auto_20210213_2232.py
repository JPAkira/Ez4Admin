# Generated by Django 3.1.6 on 2021-02-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_remove_cliente_aceita_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_de_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
