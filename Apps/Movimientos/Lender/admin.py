from django.contrib import admin

from Apps.Movimientos.Lender.models import Lender

@admin.register(Lender)

# Register your models here.

class LenderAdmin(admin.ModelAdmin):
    list_display = ['codigoL','HiringDate','Salary','id_person','Active']
    search_fields = ['codigoL']