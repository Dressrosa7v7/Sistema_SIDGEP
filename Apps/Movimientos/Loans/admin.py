
from django.contrib import admin

from Apps.Movimientos.Loans.models import Loans


@admin.register(Loans)

# Register your models here.

class LoansAdmin(admin.ModelAdmin):
    list_display = ['code_payment','AmountLent', 'Interest','StartDate','ExpirationDate','TotalAmountDue', 'id_Customer','id_Lender', 'Active']
    search_fields = ['code_payment']