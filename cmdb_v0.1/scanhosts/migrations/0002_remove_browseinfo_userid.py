# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='browseinfo',
            name='userid',
        ),
    ]
