# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-10 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeTransactions',
            new_name='EmployeeTransaction',
        ),
    ]
