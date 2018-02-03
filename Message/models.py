# -*- coding: utf-8 -*-
from Core.fun import *
from django.db import models
from datetime import datetime, date, timedelta
from django.utils import timezone
from django.contrib.auth.models import Permission, User, Group


# Create your models here.
class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name="Sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to', verbose_name="Receiver")
    title = models.CharField(max_length=1024, null=True, verbose_name="Title")
    body = models.CharField(max_length=102400, verbose_name="Message")
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.body

    def __unicode__(self):
        return self.body

    def since(self):
        time_ago = timezone.now() - self.date
        date_different = date.today() - self.date.date()
        nice = nice_time(time_ago)
        if not nice:
            return 'Now'
        else:
            if date_different.days == 0:
                return nice
            else:
                return str(date_different.days) + " Days " + nice

    class Meta:
        ordering = ['-date']


class Attachments(models.Model):
    msg = models.ForeignKey(Message, on_delete=models.CASCADE)
    attachment = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.msg.title

    def __unicode__(self):
        return self.msg.title
