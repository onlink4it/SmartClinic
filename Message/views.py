# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from datetime import datetime, date
from Core.models import Instance


# Create your views here.
@login_required(login_url='Core:login_user')
def inbox(request):
    user = request.user
    messages = Message.objects.filter(receiver=user)
    context = {
        'messages': messages,
    }
    return render(request, 'Message/new_inbox.html', context)


def sender(sender, receiver, title, message):
    msg = Message(sender=sender, receiver=receiver, title=title, body=message)
    msg.save()
    return msg


@login_required(login_url='Core:login_user')
def send_message(request):
    form1 = SendMessageForm(request.POST or None, request.FILES or None)
    form2 = MessageAttachmentsForm(request.POST or None, request.FILES or None)
    try:
        instance = Instance.objects.get(admin=request.user)
    except:
        instance = Instance.objects.get(users__username__exact=request.user)
    employees = instance.users.all()
    master = instance.admin
    forms = {'': form1, 'Attachments': form2}
    if request.POST.getlist('receiver', 0):
        msg_list = request.POST.getlist('receiver', '')
        if form1.is_valid() and form2.is_valid():
            for x in msg_list:
                msg = form1.save(commit=False)
                attachment = form2.save(commit=False)
                receiver = get_object_or_404(User, id=int(x))
                z = sender(request.user, receiver, msg.title, msg.body)
                if attachment.attachment:
                    for y in request.FILES.getlist('attachment', ''):
                        new = Attachments()
                        new.attachment = y
                        new.msg = z
                        new.save()
            return redirect('Message:inbox')
    context = {
        'forms': forms.items(),
        'employees': employees,
        'form1': form1,
        'master': master,
    }
    return render(request, 'Message/new_send_message.html', context)


@login_required(login_url='Core:login_user')
def read_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if not message.read:
        if request.user == message.receiver:
            message.read = True
            message.read_at = datetime.now()
            message.save()
    context = {
        'message': message,
    }
    return render(request, 'Message/new_view_message.html', context)


@login_required(login_url='Core:login_user')
def send_to_all(request):
    form1 = SendMessageForm(request.POST or None, request.FILES or None)
    form2 = MessageAttachmentsForm(request.POST or None, request.FILES or None)
    employees = User.objects.filter(is_staff=True)
    forms = {'Message': form1, 'Attachments': form2}
    if form1.is_valid() and form2.is_valid():
        for x in User.objects.filter(is_staff=True):
            msg = form1.save(commit=False)
            attachment = form2.save(commit=False)
            receiver = x
            z = sender(request.user, receiver, msg.title, msg.body)
            if attachment.attachment:
                for y in request.FILES.getlist('attachment', ''):
                    new = Attachments()
                    new.attachment = y
                    new.msg = z
                    new.save()
        return redirect('Message:inbox')
    context = {
        'forms': forms.items(),
        'employees': employees,
        'form1': form1,
    }
    return render(request, 'Message/send_to_all.html', context)


@login_required(login_url='Core:login_user')
def send_to_group(request):
    form1 = SendMessageForm(request.POST or None, request.FILES or None)
    form2 = MessageAttachmentsForm(request.POST or None, request.FILES or None)
    employees = Group.objects.all()
    forms = {'Message': form1, 'Attachments': form2}
    if request.POST.getlist('group', 0):
        msg_list = request.POST.getlist('group', '')
        if form1.is_valid() and form2.is_valid():
            for x in msg_list:
                print(x)
                msg = form1.save(commit=False)
                attachment = form2.save(commit=False)
                receiver = get_object_or_404(Group, id=int(x))
                for u in User.objects.filter(is_staff=True, groups=receiver):
                    z = sender(request.user, u, msg.title, msg.body)
                    if attachment.attachment:
                        for y in request.FILES.getlist('attachment', ''):
                            new = Attachments()
                            new.attachment = y
                            new.msg = z
                            new.save()
                return redirect('Message:inbox')
    context = {
        'forms': forms.items(),
        'employees': employees,
        'form1': form1,
    }
    return render(request, 'Message/send_to_group.html', context)


