# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from datetime import datetime, timedelta
from Message.views import *


# Create your views here.
@login_required(login_url='Core:login_user')
def index(request):
    get_instance(request)
    return redirect('Queues:queue_home')


@login_required(login_url='Core:login_user')
def update_online(request):
    Online.objects.get_or_create(user=request.user)
    online_record = Online.objects.get(user=request.user)
    online_record.last_update = datetime.now(tz=None)
    online_record.save()
    return HttpResponse('True')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                if user.is_active:
                    login(request, user)
                    if request.POST['next']:
                        return redirect(request.POST.get('next'), '/')
                    else:
                        return redirect('Core:index')
                else:
                    return render(request, 'Core/login.html', {'error_message': 'تم إيقاف الحساب الخاص بك'})
            else:
                return render(request, 'Core/permission_error.html',
                              {'message': 'غير مسموح لك بالتواجد داخل هذه الصفحة!'})
        else:
            return render(request, 'Core/login.html', {'error_message': 'برجاء التأكد من اسم المستخدم وكلمة السر'})
    return render(request, 'Core/login.html')


def logout_user(request):
    logout(request)
    return redirect('Core:login_user')


@login_required(login_url='Core:login_user')
def change_password(request):
    user = request.user
    form = ChangePasswordForm(request.POST or None, instance=user)
    title = "تغيير كلمة المرور لـ" + user.username
    if form.is_valid():
        new = form.save(commit=False)
        new.set_password(new.password)
        new.save()
        return redirect('Core:index')
    context = {
        'user': user,
        'form': form,
        'title': title
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def get_instance(request):
    user = request.user
    try:
        instance = Instance.objects.get(admin=user)
    except:
        instance = Instance.objects.get(users__username__exact=user)
    return instance


@login_required(login_url='Core:login_user')
def new_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_staff = True
        user.set_password(user.password)
        user.save()
        instance = get_instance(request)
        instance.users.add(user)
        return redirect('Core:list_employees')
    context = {
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def list_employees(request):
    instance = get_instance(request)
    employees = instance.users.all()
    context = {
        'employees': employees
    }
    return render(request, 'Core/list_employees.html', context)


@login_required(login_url='Core:login_user')
def edit_employee(request, employee_id):
    employee = get_object_or_404(User, id=employee_id)
    if request.user.is_superuser and employee in get_instance(request).users.all():
        form = EmployeeForm(request.POST or None, instance=employee)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.set_password(user.password)
            user.save()
            instance = get_instance(request)
            instance.users.add(user)
            return redirect('Core:list_employees')
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'form': form,
    }
    return render(request, 'Core/form.html', context)


def register(request):
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
        login(request, user)
        return redirect('Queues:new_clinic')
    context = {
        'forms': forms
    }
    return render(request, 'Core/register.html', context)


@login_required(login_url='Core:login_user')
def login_as(request, user_id):
    instance = get_instance(request)
    if instance.is_superadmin:
        user = get_object_or_404(User, id=user_id)
        login(request, user)
        return redirect('Core:index')
