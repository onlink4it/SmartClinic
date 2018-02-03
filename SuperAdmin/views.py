# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *
from Core.views import *
from Message.views import *
from Queues.models import *
from Resellers.models import *
from django.shortcuts import render, get_object_or_404, redirect
import os.path
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


# Create your views here.
@login_required(login_url='Core:login_user')
def index(request):
    users = User.objects.all()
    resellers = Instance.objects.filter(is_reseller=True)
    doctors = Instance.objects.filter(is_reseller=False, is_superadmin=False)
    patients = Patient.objects.all()
    medicines = Medicine.objects.all()
    messages = Message.objects.all()
    customer_purchases = CustomerTransaction.objects.all().aggregate(sum=Sum('amount'))
    context = {
        'users': users,
        'resellers': resellers,
        'doctors': doctors,
        'patients': patients,
        'medicines': medicines,
        'messages': messages,
        'customer_purchases': customer_purchases,
    }
    return render(request, 'SuperAdmin/index.html', context)


@login_required(login_url='Core:login_user')
def list_doctors(request):
    doctors = Instance.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(doctors, 5)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    context = {
        'doctors': doctors,
    }
    return render(request, 'SuperAdmin/list_doctors.html', context)


@login_required(login_url='Core:login_user')
def view_doctor(request, doctor_id):
    doctor = get_object_or_404(Instance, id=doctor_id)
    admin = doctor.admin
    assistants = doctor.users.all()
    clinics = Clinic.objects.filter(admin=admin)
    context = {
        'doctor': doctor,
        'admin': admin,
        'assistants': assistants,
        'clinics': clinics,
    }
    return render(request, 'SuperAdmin/view_doctor.html', context)


@login_required(login_url='Core:login_user')
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Instance, id=doctor_id)
    form1 = EditUserForm(request.POST or None, instance=doctor.admin)
    form2 = EditInstanceForm(request.POST or None, instance=doctor)
    forms = [form1, form2]
    if form1.is_valid() and form2.is_valid():
        user = form1.save(commit=True)
        doctor = form2.save(commit=True)
        return redirect('SuperAdmin:list_doctors')
    context = {
        'form1': form1,
        'form2': form2,
        'forms': forms,
        'doctor': doctor,
    }
    return render(request, 'SuperAdmin/multi_form.html', context)


@login_required(login_url='Core:login_user')
def register_doctor(request):
    form1 = EmployeeForm(request.POST or None)
    form2 = InstanceForm(request.POST or None)
    forms = [form1, form2]
    if form1.is_valid() and form2.is_valid():
        user = form1.save(commit=False)
        user.is_staff = True
        user.set_password(user.password)
        user.is_superuser = True
        user.save()
        instance = form2.save(commit=False)
        instance.admin = user
        instance.name = user.username
        instance.reseller = request.user
        instance.expiration = date.today() + timedelta(days=15)
        instance.save()
        message = """<p><strong>Welcome To Smart Clinic&nbsp;</strong></p>
    <p>We are pleased to welcome you as a new customer of <span style="text-decoration: underline;"><strong>ON-Link Smart Clinic</strong></span>. We feel honored that you have chosen us to fill your business needs, and we are eager to be of service.</p>
    <p>Now you can add your Clinics, Employees, and try our system before purchasing your license.</p>
    <p>&nbsp;</p>
    <p>Our friendly, knowledgeable customer service representatives are standing by to explain our additional services and to assist you in getting the most from your telephone service. You may call us at 01066440666. Or you can reply to this message.</p>
    <p>Your complete satisfaction is our first priority! We are delighted that you are a <span style="text-decoration: underline;"><strong>ON-Link</strong></span> customer and look forward to serving you.</p>
    <p>&nbsp;</p>

    """
        sender(User.objects.get(id=1), user, 'Welcome To Smart Clinic', message)
        return redirect('Resellers:index')
    context = {
        'forms': forms
    }
    return render(request, 'SuperAdmin/multi_form.html', context)


