# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 07:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoxScore', '0004_auto_20161110_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarterscore',
            name='game_date',
            field=models.DateField(blank=True, default=datetime.date(2016, 11, 11)),
        ),
    ]
