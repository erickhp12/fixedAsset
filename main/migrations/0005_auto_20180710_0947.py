# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-10 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180710_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha_inicio'),
        ),
    ]
