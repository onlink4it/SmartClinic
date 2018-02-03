from django.conf.urls import url
from .views import *

app_name = 'Accounts'
urlpatterns = [
    url(r'^(?P<clinic_id>[0-9]+)/Expense/New/$', add_expense_for_clinic, name='add_expense_for_clinic'),
    url(r'^(?P<clinic_id>[0-9]+)/Income/New/$', add_income_for_clinic, name='add_income_for_clinic'),
    url(r'^Reports/$', reports, name='reports'),
    url(r'^Reports/Employee/$', employee_balance, name='employee_balance'),
    url(r'^Accounts/Employee/(?P<employee_id>[0-9]+)/Withdraw/$', withdraw_cash_from_employee, name='withdraw_cash_from_employee'),
]