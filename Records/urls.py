from django.conf.urls import url
from .views import *

app_name = 'Records'
urlpatterns = [
    url(r'^Add/$', add_patient, name='add_patient'),
    url(r'^(?P<clinic_id>[0-9]+)/Add/$', add_patient_for_clinic, name='add_patient_for_clinic'),
    url(r'^View/(?P<patient_id>[0-9]+)/$', view_patient, name='view_patient'),
    url(r'^(?P<clinic_id>[0-9]+)/View/(?P<patient_id>[0-9]+)/$', view_patient_for_clinic, name='view_patient_for_clinic'),
    url(r'^(?P<patient_id>[0-9]+)/Records/Add/$', add_record, name='add_record'),
    url(r'^(?P<clinic_id>[0-9]+)/(?P<patient_id>[0-9]+)/Records/Add/$', add_record_for_clinic, name='add_record_for_clinic'),
    url(r'^(?P<record_id>[0-9]+)/Print/$', print_prescription, name='print_prescription'),
    url(r'^Search/$', search2, name='search'),
    url(r'^Delete/(?P<patient_id>[0-9]+)/$', delete_patient, name='delete_patient'),
    url(r'^Setting/CO/New/$', new_co, name='new_co'),
    url(r'^Setting/Medicine/$', list_medicine, name='list_medicine'),
    url(r'^Setting/Medicine/New/$', new_medicine, name='new_medicine'),
    url(r'^Setting/Medicine/(?P<medicine_id>[0-9]+)/Edit/$', edit_medicine, name='edit_medicine'),
    url(r'^Setting/Medicine/(?P<medicine_id>[0-9]+)/Delete/$', delete_medicine, name='delete_medicine'),
    url(r'^API/Medicine/$', get_medicine_api, name='get_medicine_api'),
    url(r'^API/CO/$', get_co_api, name='get_co_api'),
    url(r'^Import/From/CSV/$', import_from_csv, name='import_from_csv'),
    url(r'^Remove/From/CSV/$', remove_my_patients, name='remove_my_patients'),
    url(r'^Import/Medicine/$', import_medicine, name='import_medicine'),
    url(r'^Remove/Medicine/$', remove_medicine, name='remove_medicine'),

]
