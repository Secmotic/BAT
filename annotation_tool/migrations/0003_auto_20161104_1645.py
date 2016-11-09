# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_tool', '0002_auto_20161104_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='primary_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotation_tool.Class'),
        ),
        migrations.AddField(
            model_name='tags',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotation_tool.Event'),
        ),
    ]
