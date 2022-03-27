from django.utils.translation import gettext_lazy as _
from django.db import models


class ServiceType(models.Model):
    service_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.service_type


class ServiceStatus(models.Model):
    status = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.status


class Service(models.Model):
    address = models.CharField(max_length=200)
    provider_id = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    status_id = models.ForeignKey(ServiceStatus, on_delete=models.CASCADE)
    started_date = models.DateField(null=True)
    finished_date = models.DateField(null=True)

    def __str__(self):
        return self.address


class BalanceItem(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
    
    
    
class BalanceItemServiceEntry(models.Model):
    class BalanceSign(models.TextChoices):
        POSITIVE = '+', _('POSITIVE')
        NEGATIVE = '-', _('NEGATIVE')
    
    sign = models.CharField(
      max_length=2,
      choices=BalanceSign.choices
    )
    item_type = models.ForeignKey(BalanceItem, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    note = models.CharField(max_length=1500)
    value = models.FloatField()
