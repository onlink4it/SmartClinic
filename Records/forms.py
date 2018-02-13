from .models import *
from django import forms
from tinymce.widgets import TinyMCE
from django_select2.forms import ModelSelect2MultipleWidget


class MedicineWidget(ModelSelect2MultipleWidget):
    model = Medicine
    search_fields = [
        'name__icontains',
    ]


class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['date_added', 'instance']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'}),
            'husband_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'rh': forms.NumberInput(attrs={'class': 'form-control'}),
            'cbc': forms.TextInput(attrs={'class': 'form-control'}),
            'hb': forms.TextInput(attrs={'class': 'form-control'}),
            'taxoplasma': forms.TextInput(attrs={'class': 'form-control'}),
            'rubella': forms.TextInput(attrs={'class': 'form-control'}),
            'other_investigation': forms.TextInput(attrs={'class': 'form-control'}),
            'fsh': forms.TextInput(attrs={'class': 'form-control'}),
            'lh': forms.TextInput(attrs={'class': 'form-control'}),
            'e2': forms.TextInput(attrs={'class': 'form-control'}),
            'tsh': forms.TextInput(attrs={'class': 'form-control'}),
            'hs': forms.TextInput(attrs={'class': 'form-control'}),
            'male_f': forms.TextInput(attrs={'class': 'form-control'}),
            'other_hermones': forms.TextInput(attrs={'class': 'form-control'}),
            'ut': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_tube': forms.TextInput(attrs={'class': 'form-control'}),
            'lt_tube': forms.TextInput(attrs={'class': 'form-control'}),
            'rt_ov': forms.TextInput(attrs={'class': 'form-control'}),
            'lt_ov': forms.TextInput(attrs={'class': 'form-control'}),
            'dp': forms.TextInput(attrs={'class': 'form-control'}),
            'other_laprospic_finding': forms.TextInput(attrs={'class': 'form-control'}),
            'laprospic_report': forms.FileInput(),
            'twins': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'diabetes': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'cfm': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'hypertention': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'cancer': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'cns': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'operations': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'drugs': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'abortion': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'ectopic': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'v_mole': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'deliveries': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'xx': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'xy': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'still_birth': forms.CheckboxInput(attrs={'class': 'flat-red'}),
            'co': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'l_n_m_b': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'e_d_d': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'readonly'}),

            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'antenatal_history': forms.Textarea(attrs={'class': 'form-control'}),
            'wt_at_birth': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_of_pregnancy': forms.TextInput(attrs={'class': 'form-control'}),
            'mode_of_delivery': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor': forms.TextInput(attrs={'class': 'form-control'}),
            'father_abo': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_abo': forms.TextInput(attrs={'class': 'form-control'}),
            'consanguinity': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control'}),
            'diseases': forms.TextInput(attrs={'class': 'form-control'}),
            'nutrition': forms.Textarea(attrs={'class': 'form-control'}),
            'social_smile': forms.NumberInput(attrs={'class': 'form-control'}),
            'head_support': forms.NumberInput(attrs={'class': 'form-control'}),
            'set_alone': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_teething': forms.NumberInput(attrs={'class': 'form-control'}),
            'crawl': forms.NumberInput(attrs={'class': 'form-control'}),
            'walk_alone': forms.NumberInput(attrs={'class': 'form-control'}),
            'speech': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AddPatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        exclude = [
            'date',
            'patient',
        ]
        widgets = {
            'b_p': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'oedama': forms.NumberInput(attrs={'class': 'form-control'}),
            'fundel_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'urine_suger': forms.NumberInput(attrs={'class': 'form-control'}),
            'urine_albumin': forms.NumberInput(attrs={'class': 'form-control'}),
            'week': forms.NumberInput(attrs={'class': 'form-control'}),
            'h_b_percent': forms.NumberInput(attrs={'class': 'form-control'}),
            'comments_complain': TinyMCE(attrs={'class': 'form-control'}),
            'prescription': MedicineWidget(attrs={'class': 'form-control select2', 'multiple': 'multiple'}),


            'problem': TinyMCE(attrs={'class': 'form-control'}),
            'h_c': forms.NumberInput(attrs={'class': 'form-control'}),
            'l_t': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'prescriptions': forms.SelectMultiple(attrs={'class': 'form-control select2'})
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class COForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ['complain']
        widgets = {
            'complain': forms.TextInput(attrs={'class': 'form-control'}),
        }