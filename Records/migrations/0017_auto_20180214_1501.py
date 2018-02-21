# Generated by Django 2.0.2 on 2018-02-14 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0016_auto_20180204_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PatientLabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('result', models.TextField(null=True)),
                ('result_at', models.DateField(null=True)),
                ('img1', models.FileField(blank=True, null=True, upload_to='')),
                ('img2', models.FileField(blank=True, null=True, upload_to='')),
                ('img3', models.FileField(blank=True, null=True, upload_to='')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.PatientRecord')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.LabTest')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRadiology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('result', models.TextField(null=True)),
                ('result_at', models.DateField(null=True)),
                ('img1', models.FileField(blank=True, null=True, upload_to='')),
                ('img2', models.FileField(blank=True, null=True, upload_to='')),
                ('img3', models.FileField(blank=True, null=True, upload_to='')),
                ('record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.PatientRecord')),
            ],
        ),
        migrations.CreateModel(
            name='Radiology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='patientradiology',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Records.Radiology'),
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='lab_tests_asked',
            field=models.ManyToManyField(blank=True, to='Records.LabTest'),
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='radiology_asked',
            field=models.ManyToManyField(blank=True, to='Records.Radiology'),
        ),
    ]