@login_required(login_url='Core:login_user')
def change_user_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = ChangePasswordForm(request.POST or None, instance=user)
    title = "Change Password For" + user.username
    if form.is_valid():
        new = form.save(commit=False)
        new.set_password(new.password)
        new.save()
        return redirect('SuperAdmin:list_doctors')
    context = {
        'user': user,
        'form': form,
        'title': title
    }
    return render(request, 'SuperAdmin/form.html', context)


@login_required(login_url='Core:login_user')
def list_resellers(request):
    resellers = Reseller.objects.all()
    context = {
        'resellers': resellers,
    }
    return render(request, 'SuperAdmin/list_resellers.html', context)


@login_required(login_url='Core:login_user')
def new_reseller(request):
    form1 = EmployeeForm(request.POST or None)
    form2 = InstanceForm(request.POST or None)
    form3 = ResellerForm(request.POST or None)
    forms = [form1, form2, form3]
    if form1.is_valid() and form2.is_valid() and form3.is_valid():
        user = form1.save(commit=False)
        user.is_staff = True
        user.set_password(user.password)
        user.is_superuser = True
        user.save()
        instance = form2.save(commit=False)
        instance.admin = user
        instance.name = user.username
        instance.expiration = date.today() + timedelta(days=365)
        instance.is_reseller = True
        instance.save()
        reseller = form3.save(commit=False)
        reseller.user = user
        reseller.save()
        return redirect('SuperAdmin:list_resellers')
    context = {
        'forms': forms
    }
    return render(request, 'SuperAdmin/multi_form.html', context)


@login_required(login_url='Core:login_user')
def view_reseller(request, reseller_id):
    reseller = get_object_or_404(Reseller, id=reseller_id)
    context = {
        'reseller': reseller,
    }
    return render(request, 'SuperAdmin/view_reseller.html', context)


@login_required(login_url='Core:login_user')
def edit_reseller(request, reseller_id):
    reseller = get_object_or_404(Reseller, id=reseller_id)
    form1 = EmployeeForm(request.POST or None, instance=reseller.user)
    form2 = InstanceForm(request.POST or None, instance=reseller.user.instance_admin.all()[0])
    form3 = ResellerForm(request.POST or None, instance=reseller)
    forms = [form1, form2, form3]
    if form1.is_valid() and form2.is_valid() and form3.is_valid():
        user = form1.save(commit=False)
        user.is_staff = True
        user.set_password(user.password)
        user.is_superuser = True
        user.save()
        instance = form2.save(commit=False)
        instance.admin = user
        instance.name = user.username
        instance.expiration = date.today() + timedelta(days=365)
        instance.is_reseller = True
        instance.save()
        reseller = form3.save(commit=False)
        reseller.user = user
        reseller.save()
        return redirect('SuperAdmin:list_resellers')
    context = {
        'forms': forms
    }
    return render(request, 'SuperAdmin/multi_form.html', context)


@login_required(login_url='Core:login_user')
def remove_reseller(request, reseller_id):
    reseller = get_object_or_404(Reseller, id=reseller_id)
    reseller.delete()
    return redirect('SuperAdmin:list_resellers')


@login_required(login_url='Core:login_user')
def lock_reseller(request, reseller_id):
    reseller = get_object_or_404(Reseller, id=reseller_id)
    reseller.user.is_active = False
    reseller.user.save()
    return redirect('SuperAdmin:list_resellers')


@login_required(login_url='Core:login_user')
def unlock_reseller(request, reseller_id):
    reseller = get_object_or_404(Reseller, id=reseller_id)
    reseller.user.is_active = True
    reseller.user.save()
    return redirect('SuperAdmin:list_resellers')


@login_required(login_url='Core:login_user')
def list_patients(request):
    patients = Patient.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(patients, 50)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    context = {
        'patients': patients,
    }
    return render(request, 'SuperAdmin/list_patients.html', context)
