# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciaTransp', '0002_funcionario_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefixo', models.CharField(max_length=20, verbose_name='Prefixo ')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca ')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo ')),
                ('ano', models.CharField(max_length=10, verbose_name='Ano ')),
                ('placa', models.CharField(max_length=4, verbose_name='Placa ')),
            ],
        ),
    ]
