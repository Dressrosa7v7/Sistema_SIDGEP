from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.Alerts.models import Alerts

class AlertsSerializer(ModelSerializer):
    class Meta:
        model = Alerts
        fields = ['id','CodeAlerts','AlertDate','MessegaAlert','Active','id_Loans']