# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queues', '0013_auto_20171210_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='consultant_fees',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clinic',
            name='examination_fees',
            field=models.IntegerField(default=0),
        ),
    ]