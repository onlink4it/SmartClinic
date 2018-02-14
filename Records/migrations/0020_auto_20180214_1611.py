# Generated by Django 2.0.2 on 2018-02-14 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0019_auto_20180214_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientlabtest',
            name='record',
        ),
        migrations.RemoveField(
            model_name='patientradiology',
            name='record',
        ),
        migrations.AddField(
            model_name='patientlabtest',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.Patient'),
        ),
        migrations.AddField(
            model_name='patientradiology',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.Patient'),
        ),
    ]
