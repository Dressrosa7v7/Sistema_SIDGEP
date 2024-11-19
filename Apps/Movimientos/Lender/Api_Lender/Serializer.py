from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.Lender.models import Lender

class LenderSerializer(ModelSerializer):
    class Meta:
        model = Lender
        fields = ['codigoL','HiringDate','Salary','Active','id_person']