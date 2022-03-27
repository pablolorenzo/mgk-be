import django_filters
from index.models import *

class ServiceFilter(django_filters.rest_framework.FilterSet):
  """
     Filtro de servidor físico
  """
  address = django_filters.CharFilter(name='address', lookup_expr='icontains')
  provider_id = django_filters.NumberFilter(name='provider_id')
  status_id = django_filters.NumberFilter(name='status_id')
  started_date = django_filters.DateFilter(
        'started_date', label='With start date',
        lookup_type='contains' # use contains
    )
  finished_date = django_filters.DateFilter(
        'finished_date', label='With end date',
        lookup_type='contains' # use contains
    )

  class Meta:
    model = Service
    fields = ['address', 'provider_id', 'status_id', 'started_date', 'finished_date' ]