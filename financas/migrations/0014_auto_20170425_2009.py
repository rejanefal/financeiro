# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0013_auto_20170424_2044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AlterModelOptions(
            name='baixasapagar',
            options={'verbose_name_plural': 'Baixas a pagar'},
        ),
        migrations.AlterModelOptions(
            name='baixasareceber',
            options={'verbose_name_plural': 'Baixas a receber'},
        ),
        migrations.AlterModelOptions(
            name='clientepessoafisica',
            options={'verbose_name_plural': 'Cliente pessoa física'},
        ),
        migrations.AlterModelOptions(
            name='clientepessoajuridica',
            options={'verbose_name_plural': 'Cliente pessoa jurídica'},
        ),
        migrations.AlterModelOptions(
            name='contasbancarias',
            options={'verbose_name_plural': 'Conta bancária'},
        ),
        migrations.AlterModelOptions(
            name='empresas',
            options={'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name_plural': 'Endereço'},
        ),
        migrations.AlterModelOptions(
            name='formasdepagamento',
            options={'verbose_name_plural': 'Formas de pagamento'},
        ),
        migrations.AlterModelOptions(
            name='fornecedorpessoafisica',
            options={'verbose_name_plural': 'Fornecedor pessoa física'},
        ),
        migrations.AlterModelOptions(
            name='lancamentosapagar',
            options={'verbose_name_plural': 'Lançamentos a pagar'},
        ),
        migrations.AlterModelOptions(
            name='lancamentosareceber',
            options={'verbose_name_plural': 'Lançamentos a receber'},
        ),
        migrations.AlterModelOptions(
            name='pessoafisica',
            options={'verbose_name_plural': 'Pessoa física'},
        ),
        migrations.AlterModelOptions(
            name='pessoajuridica',
            options={'verbose_name_plural': 'Pessoa jurídica'},
        ),
        migrations.AlterModelOptions(
            name='planodecontas',
            options={'verbose_name_plural': 'Plano de contas'},
        ),
        migrations.AlterModelOptions(
            name='tesouraria',
            options={'verbose_name_plural': 'Tesouraria'},
        ),
    ]