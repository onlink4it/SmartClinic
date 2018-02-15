# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Queues.models import *
from django.contrib.auth.models import User


# Create your models here.
class MoneyTransaction(models.Model):
    date = models.DateField(auto_now_add=True)
    income = models.FloatField(default=0)
    outcome = models.FloatField(default=0, verbose_name="مصروف")
    comment = models.TextField(verbose_name="ملاحظات")
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)
    done_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comment


class MainCategory(models.Model):
    name = models.CharField(max_length=128)


class EmployeeTransaction(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.date) + self.employee.get_full_name()

    class Meta:
        ordering = ('-id',)


class PatientTransaction(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(ClinicServices, on_delete=models.SET_NULL, null=True)
    credit = models.FloatField(default=0.0)
    debit = models.FloatField(default=0.0)
    comment = models.TextField(null=True, blank=True)
    done_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.patient.name
