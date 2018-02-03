# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from .models import *
from Queues.models import *
from django.db.models import Q
from Core.views import *
from .forms import *
import os.path
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@login_required(login_url='Core:login_user')
def add_patient(request):
    form = AddPatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        patient = form.save(commit=False)
        patient.instance = get_instance(request)
        patient.save()
        return redirect('Records:view_patient', patient.id)
    context = {'form': form}
    instance = get_instance(request)
    return render(request, 'Records/' + str(instance.specialty) + '/add_patient.html', context)


@login_required(login_url='Core:login_user')
def add_patient_for_clinic(request, clinic_id):
    form = AddPatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        patient = form.save(commit=False)
        patient.instance = get_instance(request)
        patient.save()
        return redirect('Queues:today_calendar_for_clinic', clinic_id)
    context = {'form': form}
    instance = get_instance(request)
    return render(request, 'Records/' + str(instance.specialty) + '/add_patient.html', context)


@login_required(login_url='Core:login_user')
def view_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if patient.instance == get_instance(request):
        form = AddPatientForm(request.POST or None, request.FILES or None, instance=patient)
        form2 = COForm(request.POST or None)
        if form.is_valid():
            patient = form.save()
            if patient.l_n_m_b:
                patient.e_d_d = patient.l_n_m_b + timedelta(weeks=40)
            patient.save()
            return redirect('Core:index')
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'form': form,
        'form2': form2,
        'patient': patient,
    }

    instance = get_instance(request)
    return render(request, 'Records/' + str(instance.specialty) + '/view_patient.html', context)


