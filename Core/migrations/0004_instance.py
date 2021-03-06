# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 11:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0003_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('expiration', models.DateField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instance_admin', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='instance_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
