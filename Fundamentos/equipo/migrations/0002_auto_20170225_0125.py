# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Profesor'), ('C', 'Coordinador')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='equipo',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.Cargo'),
        ),
    ]
