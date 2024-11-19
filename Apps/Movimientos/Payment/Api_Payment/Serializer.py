from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.Payment.models import Payment

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','N_Payment','PaymentDate','AmountPerPayment','AmountPaid','PendingAmount','Active','id_PayFrecuency','id_payStatus','id_Loans']