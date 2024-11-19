from rest_framework.routers import DefaultRouter
from Apps.Movimientos.PaymentFrecuency.Api_Payfrecuency.PayFrecuency import PayFrequencyViewSet

routerPaymentFrecuency = DefaultRouter()

routerPaymentFrecuency.register(prefix='PayFrecuency',basename='PayFrecuency', viewset=PayFrequencyViewSet)