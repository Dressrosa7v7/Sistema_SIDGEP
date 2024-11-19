from rest_framework.routers import DefaultRouter
from Apps.Movimientos.PaymentStatus.Api_PayStatus.PayStatus import PaymentStatusViewSet

routerPaymentStatus = DefaultRouter()

routerPaymentStatus.register(prefix='PayStatus', viewset=PaymentStatusViewSet, basename='PayStatus')