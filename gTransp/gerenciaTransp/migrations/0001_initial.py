# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome ')),
                ('fone', models.CharField(max_length=100, verbose_name='FONE ')),
            ],
        ),
    ]