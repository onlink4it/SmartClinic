# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-14 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_instance_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='specialty',
            field=models.SmallIntegerField(choices=[(1, 'Obstetrics and Gynaecology'), (2, 'Pediatrics')], null=True),
        ),
    ]
