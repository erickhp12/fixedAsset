# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-02 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180702_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='imagen1',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='main',
            name='imagen2',
        ),
    ]
