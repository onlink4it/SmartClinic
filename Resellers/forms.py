from .models import *
from django import forms
from Core.models import *


class ChooseServiceForm(forms.ModelForm):
    class Meta:
        model = CustomerTransaction
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'})
        }


class ChooseSpecialtyForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['specialty']
        widgets = {
            'specialty': forms.Select(attrs={'class': 'form-control select2'})
        }