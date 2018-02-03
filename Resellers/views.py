from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from Core.views import *
from datetime import timedelta, datetime, date
from .forms import *
from dateutil.relativedelta import relativedelta


# Create your views here.
@login_required(login_url='Core:login_user')
def index(request):
    active = 0
    non_active = 0
    expire_soon = 0
    for x in request.user.Reseller.all():
        if x.is_active():
            active += 1
            if x.expire_soon():
                expire_soon += 1
        else:
            non_active += 1
    context = {
        'active': active,
        'non_active': non_active,
        'expire_soon': expire_soon,
    }
    return render(request, 'Resellers/index.html', context)


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
    return render(request, 'Resellers/register_doctor.html', context)


@login_required(login_url='Core:login_user')
def list_doctors(request):
    doctors = Instance.objects.filter(reseller=request.user)
    context = {
        'doctors': doctors
    }
    return render(request, 'Resellers/list_doctors.html', context)


@login_required(login_url='Core:login_user')
def view_doctor(request, doctor_id):
    doctor = get_object_or_404(Instance, id=doctor_id)
    size = 0
    for x in doctor.patient_set.all():
        if x.laprospic_report:
            size += x.laprospic_report.size
    context = {
        'doctor': doctor,
        'size': size,
    }
    return render(request, 'Resellers/view_doctor.html', context)


@login_required(login_url='Core:login_user')
def renew_subscription(request, doctor_id):
    doctor = get_object_or_404(Instance, id=doctor_id)
    services = Service.objects.filter(enabled=True)
    context = {
        'doctor': doctor,
        'services': services,
    }
    return render(request, 'Resellers/choose_service.html', context)


@login_required(login_url='Core:login_user')
def confirm_renewal(request, doctor_id, service_id):
    doctor = get_object_or_404(Instance, id=doctor_id)
    service = get_object_or_404(Service, id=service_id)
    new_expiration = doctor.expiration + relativedelta(months=service.months_to_add)
    form = ChooseServiceForm(request.POST or None)
    if form.is_valid():
        customer_transaction = form.save(commit=False)
        customer_transaction.instance = doctor
        customer_transaction.service = service
        customer_transaction.done_by = request.user
        customer_transaction.amount = service.price
        customer_transaction.save()
        doctor.payments += 1
        doctor.expiration = new_expiration
        doctor.save()
        reseller_transaction = ResellerTransaction()
        reseller_transaction.customer_transaction = customer_transaction
        reseller_transaction.reseller = request.user
        if doctor.payments >= 1:
            reseller_transaction.amount = -(service.price - (
                service.price * request.user.reseller_set.all()[0].percentage_on_first / 100))
        else:
            reseller_transaction.amount = -(service.price - (
                service.price * request.user.reseller_set.all()[0].percentage_on_renewal / 100))
        reseller_transaction.comment = "Invoice " + str(customer_transaction.id)
        reseller_transaction.save()
        reseller = request.user.reseller_set.all()[0]
        reseller.credit += reseller_transaction.amount
        reseller.save()

        return redirect('Resellers:print_receipt', customer_transaction.id)
    context = {
        'doctor': doctor,
        'service': service,
        'new_expiration': new_expiration,
        'form': form,
    }
    return render(request, 'Resellers/confirm_renewal.html', context)


@login_required(login_url='Core:login_user')
def print_customer_receipt(request, trans_id):
    trans = get_object_or_404(CustomerTransaction, id=trans_id)
    context = {
        'trans': trans
    }
    return render(request, 'Resellers/print_receipt.html', context)


@login_required(login_url='Core:login_user')
def billing(request):
    reseller = request.user.reseller_set.all()[0]
    transactions = request.user.resellertransaction_set.all()
    context = {
        'reseller': reseller,
        'transactions': transactions,
    }
    return render(request, 'Resellers/billing.html', context)


@login_required(login_url='Core:login_user')
def choose_specialty(request):
    instance = get_instance(request)
    form = ChooseSpecialtyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('Core:index')
    context = {
        'form': form,
    }
    return render(request, 'Core/form.html', context)


@login_required(login_url='Core:login_user')
def api_get_expire_soon(request):
    doctors = Instance.objects.filter(reseller=request.user,
                                      expiration__range=[date.today(), date.today() + timedelta(days=15)])
    return render(request, 'Resellers/API/get_expire_soon.html', context={'doctors': doctors})


@login_required(login_url='Core:login_user')
def api_get_expire_soon_count(request):
    doctors = Instance.objects.filter(reseller=request.user,
                                      expiration__range=[date.today(), date.today() + timedelta(days=15)]).count()
    return render(request, 'Resellers/API/get_count.html', context={'doctors': doctors})


@login_required(login_url='Core:login_user')
def api_get_recent_expired(request):
    doctors = Instance.objects.filter(reseller=request.user,
                                      expiration__range=[date.today() - timedelta(days=15), date.today()])
    return render(request, 'Resellers/API/get_recent_expired.html', context={'doctors': doctors})


@login_required(login_url='Core:login_user')
def api_get_recent_expired_count(request):
    doctors = Instance.objects.filter(reseller=request.user,
                                      expiration__range=[date.today() - timedelta(days=15), date.today()]).count()
    return render(request, 'Resellers/API/get_count.html', context={'doctors': doctors})
