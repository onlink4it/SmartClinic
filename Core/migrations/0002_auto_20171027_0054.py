# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-27 00:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientrecord',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='PatientRecord',
        ),
    ]
