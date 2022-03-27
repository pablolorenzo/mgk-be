from rest_framework import serializers

from index.models import ServiceType, ServiceStatus, Service, BalanceItem, BalanceItemServiceEntry

class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('service_type', 'pub_date', 'id')

class BalanceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BalanceItem
        fields = ('name', 'pub_date', 'id')


class ServiceStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceStatus
        fields = ('status', 'pub_date', 'id')
  
class ServiceSerializer(serializers.ModelSerializer):
    #status_id = ServiceStatusSerializer(many=False, read_only=False)
    ###provider_id = ServiceTypeSerializer(many=False, read_only=False)
    class Meta:
        model = Service
        fields = ('id', 'address', 'status_id','provider_id', 'started_date', 'finished_date')

class BalanceItemServiceEntrySerializer(serializers.ModelSerializer):
    item_type = BalanceItemSerializer(many=False, read_only=False)
    class Meta:
        model = BalanceItemServiceEntry
        fields = ('id', 'sign', 'item_type', 'service_id', 'value')

class BalanceItemServiceEntrySerializerID(serializers.ModelSerializer):
    class Meta:
        model = BalanceItemServiceEntry
        fields = ('id', 'sign', 'item_type', 'service_id', 'value')