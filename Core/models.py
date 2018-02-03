# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from .fun import *


# Create your models here.
class Online(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name() + ' : ' + str(self.last_update)

    def get_status(self):
        user = self.user
        last_update = self.last_update
        now = timezone.now()
        diff = now - last_update
        date_different = date.today() - self.last_update.date()
        nice = nice_time_ar(diff)
        if not nice:
            return 'Online'
        else:
            if date_different.days == 0:
                return "منذ " + nice
            else:
                return "منذ " + str(date_different.days) + " يوم " + nice


class Instance(models.Model):
    specialty_choices = (
        (1, 'Obstetrics and Gynaecology'),
        (2, 'Pediatrics'),
    )
    specialty = models.SmallIntegerField(choices=specialty_choices, null=True)
    reseller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Reseller", blank=True)
    name = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instance_admin')
    users = models.ManyToManyField(User, related_name='instance_users', blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    payments = models.IntegerField(default=0)
    trials = models.IntegerField(default=1)
    expiration = models.DateField()
    created_on = models.DateField(auto_now_add=True, null=True)
    is_reseller = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_days_left(self):
        days_left = (self.expiration - date.today()).days
        return days_left

    def is_active(self):
        if self.get_days_left() >= 0:
            return True
        else:
            return False

    def expire_soon(self):
        if self.get_days_left() in range(0, 16):
            return True
        else:
            return False
