# Generated by Django 2.0.2 on 2018-02-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queues', '0020_queue_service_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='balance_before',
            field=models.FloatField(default=0.0),
        ),
    ]
