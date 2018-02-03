# -*- coding: utf-8 -*-
from .models import *
from django import forms
from django.contrib.auth.models import Permission, User


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['specialty', 'mobile']
        widgets = {
            'specialty': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
        }