@login_required(login_url='Core:login_user')
def reply(request, message_id):
    msg = get_object_or_404(Message, id=message_id)
    form1 = ReplyMessageForm(request.POST or None, request.FILES or None)
    form2 = MessageAttachmentsForm(request.POST or None, request.FILES or None)
    form1.fields[
        'body'].initial = '<br><br><hr>' + '<p><strong>From: </strong>' + msg.sender.get_full_name() + '</p><p><strong>To:</strong>' + msg.receiver.get_full_name() + '</p><p><strong>Date:</strong>' + str(
        msg.date) + '</p>' + msg.body
    employees = User.objects.filter(is_staff=True)
    forms = {'': form1, 'Attachments': form2}
    if request.POST.getlist('receiver', 0):
        msg_list = request.POST.getlist('receiver', '')
        if form1.is_valid() and form2.is_valid():
            for x in msg_list:
                msg = form1.save(commit=False)
                attachment = form2.save(commit=False)
                msg.title = request.POST.get('title', '')
                receiver = get_object_or_404(User, id=int(x))
                z = sender(request.user, receiver, msg.title, msg.body)
                if attachment.attachment:
                    for y in request.FILES.getlist('attachment', ''):
                        new = Attachments()
                        new.attachment = y
                        new.msg = z
                        new.save()
            return redirect('Message:inbox')
    context = {
        'msg': msg,
        'forms': forms.items(),
        'employees': employees,
        'form1': form1,
    }
    return render(request, 'Message/new_reply.html', context)


@login_required(login_url='Core:login_user')
def forward(request, message_id):
    msg = get_object_or_404(Message, id=message_id)
    form1 = ForwardMessageForm(request.POST or None, request.FILES or None)
    form2 = MessageAttachmentsForm(request.POST or None, request.FILES or None)
    form1.fields[
        'body'].initial = '<br><br><hr>' + '<p><strong>From: </strong>' + msg.sender.get_full_name() + '</p><p><strong>To:</strong>' + msg.receiver.get_full_name() + '</p><p><strong>Date:</strong>' + str(
        msg.date) + '</p>' + msg.body
    try:
        instance = Instance.objects.get(admin=request.user)
    except:
        instance = Instance.objects.get(users__username__exact=request.user)
    employees = instance.users.all()
    forms = {'Message': form1, 'Attachments': form2}
    if request.POST.getlist('receiver', 0):
        msg_list = request.POST.getlist('receiver', '')
        if form1.is_valid() and form2.is_valid():
            for x in msg_list:
                new_msg = form1.save(commit=False)
                attachment = form2.save(commit=False)
                new_msg.title = request.POST.get('title', '')
                receiver = get_object_or_404(User, id=int(x))
                z = sender(request.user, receiver, 'FW:' + msg.title, new_msg.body)
                if attachment.attachment:
                    for y in request.FILES.getlist('attachment', ''):
                        new = Attachments()
                        new.attachment = y
                        new.msg = z
                        new.save()
            return redirect('Message:inbox')
    context = {
        'msg': msg,
        'forms': forms.items(),
        'employees': employees,
        'form1': form1,
    }
    return render(request, 'Message/new_forward.html', context)


@login_required(login_url='Core:login_user')
def list_sent(request):
    user = request.user
    messages = Message.objects.filter(sender=user)
    context = {
        'messages': messages,
    }
    return render(request, 'Message/new_outbox.html', context)


@login_required(login_url='Core:login_user')
def all_messages(request):
    this_day = date.today()
    default_from = this_day.replace(day=1)
    if request.GET.get('from_date'):
        f = datetime.strptime(request.GET.get('from_date'), '%Y-%m-%d')
        from_date = datetime.combine(f, datetime.min.time())
    else:
        from_date = datetime.combine(default_from, datetime.min.time())
    if request.GET.get('to_date'):
        t = datetime.strptime(request.GET.get('to_date'), '%Y-%m-%d')
        to_date = datetime.combine(t, datetime.max.time())
    else:
        to_date = datetime.combine(this_day, datetime.max.time())
    messages = Message.objects.filter(date__range=(from_date, to_date))
    context = {
        'messages': messages,
        'this_day': this_day.isoformat(),
        'default_from': default_from.isoformat(),
    }
    return render(request, 'Message/all_messages.html', context)


@login_required(login_url='Core:login_user')
def unread_message(request):
    user = request.user
    unread = Message.objects.filter(receiver=user, read=False).count()
    if unread > 0:
        text = str(unread)
        new = True
    else:
        text = str(unread)
        new = False
    context = {
        'text': text,
        'new': new,
    }
    return render(request, 'Message/unread_notification.html', context)


@login_required(login_url='Core:login_user')
def latest_msgs(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-id')[:5]
    context = {
        'messages': messages
    }
    return render(request, 'Message/latest_messages.html', context)

