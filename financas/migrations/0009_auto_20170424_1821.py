# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0008_auto_20170424_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
