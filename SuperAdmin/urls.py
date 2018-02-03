from django.conf.urls import url
from .views import *


app_name = 'SuperAdmin'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Doctors/$', list_doctors, name='list_doctors'),
    url(r'^Doctors/New/$', register_doctor, name='register_doctor'),
    url(r'^Doctors/(?P<doctor_id>[0-9]+)/$', view_doctor, name='view_doctor'),
    url(r'^Doctors/(?P<doctor_id>[0-9]+)/Edit/$', edit_doctor, name='edit_doctor'),
    url(r'^Doctors/(?P<user_id>[0-9]+)/Password/$', change_user_password, name='change_user_password'),
    url(r'^Resellers/$', list_resellers, name='list_resellers'),
    url(r'^Resellers/New/$', new_reseller, name='new_reseller'),
    url(r'^Resellers/(?P<reseller_id>[0-9]+)/$', view_reseller, name='view_reseller'),
    url(r'^Resellers/(?P<reseller_id>[0-9]+)/Edit/$', edit_reseller, name='edit_reseller'),
    url(r'^Resellers/(?P<reseller_id>[0-9]+)/Delete/$', remove_reseller, name='remove_reseller'),
    url(r'^Resellers/(?P<reseller_id>[0-9]+)/Lock/$', lock_reseller, name='lock_reseller'),
    url(r'^Resellers/(?P<reseller_id>[0-9]+)/Unlock/$', unlock_reseller, name='unlock_reseller'),
    url(r'^Patients/$', list_patients, name='list_patients'),

]