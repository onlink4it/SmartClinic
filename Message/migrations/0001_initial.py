# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.CharField(max_length=1024)),
                ('first_msg', models.BooleanField(default=True)),
                ('read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='message_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Message.MessageGroup'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attachments',
            name='msg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Message.Message'),
        ),
    ]
