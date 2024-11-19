from django.db import models

from Apps.Movimientos.Customer.models import Customer
from Apps.Movimientos.Lender.models import Lender


# Create your models here.

class Loans(models.Model):
    code_payment = models.CharField(max_length=10)
    AmountLent = models.DecimalField(max_digits=10, decimal_places=2)
    Interest = models.DecimalField(max_digits=10, decimal_places=2)
    StartDate = models.DateTimeField(auto_now_add=True)
    ExpirationDate = models.DateTimeField(auto_now_add=True)
    TotalAmountDue = models.DecimalField(max_digits=10, decimal_places=2)
    Active = models.BooleanField(default=True)
    id_Customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    id_Lender = models.ForeignKey(Lender, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Loans'

    def __str__(self):
        return self.code_payment
