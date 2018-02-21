from django import forms
from .models import *
from Core.views import *
from datetime import date
from django_select2.forms import ModelSelect2Widget, Select2Widget, HeavySelect2Widget


class PatientWidget(ModelSelect2Widget):
    model = Patient
    search_fields = [
        'name__icontains',
        'phone__icontains',
    ]


class AssignDateForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'date',
            'task_type',
            'patient',
        ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control select2 patient'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today})
        }


class AssignDateForPatientForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'date',
            'task_type',
            'clinic',
        ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control select2 patient'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today})
        }


class AssignConsultantForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'date',
            'task_type',
        ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class QueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = [
            'balance_before',
            'service_cost',
            'paid',
        ]
        widgets = {
            'paid': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        exclude = ['admin']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'examination_fees': forms.NumberInput(attrs={'class': 'form-control'}),
            'consultant_fees': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ClinicAuthForm(forms.ModelForm):
    class Meta:
        model = EmployeeAuth
        fields = ['allowed_clinic']
        widgets = {
            'allowed_clinic': forms.SelectMultiple(attrs={'class': 'form-control select2'})
        }


class EditCalendarDate(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'date'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class AssignDate2Form(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'date',
            'patient',
        ]
        widgets = {
            'task_type': forms.RadioSelect(),
            'patient': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today})
        }


class ClinicServiceForm(forms.ModelForm):
    class Meta:
        model = ClinicServices
        fields = [
            'name',
            'price',
        ]
