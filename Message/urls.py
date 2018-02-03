# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

app_name = 'Message'
urlpatterns = [
    url(r'^$', inbox, name='inbox'),
    url(r'^All/$', all_messages, name='all_messages'),
    url(r'^Send/$', send_message, name='send_message'),
    url(r'^Sent/$', list_sent, name='outbox'),
    url(r'^Broadcast$', send_to_all, name='send_to_all'),
    url(r'^View/(?P<message_id>[0-9]+)/$', read_message, name='read_message'),
    url(r'^View/(?P<message_id>[0-9]+)/Reply/$', reply, name='reply'),
    url(r'^View/(?P<message_id>[0-9]+)/Forward/$', forward, name='forward'),
    url(r'^Send/Group/$', send_to_group, name='send_to_group'),
    url(r'^API/Unread/$', unread_message, name='get_unread_count'),
    url(r'^API/Latest/$', latest_msgs, name='get_latest_messages'),
]
