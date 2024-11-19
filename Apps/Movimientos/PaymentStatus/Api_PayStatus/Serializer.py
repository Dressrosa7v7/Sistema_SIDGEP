from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.PaymentStatus.models import PaymentStatus

class PaymentStatusSerializer(ModelSerializer):
    class Meta:
        model = PaymentStatus
        fields = ['Asset','Paid','Defeated','InMora']