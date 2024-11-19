from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.PaymentFrecuency.models import PaymentFrequency

class PaymentFrequencySerializer(ModelSerializer):
    class Meta:
        model = PaymentFrequency
        fields = ['id','codigoP','Monthly','Weekly']