# Generated by Django 3.1.6 on 2021-02-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('embalagem', models.CharField(blank=True, max_length=50)),
                ('tamanho', models.CharField(max_length=20)),
                ('quantidade', models.CharField(max_length=20)),
                ('preco', models.CharField(max_length=20)),
            ],
        ),
    ]
