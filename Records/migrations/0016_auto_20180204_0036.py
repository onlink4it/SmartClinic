# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0015_patient_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='laprospic_report',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
