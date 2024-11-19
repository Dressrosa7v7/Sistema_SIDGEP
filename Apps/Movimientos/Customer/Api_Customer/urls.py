from Apps.Movimientos.Customer.Api_Customer.Customer_Api import CustomerViewSet
from rest_framework.routers import DefaultRouter

routerCustomer = DefaultRouter()

routerCustomer.register(prefix='Customer', basename='Customer', viewset=CustomerViewSet)