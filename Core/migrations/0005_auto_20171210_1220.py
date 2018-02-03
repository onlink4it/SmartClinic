# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 12:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='instance_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
