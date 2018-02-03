from django.conf.urls import url
from .views import *

app_name = 'Resellers'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^New/Doctor/$', register_doctor, name='register_doctor'),
    url(r'^List/Doctors/$', list_doctors, name='list_doctors'),
    url(r'^View/Doctor/(?P<doctor_id>[0-9]+)/$', view_doctor, name='view_doctor'),
    url(r'^Renew/Doctor/(?P<doctor_id>[0-9]+)/$', renew_subscription, name='renew_subscription'),
    url(r'^Renew/Doctor/(?P<doctor_id>[0-9]+)/Confirm/(?P<service_id>[0-9]+)/$', confirm_renewal, name='confirm_renewal'),
    url(r'^Customer/Transactions/(?P<trans_id>[0-9]+)/Print$', print_customer_receipt, name='print_receipt'),
    url(r'^Billing/$', billing, name='billing'),
    url(r'^Specialty/$', choose_specialty, name='choose_specialty'),
    url(r'^API/get_expire_soon/$', api_get_expire_soon, name='api_get_expire_soon'),
    url(r'^API/get_expire_soon/count/$', api_get_expire_soon_count, name='api_get_expire_soon_count'),
    url(r'^API/get_recent_expired/$', api_get_recent_expired, name='api_get_recent_expired'),
    url(r'^API/get_recent_expired/count/$', api_get_recent_expired_count, name='api_get_recent_expired_count'),
]
