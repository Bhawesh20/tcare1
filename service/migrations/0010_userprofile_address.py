# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20170316_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
