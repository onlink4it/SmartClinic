# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Queues', '0007_auto_20171124_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='calendar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Queues.Calendar'),
        ),
    ]