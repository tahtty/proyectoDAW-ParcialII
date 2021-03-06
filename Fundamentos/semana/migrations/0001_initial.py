# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('url', models.URLField(blank=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('icono', models.CharField(max_length=300)),
                ('tipo', models.CharField(choices=[('V', 'video'), ('P', 'pdf')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='recurso',
            name='semana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semana.Semana'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semana.TipoRecurso'),
        ),
    ]
