from rest_framework.routers import DefaultRouter
from Apps.Movimientos.Payment.Api_Payment.Payment_Api import PaymentViewSet

routerPayment = DefaultRouter()

routerPayment.register(prefix='Payment',basename='Payment', viewset=PaymentViewSet)