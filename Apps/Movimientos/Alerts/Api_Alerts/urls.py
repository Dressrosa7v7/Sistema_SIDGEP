from rest_framework.routers import DefaultRouter
from Apps.Movimientos.Alerts.Api_Alerts.Alerts_Api import AlertsViewSet

routerAlerts = DefaultRouter()

routerAlerts.register(prefix='Alerts',basename='Alerts', viewset=AlertsViewSet)