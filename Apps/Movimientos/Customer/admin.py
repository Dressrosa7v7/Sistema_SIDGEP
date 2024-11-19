from django.contrib import admin

from Apps.Movimientos.Customer.models import Customer

@admin.register(Customer)

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['codigo','DateRegistration','MonthlyIncome','CreditLimit','id_person','Active']
    search_fields = ['codigo']