from Core.models import *
from Resellers.models import *
from django import forms


class EditInstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = '__all__'
        widgets = {
            'reseller': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'form-control select2'}),
            'admin': forms.Select(attrs={'class': 'form-control select2'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'payments': forms.NumberInput(attrs={'class': 'form-control'}),
            'trials': forms.NumberInput(attrs={'class': 'form-control'}),
            'expiration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_reseller': forms.CheckboxInput(),
            'is_superadmin': forms.CheckboxInput(),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'date_joined']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'user_permissions': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'staff_status': forms.CheckboxInput(),
            'is_superuser': forms.CheckboxInput(),
            'is_active': forms.CheckboxInput(),
        }


class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = [
            'percentage_on_first',
            'percentage_on_renewal',
            'allow_negative_balance',
            'max_negative_balance',

        ]