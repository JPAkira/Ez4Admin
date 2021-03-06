# Generated by Django 3.1.6 on 2021-02-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('dd', models.CharField(default='', max_length=2)),
                ('telefone', models.CharField(default='', max_length=9)),
                ('endereco', models.CharField(max_length=200)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('data_de_nascimento', models.DateField()),
                ('cliente_ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