@login_required(login_url='Core:login_user')
def view_patient_for_clinic(request, clinic_id, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if patient.instance == get_instance(request) and clinic.admin == get_instance(request).admin:
        form = AddPatientForm(request.POST or None, request.FILES or None, instance=patient)
        form2 = COForm(request.POST or None)
        if form.is_valid():
            patient = form.save()
            if patient.l_n_m_b:
                patient.e_d_d = patient.l_n_m_b + timedelta(weeks=40)
            patient.save()
            return redirect('Queues:today_calendar_for_clinic', clinic_id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'form': form,
        'form2': form2,
        'patient': patient,
        'clinic_id': clinic_id,
    }
    instance = get_instance(request)
    return render(request, 'Records/' + str(instance.specialty) + '/view_patient_for_clinic.html', context)


@login_required(login_url='Core:login_user')
def add_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if patient.instance == get_instance(request):
        form = AddPatientRecordForm(request.POST or None)
        form2 = MedicineForm(request.POST or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            medications = form.cleaned_data['prescription']
            for x in medications.all():
                record.prescription.add(x)
            return redirect('Records:view_patient', patient_id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'patient': patient,
        'form': form,
        'form2': form2,
    }

    instance = get_instance(request)

    return render(request, 'Records/' + str(instance.specialty) + '/add_record.html', context)


@login_required(login_url='Core:login_user')
def add_record_for_clinic(request, clinic_id, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if patient.instance == get_instance(request) and clinic.admin == get_instance(request).admin:
        form = AddPatientRecordForm(request.POST or None)
        form2 = MedicineForm(request.POST or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            medications = form.cleaned_data['prescription']
            for x in medications.all():
                record.prescription.add(x)
            return redirect('Records:view_patient_for_clinic', clinic_id, patient_id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'patient': patient,
        'form': form,
        'form2': form2,
        'clinic_id': clinic_id,
    }
    instance = get_instance(request)

    return render(request, 'Records/' + str(instance.specialty) + '/add_record_for_clinic.html', context)


@login_required(login_url='Core:login_user')
def search(request):
    if request.POST or request.GET:
        if not request.POST:
            if request.GET.get('q'):
                q = request.GET.get('q')
                results = Patient.objects.filter(Q(phone__contains=q) | Q(name__contains=q),
                                                 instance=get_instance(request))
                search = True
                title = 'Search Results For: ' + q
                context = {
                    'title': title,
                    'search': search,
                    'title': title,
                    'results': results,
                }
                instance = get_instance(request)
                return render(request, 'Records/search.html', context)
        if request.POST.get('id', 0):
            patient_id = request.POST.get('id')
            results = Patient.objects.filter(Q(phone__contains=patient_id), instance=get_instance(request))
            title = 'Search Results For Phone: ' + patient_id
            search = True
            context = {
                'search': search,
                'title': title,
                'patient_id': patient_id,
                'results': results,
            }

            instance = get_instance(request)
            return render(request, 'Records/search.html', context)

        elif request.POST.get('name', 0):
            patient_name = request.POST.get('name')
            results = Patient.objects.filter(name__contains=patient_name, instance=get_instance(request))
            title = 'Search Results For Name: ' + patient_name
            search = True
            context = {
                'search': search,
                'title': title,
                'patient_name': patient_name,
                'results': results,
            }
            instance = get_instance(request)
            return render(request, 'Records/search.html', context)

        else:
            results = Patient.objects.filter(instance=get_instance(request))
            title = 'Search Results For : '
            search = True
            context = {
                'search': search,
                'title': title,
                'results': results,
            }

            instance = get_instance(request)
            return render(request, 'Records/search.html', context)
    else:
        title = 'Search'
        context = {
            'title': title
        }

        instance = get_instance(request)
        return render(request, 'Records/search.html', context)


@login_required(login_url='Core:login_user')
def delete_patient(request, patient_id):
    if request.user.is_superuser:
        clinic = Clinic.objects.get(admin=request.user)
        patient = get_object_or_404(Patient, id=patient_id, instance=get_instance(request))
        if patient.instance == get_instance(request) and clinic.admin == get_instance(request).admin:
            patient.delete()
        else:
            return render(request, 'Core/permission_error.html')
    else:
        return render(request, 'Core/permission_error.html')
    return redirect('Records:search')


@login_required(login_url='Core:login_user')
def list_medicine(request):
    medicine = Medicine.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(medicine, 100)
    try:
        medicine = paginator.page(page)
    except PageNotAnInteger:
        medicine = paginator.page(1)
    except EmptyPage:
        medicine = paginator.page(paginator.num_pages)
    context = {'medicine': medicine}
    return render(request, 'Records/list_medicine.html', context)


@login_required(login_url='Core:login_user')
def new_medicine(request):
    title = 'New Medicine'
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        medicine = form.save()
        medicine.added_by = request.user
        medicine.save()
        return redirect('Records:list_medicine')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def edit_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.user.is_superuser and request.user == medicine.added_by:
        title = 'Edit Medicine'
        form = MedicineForm(request.POST or None, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('Records:list_medicine')
        context = {
            'title': title,
            'form': form,
        }
        return render(request, 'Core/form.html', context)
    else:
        return render(request, 'Core/permission_error.html')


@login_required(login_url='Core:login_user')
def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.user.is_superuser and request.user == medicine.added_by:
        medicine.delete()
        return redirect('Records:list_medicine')
    else:
        return render(request, 'Core/permission_error.html')


@login_required(login_url='Core:login_user')
def get_medicine_api(request):
    medicine = Medicine.objects.all()
    return render(request, 'Records/get_medicine_api.html', {'medicine': medicine})


@login_required(login_url='Core:login_user')
def print_prescription(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)
    if record.patient.instance == get_instance(request):
        context = {
            'record': record
        }
        return render(request, 'Records/reciept_print.html', context)
    else:
        return render(request, 'Core/permission_error.html')


@login_required(login_url='Core:login_user')
def new_co(request):
    form = COForm(request.POST or None)
    if form.is_valid():
        co = form.save(commit=False)
        co.added_by = request.user
        co.save()
    return render(request, 'Core/form.html', {'form': form})


@login_required(login_url='Core:login_user')
def get_co_api(request):
    all = Complain.objects.filter(added_by=request.user)
    return render(request, 'Records/get_co_api.html', {'all': all})


@login_required(login_url='Core:login_user')
def import_from_csv(request):
    instance = get_instance(request)
    BASE = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(BASE, "b.csv"), mode='r', encoding="utf-8")
    content = f.readlines()
    done = 0
    for x in content:
        col = x.split(',')
        try:
            patient = Patient.objects.get(phone='0' + str(col[3]), instance=instance, name=col[1], code=col[0])
        except:
            patient = Patient()
        patient.instance = instance
        patient.code = col[0]
        patient.name = col[1]
        patient.address = col[2]
        patient.phone = '0' + str(col[3])
        patient.save()
        done += 1
    f.close()
    os.remove(os.path.join(BASE, 'b.csv'))
    context = {
        'content': content,
        'done': done
    }
    return render(request, 'Records/import.html', context)


@login_required(login_url='Core:login_user')
def remove_my_patients(request):
    instance = get_instance(request)
    my_patients = Patient.objects.filter(instance=instance)
    done = 0
    for x in my_patients:
        x.delete()
        done += 1
    context = {
        'done': done
    }
    return render(request, 'Records/import.html', context)


@login_required(login_url='Core:login_user')
def import_medicine(request):
    BASE = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(BASE, "medicine.csv"), mode='r', encoding="utf-8")
    content = f.readlines()
    done = 0
    for x in content:
        col = x.split(',')
        try:
            medicine = Medicine.objects.get(name=col[1])
        except:
            medicine = Medicine()
        medicine.name = col[1]
        medicine.added_by = request.user
        medicine.save()
        done += 1
    f.close()
    os.remove(os.path.join(BASE, 'medicine.csv'))
    context = {
        'content': content,
        'done': done
    }
    return render(request, 'Records/import.html', context)


@login_required(login_url='Core:login_user')
def remove_medicine(request):
    instance = get_instance(request)
    my_medicine = Medicine.objects.filter(added_by=request.user)
    done = 0
    for x in my_medicine:
        x.delete()
        done += 1
    context = {
        'done': done
    }
    return render(request, 'Records/import.html', context)


@login_required(login_url='Core:login_user')
def search2(request):
    instance = get_instance(request)
    results = ''
    search = False
    if request.POST.get('id', 0):
        mobile = request.POST.get('id')
        results = Patient.objects.filter(Q(phone__contains=mobile), instance=instance)
        search = True
    if request.POST.get('name'):
        name = request.POST.get('name', '')
        results = Patient.objects.filter(Q(name__contains=name), instance=instance)
        search = True
    if request.GET.get('q', ''):
        q = request.GET.get('q')
        results = Patient.objects.filter(Q(phone__contains=q) | Q(name__contains=q), instance=instance)
        search = True
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 100)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    context = {
        'results': results,
        'search': search,
    }
    return render(request, 'Records/search.html', context)
