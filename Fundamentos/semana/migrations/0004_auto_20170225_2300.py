# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 04:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semana', '0003_auto_20170225_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recurso',
            old_name='file',
            new_name='file_recurso',
        ),
    ]
