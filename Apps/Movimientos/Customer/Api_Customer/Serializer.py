from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.Customer.models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','codigo','DateRegistration', 'MonthlyIncome', 'CreditLimit','Active', 'id_person']