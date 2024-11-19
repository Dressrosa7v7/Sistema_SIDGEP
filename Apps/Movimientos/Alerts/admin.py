from django.contrib import admin

from Apps.Movimientos.Alerts.models import Alerts

@admin.register(Alerts)


class  AlertsAdmin(admin.ModelAdmin):
    list_display = ['CodeAlerts','AlertDate','MessegaAlert','Active','id_Loans']
    search_fields = ['CodeAlerts']