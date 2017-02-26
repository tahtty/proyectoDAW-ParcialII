# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_auto_20170225_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinador',
            old_name='foto',
            new_name='foto_url',
        ),
        migrations.RenameField(
            model_name='profesores',
            old_name='foto',
            new_name='foto_url',
        ),
        migrations.AddField(
            model_name='coordinador',
            name='file_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profesores',
            name='file_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]