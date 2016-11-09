# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_tool', '0016_auto_20161109_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='annotation',
        ),
        migrations.AddField(
            model_name='annotation',
            name='name',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='name',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
