# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, datetime
from .models import *
from Core.views import *
from .forms import *
from Accounts.views import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required(login_url='Core:login_user')
def my_calendar(request):
    tasks = ''
    this_day = date.today()
    if request.GET.get('date'):
        this_day = request.GET.get('date')
        f = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
        this_day = datetime.combine(f, datetime.min.time()).date()
        tasks = Calendar.objects.filter(date=this_day, patient__instance=get_instance(request))
    context = {
        'tasks': tasks,
        'this_day': this_day.isoformat(),
    }
    return render(request, 'Queues/calendar.html', context)


@login_required(login_url='Core:login_user')
def today_tasks_api(request):
    today = date.today()
    tasks = Calendar.objects.filter(date=today, patient__instance=get_instance(request))
    queues = Queue.objects.all()
    instance = get_instance(request)
    days_left = instance.get_days_left()
    context = {
        'today': today,
        'tasks': tasks,
        'queues': queues,
        'days_left': days_left,
    }
    return render(request, 'Queues/today_api.html', context)


@login_required(login_url='Core:login_user')
def queues_api(request):
    queues = Queue.objects.filter(done=False, calendar__patient__instance=get_instance(request))
    context = {
        'queues': queues,
    }
    return render(request, 'Queues/queues_api.html', context)


@login_required(login_url='Core:login_user')
def get_queues_count(request):
    count = Queue.objects.filter(done=False, calendar__patient__instance=get_instance(request)).count()
    context = {
        'count': count
    }
    return render(request, 'Queues/count_api.html', context)


@login_required(login_url='Core:login_user')
def get_tasks_count(request):
    count = Calendar.objects.filter(date=date.today(), patient__instance=get_instance(request)).count()
    context = {
        'count': count
    }
    return render(request, 'Queues/count_api.html', context)


@login_required(login_url='Core:login_user')
def list_clinics(request):
    if request.user.is_superuser:
        clinics = Clinic.objects.filter(admin=request.user)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'clinics': clinics,
    }
    return render(request, 'Queues/list_clinics.html', context)


