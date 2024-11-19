from rest_framework.routers import DefaultRouter
from Apps.Movimientos.Loans.Api_Loans.Loans_Api import LoansViewSet

routerLoans = DefaultRouter()

routerLoans.register(prefix='Loans',basename='Loans', viewset=LoansViewSet )