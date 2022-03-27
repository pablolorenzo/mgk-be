from django.contrib import admin

# Register your models here.
from .models import ServiceType, BalanceItem, Service, BalanceItemServiceEntry, ServiceStatus

admin.site.register(ServiceType)
admin.site.register(BalanceItem)
admin.site.register(Service)
admin.site.register(BalanceItemServiceEntry)
admin.site.register(ServiceStatus)