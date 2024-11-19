"""Confi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Apps.Catalogos.Person.Api_Person.urls import routerPerson
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Apps.Movimientos.Alerts.Api_Alerts.urls import routerAlerts
from Apps.Movimientos.Customer.Api_Customer.urls import routerCustomer
from Apps.Movimientos.Lender.Api_Lender.urls import routerLender
from Apps.Movimientos.Loans.Api_Loans.urls import routerLoans
from Apps.Movimientos.Payment.Api_Payment.urls import routerPayment
from Apps.Movimientos.PaymentFrecuency.Api_Payfrecuency.urls import routerPaymentFrecuency
from Apps.Movimientos.PaymentStatus.Api_PayStatus.urls import routerPaymentStatus
from Seguridad.Usuarios.Api.UsuariosApi import UserCreateView

schema_view = get_schema_view(
   openapi.Info(
      title="SIDGEP_WEB",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routerCustomer.urls)),#Api Perspn
    path('api/', include(routerPerson.urls)),#Api Customer
    path('api/', include(routerLender.urls)),#Api Lender
    path('api/', include(routerLoans.urls)),#Api Loans
    path('api/', include(routerAlerts.urls)),#ApiAlerts
    path('api/', include(routerPayment.urls)),#ApiPayment
    path('api/', include(routerPaymentFrecuency.urls)),#ApiPayFrecuency
    path('api/', include(routerPaymentStatus.urls)),#ApipayStatus
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('Seguridad.Usuarios.Api.Router')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/register/', UserCreateView.as_view(), name='register'),
]
