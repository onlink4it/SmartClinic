# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_instance_is_superadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='max_results_per_page',
            field=models.IntegerField(default=10),
        ),
    ]
