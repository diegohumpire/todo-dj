# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160311_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
