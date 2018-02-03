from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Reseller)
admin.site.register(ResellerTransaction)
admin.site.register(Service)
admin.site.register(CustomerTransaction)