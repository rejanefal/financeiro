# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_auto_20170423_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
