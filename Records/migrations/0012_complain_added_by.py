# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-17 17:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Records', '0011_auto_20171217_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
