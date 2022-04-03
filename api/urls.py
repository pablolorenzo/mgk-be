# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views

router = routers.DefaultRouter()
router.register(r'service-status', views.ServiceStatusViewSet)
router.register(r'service-type', views.ServiceTypeViewSet)
router.register(r'services-alt', views.ServicesViewSetAlt)
router.register(r'services', views.ServicesViewSet)
router.register(r'balance-item', views.BalanceItemViewSet)
router.register(r'balance-item-service', views.BalanceItemServiceEntryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

