# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-12 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookManager',
        ),
    ]
