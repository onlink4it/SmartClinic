from django.conf.urls import url
from .views import *

app_name = 'Queues'
urlpatterns = [
    url(r'^Calendar/Search/$', my_calendar, name='my_calendar'),
    url(r'^API/TodayTasks/$', today_tasks_api, name='get_today_tasks'),
    url(r'^API/Queue/$', queues_api, name='get_queue'),
    url(r'^API/TodayTasks/Count/$', get_tasks_count, name='get_tasks_count'),
    url(r'^API/Queue/Count/$', get_queues_count, name='get_queues_count'),
    url(r'^Settings/Employee/(?P<employee_id>[0-9]+)/Permissions/$', employee_auth, name='employee_auth'),
    url(r'^Settings/Clinic/$', list_clinics, name='list_clinics'),
    url(r'^Settings/Clinic/New/$', new_clinic, name='new_clinic'),
    url(r'^Settings/Clinic/(?P<clinic_id>[0-9]+)/Edit/$', edit_clinic, name='edit_clinic'),
    url(r'^Settings/Clinic/(?P<clinic_id>[0-9]+)/Delete/$', delete_clinic, name='delete_clinic'),
    url(r'^Queues/$', queue_home, name='queue_home'),
    url(r'^(?P<clinic_id>[0-9]+)/Today/$', today_calendar_for_clinic, name='today_calendar_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/Assign/$', assign_date_for_clinic, name='assign_date_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/(?P<patient_id>[0-9]+)/Consultation/$', assign_consultant_for_clinic, name='assign_consultant_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/(?P<patient_id>[0-9]+)/Examination/$', assign_examination_for_clinic, name='assign_examination_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/(?P<calendar_id>[0-9]+)/Add_To_Queue/$', add_to_queue_for_clinic, name='add_to_queue_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/(?P<queue_id>[0-9]+)/Remove_From_Queue/$', remove_from_queue_for_clinic, name='remove_from_queue_for_clinic'),
]
