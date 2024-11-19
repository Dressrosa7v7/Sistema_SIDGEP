from django.contrib import admin

from Apps.Movimientos.Payment.models import Payment



@admin.register(Payment)

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['N_Payment','PaymentDate','AmountPerPayment','AmountPaid','PendingAmount','Active','id_Loans','id_PayFrecuency','id_payStatus']
    search_fields = ['N_Payment']