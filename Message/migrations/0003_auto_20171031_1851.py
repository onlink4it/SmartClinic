# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0002_auto_20171031_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.CharField(max_length=102400, verbose_name=b'\xd9\x86\xd8\xb5 \xd8\xa7\xd9\x84\xd8\xb1\xd8\xb3\xd8\xa7\xd9\x84\xd8\xa9'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL, verbose_name=b'\xd8\xa7\xd9\x84\xd9\x85\xd8\xb1\xd8\xb3\xd9\x84 \xd8\xa5\xd9\x84\xd9\x8a\xd9\x87'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name=b'\xd8\xa7\xd9\x84\xd8\xb1\xd8\xa7\xd8\xb3\xd9\x84'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=1024, null=True, verbose_name=b'\xd8\xa7\xd9\x84\xd8\xb9\xd9\x86\xd9\x88\xd8\xa7\xd9\x86'),
        ),
    ]
