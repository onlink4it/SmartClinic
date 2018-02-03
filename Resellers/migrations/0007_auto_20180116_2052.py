# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-16 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Resellers', '0006_auto_20180116_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('for_new_customers', models.BooleanField(default=True)),
                ('for_renewal', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resellers.Service'),
        ),
    ]
