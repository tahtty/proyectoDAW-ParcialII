# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]