# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_auto_20180116_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
    ]