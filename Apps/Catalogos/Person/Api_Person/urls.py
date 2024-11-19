from Apps.Catalogos.Person.Api_Person.Person_Api import PersonViewSet
from rest_framework.routers import DefaultRouter

routerPerson = DefaultRouter()

routerPerson.register(prefix='Person', basename='Person', viewset=PersonViewSet)