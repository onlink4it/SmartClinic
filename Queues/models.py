# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Records.models import *
from django.contrib.auth.models import User


# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    examination_fees = models.IntegerField(default=0)
    consultant_fees = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class EmployeeAuth(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    allowed_clinic = models.ManyToManyField(Clinic, blank=True)

    def __str__(self):
        return self.employee.get_full_name()


class Calendar(models.Model):
    task_types = (
        (1, 'كشف جديد'),
        (2, 'إعادة كشف'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Patient')
    date = models.DateTimeField(verbose_name='Date')
    task_type = models.IntegerField(verbose_name='Type', choices=task_types)
    attend = models.BooleanField(verbose_name='Attend', default=False)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.patient.name

    def get_type(self):
        if self.task_type == 1:
            return 'كشف جديد'
        elif self.task_type == 2:
            return 'إعادة كشف'


class Queue(models.Model):
    date = models.DateField(auto_now_add=True, null=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)
    paid = models.FloatField(default=0.0)
    refund = models.BooleanField(default=False)
    refund_reason = models.CharField(max_length=128, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.calendar.patient.name

    class Meta:
        ordering = ['-id']