@login_required(login_url='Core:login_user')
def new_clinic(request):
    title = "New Clinic"
    form = ClinicForm(request.POST or None)
    if form.is_valid():
        clinic = form.save(commit=False)
        clinic.admin = request.user
        clinic.save()
        return redirect('Queues:list_clinics')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def edit_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if request.user.is_superuser and clinic.admin == get_instance(request).admin:
        title = "Edit Clinic" + clinic.name
        form = ClinicForm(request.POST or None, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('Queues:list_clinics')
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def delete_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if request.user.is_superuser and clinic.admin == get_instance(request).admin:
        clinic.delete()
    else:
        return render(request, 'Core/permission_error.html')
    return redirect('Queues:list_clinics')


@login_required(login_url='Core:login_user')
def assign_date_for_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if clinic.admin == get_instance(request).admin:
        form = AssignDateForm(request.POST or None)
        form.fields['patient'].queryset = Patient.objects.filter(instance=get_instance(request))
        title = 'Assign Date At: ' + str(date.today())
        if form.is_valid():
            entry = form.save(commit=False)
            entry.date = date.today()
            entry.task_type = 1
            entry.clinic = clinic
            entry.save()
            return redirect('Queues:today_calendar_for_clinic', clinic.id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def today_calendar_for_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if clinic.admin == get_instance(request).admin:
        today = date.today()
        tasks = Calendar.objects.filter(date=today, clinic=clinic)
        queues = Queue.objects.filter(done=False, calendar__clinic=clinic).order_by('id')
        instance = get_instance(request)
        context = {
            'today': today,
            'tasks': tasks,
            'queues': queues,
            'clinic': clinic,
        }
    else:
        return render(request, 'Core/permission_error.html')
    return render(request, 'Queues/today_tasks.html', context)


@login_required(login_url='Core:login_user')
def assign_examination_for_clinic(request, clinic_id, patient_id):
    clinic = get_object_or_404(Clinic, id=clinic_id,)
    patient = get_object_or_404(Queue, id=patient_id)
    if clinic.admin == get_instance(request).admin and patient.calendar.patient.instance == get_instance(request):
        title = 'Assign Examination For: ' + patient.calendar.patient.name
        form = AssignConsultantForm(request.POST or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.patient = patient.calendar.patient
            entry.task_type = 1
            entry.clinic = clinic
            entry.save()
            return remove_from_queue_for_clinic(request, clinic_id, patient_id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'patient': patient,
        'form': form,
        'title': title,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def assign_consultant_for_clinic(request, clinic_id, patient_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    patient = get_object_or_404(Queue, id=patient_id)
    if clinic.admin == get_instance(request).admin and patient.calendar.patient.instance == get_instance(request):
        title = 'Assign Consultation For: ' + patient.calendar.patient.name
        form = AssignConsultantForm(request.POST or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.patient = patient.calendar.patient
            entry.task_type = 2
            entry.clinic = clinic
            entry.save()
            return remove_from_queue_for_clinic(request, clinic_id, patient_id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'patient': patient,
        'form': form,
        'title': title
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def add_to_queue_for_clinic(request, clinic_id, calendar_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    calendar = get_object_or_404(Calendar, id=calendar_id)

    if clinic.admin == get_instance(request).admin and calendar.patient.instance == get_instance(request):
        title = "تحديد دور  " + str(calendar.patient.name) + " - "
        if calendar.task_type == 1:
            title += "كشف جديد"
            form = QueueForm(request.POST or None, initial={'paid': clinic.examination_fees})
        elif calendar.task_type == 2:
            title += "إعادة كشف"
            form = QueueForm(request.POST or None, initial={'paid': clinic.consultant_fees})
        if form.is_valid():
            queue = form.save(commit=False)
            queue.calendar = calendar
            queue.save()
            add_transaction(clinic=calendar.clinic, by=request.user, income=queue.paid, comment=str(calendar.get_type()) + ' - ' + str(calendar.patient.name))
            return redirect('Queues:today_calendar_for_clinic', clinic.id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'calendar': calendar,
        'form': form,
        'title': title,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def remove_from_queue_for_clinic(request, clinic_id, queue_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    queue = get_object_or_404(Queue, id=queue_id)
    if clinic.admin == get_instance(request).admin and queue.calendar.patient.instance == get_instance(request):
        queue.done = True
        queue.save()
        return redirect('Queues:today_calendar_for_clinic', clinic.id)
    else:
        return render(request, 'Core/permission_error.html')


@login_required(login_url='Core:login_user')
def my_calendar_for_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if clinic.admin == get_instance(request).admin:
        tasks = ''
        this_day = date.today()
        if request.GET.get('date'):
            this_day = request.GET.get('date')
            f = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
            this_day = datetime.combine(f, datetime.min.time()).date()
            tasks = Calendar.objects.filter(date=this_day, clinic=clinic)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'tasks': tasks,
        'this_day': this_day.isoformat(),
    }
    return render(request, 'Queues/calendar.html', context)


@login_required(login_url='Core:login_user')
def queue_home(request):
    user = request.user
    if user.is_superuser:
        clinics = Clinic.objects.filter(admin=user)
    else:
        clinics = Clinic.objects.filter(employeeauth__employee=request.user)
    context = {'clinics': clinics}
    return render(request, 'Queues/queue_home.html', context)


@login_required(login_url='Core:login_user')
def employee_auth(request, employee_id):
    employee = get_object_or_404(User, id=employee_id)
    if request.user.is_superuser and employee in get_instance(request).users.all():
        title = "Edit Permissions For: " + employee.username + ' - ' + employee.get_full_name()
        record = EmployeeAuth.objects.get_or_create(employee=employee)
        record = get_object_or_404(EmployeeAuth, employee=employee)
        form = ClinicAuthForm(request.POST or None, instance=record)
        form.fields['allowed_clinic'].queryset = Clinic.objects.filter(admin=get_instance(request).admin)
        if form.is_valid():
            form.save()
            return redirect('Core:list_employees')
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'title': title,
        'employee': employee,
        'record': record,
        'form': form,
    }
    return render(request, 'Core/form.html', context)