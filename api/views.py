# views.py
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ServiceStatusSerializer, ServiceTypeSerializer, ServiceSerializer, BalanceItemSerializer, BalanceItemServiceEntrySerializer, BalanceItemServiceEntrySerializerID
from index.models import ServiceType, ServiceStatus, Service, BalanceItem, BalanceItemServiceEntry
from .filters import ServiceFilter 

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ServiceStatusViewSet(viewsets.ModelViewSet):
    queryset = ServiceStatus.objects.all().order_by('status')
    serializer_class = ServiceStatusSerializer

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all().order_by('service_type')
    serializer_class = ServiceTypeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer

class BalanceItemViewSet(viewsets.ModelViewSet):
    queryset = BalanceItem.objects.all().order_by('id')
    serializer_class = BalanceItemSerializer
    
class BalanceItemServiceEntryViewSet(viewsets.ModelViewSet):
    queryset = BalanceItemServiceEntry.objects.all().order_by('id')
    serializer_class = BalanceItemServiceEntrySerializerID

class ServicesViewSetAlt(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'provider_id', 'status_id']
    search_fields = ['=address']
    ordering_fields = ['status_id', 'id']
    ordering = ['id']
    serializer_class=ServiceSerializer
    pagination_class = StandardResultsSetPagination
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
        else:    
            serializer = ServiceSerializer(queryset, many=True)
        print(serializer.data)
        output = []
        for item in serializer.data:
            print("000000000000000000000000000000000000000000000200000")
            print(item['id'])
            copied_object = {}
            copied_object.update(item)
            balance_items = BalanceItemServiceEntry.objects.filter(service_id=item['id'])
            if balance_items:
                balance_items = BalanceItemServiceEntrySerializer(balance_items, many=True).data
            gastos = []
            ingresos = []
            balance = 0
            for balance_item in balance_items:
                print(balance_item['sign'])
                if balance_item['sign'] == '-':
                    gastos.append(balance_item)
                    balance -= balance_item['value']
                else:
                    ingresos.append(balance_item)
                    balance += balance_item['value']
            print(gastos)
            print(ingresos)
            print(balance)
            copied_object['gastos'] = gastos
            copied_object['ingresos'] = ingresos
            copied_object['balance'] = balance
            output.append(copied_object)
        
        return self.get_paginated_response(output)

    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)