# Generated by Django 3.1.6 on 2021-02-14 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210213_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='aceita_email',
        ),
    ]