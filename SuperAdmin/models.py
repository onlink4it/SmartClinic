# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class SuperAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
