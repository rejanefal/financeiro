# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0012_auto_20170424_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientepessoafisica',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='clientepessoafisica',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='clientepessoafisica',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='clientepessoafisica',
            name='identificacao',
        ),
        migrations.RemoveField(
            model_name='clientepessoajuridica',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='clientepessoajuridica',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='clientepessoajuridica',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='clientepessoajuridica',
            name='identificacao',
        ),
        migrations.AddField(
            model_name='cliente',
            name='classificacao',
            field=models.CharField(default=None, max_length=18),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='financas.Endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='funcao',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='cliente',
            name='identificacao',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
