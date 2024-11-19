from django.contrib import admin

from Apps.Catalogos.Person.models import Person


@admin.register(Person)
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['IdentityCard','Address','FirtsName','SecondName','FirsLastName','SecondLantName','Sexo','Age','phone','Email','Active']
    search_fields = ['IdentityCard']