# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_instance_trials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='reseller',
            field=models.BooleanField(default=False),
        ),
    ]
