from django.contrib import admin

from Apps.Movimientos.PaymentStatus.models import PaymentStatus


@admin.register(PaymentStatus)

# Register your models here.

class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ['codigoT','Asset','Paid','Defeated','InMora']
    search_fields = ['codigoT']