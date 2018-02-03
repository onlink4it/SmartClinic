# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0007_medicine_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.Instance'),
        ),
    ]
