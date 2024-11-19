from rest_framework.routers import DefaultRouter
from Apps.Movimientos.Lender.Api_Lender.Lender_Api import LenderViewSet

routerLender = DefaultRouter()

routerLender.register(prefix='Lender',basename='Lender', viewset=LenderViewSet)