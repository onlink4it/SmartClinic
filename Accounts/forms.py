from django import forms
from .models import *


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = MoneyTransaction
        fields = [
            'outcome',
            'comment'
        ]
        widgets = {
            'outcome': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = MoneyTransaction
        fields = [
            'income',
            'comment'
        ]
        widgets = {
            'income': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmployeeTransactionForm(forms.ModelForm):
    class Meta:
        model = EmployeeTransaction
        fields = [
            'amount'
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }