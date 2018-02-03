# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import *
from Core.views import *
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def add_transaction(clinic, by, income=0, outcome=0, comment=''):
    trans = MoneyTransaction()
    trans.income = income
    trans.outcome = outcome
    trans.comment = comment
    trans.clinic = clinic
    trans.done_by = by
    trans.save()
    employee_transaction = EmployeeTransaction()
    employee_transaction.amount = income - outcome
    employee_transaction.comment = comment
    employee_transaction.employee = by
    employee_transaction.save()


@login_required(login_url='Core:login_user')
def add_expense_for_clinic(request, clinic_id):
    title = 'Add Expense'
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if clinic.admin == get_instance(request).admin:
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.clinic = clinic
            expense.done_by = request.user
            expense.save()
            emp_trans = EmployeeTransaction()
            emp_trans.amount = -expense.outcome
            emp_trans.comment = expense.comment
            emp_trans.employee = request.user
            emp_trans.save()
            return redirect('Queues:today_calendar_for_clinic', clinic.id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'title': title,
        'clinic': clinic,
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def add_income_for_clinic(request, clinic_id):
    title = 'Add Income'
    clinic = get_object_or_404(Clinic, id=clinic_id)
    if clinic.admin == get_instance(request).admin:
        form = IncomeForm(request.POST or None)
        if form.is_valid():
            income = form.save(commit=False)
            income.clinic = clinic
            income.done_by = request.user
            income.save()
            emp_trans = EmployeeTransaction()
            emp_trans.amount = income.outcome
            emp_trans.comment = income.comment
            emp_trans.employee = request.user
            emp_trans.save()
            return redirect('Queues:today_calendar_for_clinic', clinic.id)
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'title': title,
        'clinic': clinic,
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def reports(request):
    if request.user.is_superuser:
        default_from = date.today().replace(day=1)
        today = date.today()
        clinics = Clinic.objects.filter(admin=request.user)
        if request.POST.get('from_date'):
            f = datetime.strptime(request.POST.get('from_date'), '%Y-%m-%d')
            from_date = datetime.combine(f, datetime.min.time()).date()
        else:
            from_date = default_from
        if request.POST.get('to_date'):
            t = datetime.strptime(request.POST.get('to_date'), '%Y-%m-%d')
            to_date = datetime.combine(t, datetime.max.time()).date()
        else:
            to_date = today
        if request.POST.getlist('clinic'):
            clinic = get_list_or_404(Clinic, id__in=request.POST.getlist('clinic'))
            for x in clinic:
                if x.admin == get_instance(request).admin:
                    pass
                else:
                    return render(request, 'Core/permission_error.html')
        else:
            clinic = get_list_or_404(Clinic, admin=request.user)
        report = MoneyTransaction.objects.filter(date__range=(from_date, to_date), clinic__in=clinic)
        detailed = report.aggregate(income=Sum('income'), outcome=Sum('outcome'), total=Sum('income') - Sum('outcome'))
        context = {
            'report': report,
            'detailed': detailed,
            'from_date': from_date.isoformat(),
            'to_date': to_date.isoformat(),
            'clinic': clinic,
            'clinics': clinics,
        }
        return render(request, 'Accounts/report.html', context)
    else:
        return render(request, 'Core/permission_error.html')


@login_required(login_url='Core:login_user')
def employee_balance(request):
    employees = Instance.objects.get(admin=request.user).users.all()
    context = {'employees': employees}
    if request.POST.get('employee'):
        employee = get_object_or_404(User, id=request.POST.get('employee'))
        if employee in get_instance(request).users.all() and request.user.is_superuser:
            report = EmployeeTransaction.objects.filter(employee=employee)
            balance = report.aggregate(balance=Sum('amount'))
            context.update({'employee': employee, 'report': report, 'balance': balance})
        else:
            return render(request, 'Core/permission_error.html')
    return render(request, 'Accounts/employee_report.html', context)


@login_required(login_url='Core:login_user')
def withdraw_cash_from_employee(request, employee_id):
    employee = get_object_or_404(User, id=employee_id)
    if employee in get_instance(request).users.all() and request.user.is_superuser:
        report = EmployeeTransaction.objects.filter(employee=employee)
        balance = report.aggregate(balance=Sum('amount'))
        title = 'Withdraw Cash From: ' + str(employee) + ' - ' + str(balance)
        form = EmployeeTransactionForm(request.POST or None)
        if form.is_valid():
            emp_trans = form.save(commit=False)
            amount = emp_trans.amount
            emp_trans.amount = -amount
            emp_trans.employee = employee
            emp_trans.comment = "Withdrawal"
            emp_trans.save()
            admin_trans = EmployeeTransaction()
            admin_trans.amount = amount
            admin_trans.employee = request.user
            admin_trans.comment = "Withdrawal From " + str(employee)
            admin_trans.save()
            return redirect('Accounts:employee_balance')
    else:
        return render(request, 'Core/permission_error.html')
    context = {
        'title': title,
        'employee': employee,
        'form': form,
    }
    return render(request, 'Core/form.html', context)
