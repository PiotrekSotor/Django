# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_code',
            field=models.CharField(max_length=200, unique=1),
        ),
    ]
