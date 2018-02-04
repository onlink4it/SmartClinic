# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_instance_trials'),
        ('Resellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('comment', models.TextField(null=True)),
                ('instance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.Instance')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Resellers.Service')),
            ],
        ),
    ]