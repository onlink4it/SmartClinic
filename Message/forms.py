# -*- coding: utf-8 -*-
from django import forms
from .models import *
from tinymce.widgets import TinyMCE


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = [
            'read',
            'read_at',
            'sender',
            'receiver',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': TinyMCE(attrs={'class': 'form-control'})
        }


class MessageAttachmentsForm(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ['attachment']
        widgets = {
            'attachment': forms.FileInput(attrs={'class': 'form-control', 'multiple': 'multiple'})
        }


class ReplyMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = [
            'read',
            'read_at',
            'sender',
            'receiver',
            'title',
        ]
        widgets = {
            'body': TinyMCE(attrs={'class': 'form-control'})
        }

class ForwardMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = [
            'read',
            'read_at',
            'sender',
            'receiver',
            'title',
        ]
        widgets = {
            'body': TinyMCE(attrs={'class': 'form-control'})
        }