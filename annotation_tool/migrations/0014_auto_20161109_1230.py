# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_tool', '0013_auto_20161109_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
