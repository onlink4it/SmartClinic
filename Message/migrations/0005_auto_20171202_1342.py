# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-02 11:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0004_auto_20171102_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.CharField(max_length=102400, verbose_name=b'Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL, verbose_name=b'Receiver'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name=b'Sender'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'Title'),
        ),
    ]