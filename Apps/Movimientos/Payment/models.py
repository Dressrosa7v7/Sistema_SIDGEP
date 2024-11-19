from django.db import models

from Apps.Movimientos import Payment
from Apps.Movimientos.Loans.models import Loans
from Apps.Movimientos.PaymentFrecuency.models import PaymentFrequency
from Apps.Movimientos.PaymentStatus.models import PaymentStatus


# Create your models here.

class Payment(models.Model):
    N_Payment = models.CharField(max_length=10)
    PaymentDate = models.DateTimeField(auto_now_add=True)
    AmountPerPayment = models.DecimalField(max_digits=10, decimal_places=2)
    AmountPaid = models.DecimalField(max_digits=10, decimal_places=2)
    PendingAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Active = models.BooleanField(default=True)
    id_Loans = models.ForeignKey(Loans, on_delete=models.RESTRICT)
    id_PayFrecuency = models.ForeignKey(PaymentFrequency, on_delete=models.RESTRICT)
    id_payStatus = models.ForeignKey(PaymentStatus, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Payment'

    def __str__(self):
        return self.N_Payment
