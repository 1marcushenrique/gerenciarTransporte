# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciaTransp', '0008_solicitar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataH_liberacao', models.DateTimeField(blank=True, null=True)),
                ('situacao', models.BooleanField(default=False, verbose_name='Solicitação atendida?')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciaTransp.Funcionario')),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciaTransp.Motorista')),
                ('socilitacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gerenciaTransp.Solicitar')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciaTransp.Veiculo')),
            ],
        ),
    ]