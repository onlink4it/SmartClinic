# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queues', '0010_auto_20171124_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='done',
            field=models.BooleanField(default=True),
        ),
    ]
