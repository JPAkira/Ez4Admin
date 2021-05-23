# Generated by Django 3.1.6 on 2021-02-14 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210213_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='aceita_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_de_nascimento',
            field=models.DateField(blank=True),
        ),
    ]