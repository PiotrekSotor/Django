# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]