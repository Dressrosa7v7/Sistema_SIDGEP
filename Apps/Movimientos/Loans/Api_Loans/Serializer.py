from rest_framework.serializers import ModelSerializer
from Apps.Movimientos.Loans.models import Loans

class LoansSerializer(ModelSerializer):
    class Meta:
        model = Loans
        fields = ['id','code_payment','AmountLent', 'Interest','StartDate','ExpirationDate','TotalAmountDue', 'Active', 'id_Customer','id_Lender']