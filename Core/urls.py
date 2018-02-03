# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *
app_name = 'Core'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Register/$', register, name='register'),
    url(r'^login/$', login_user, name='login_user'),
    url(r'^logout/$', logout_user, name='logout_user'),
    url(r'^change_password/$', change_password, name='change_password'),
    url(r'^login_as/(?P<user_id>[0-9]+)/$', login_as, name='login_as'),
    url(r'^stay_alive/$', update_online, name='update_online'),
    url(r'^Employees/$', list_employees, name='list_employees'),
    url(r'^Employees/(?P<employee_id>[0-9]+)/Edit/$', edit_employee, name='edit_employee'),
    url(r'^Employees/New/$', new_employee, name='new_employee'),
]