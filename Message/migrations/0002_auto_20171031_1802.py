# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='first_msg',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_group',
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.CharField(max_length=102400),
        ),
        migrations.DeleteModel(
            name='MessageGroup',
        ),
    ]
