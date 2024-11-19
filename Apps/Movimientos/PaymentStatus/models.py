from django.db import models

# Create your models here.

class PaymentStatus(models.Model):
    codigoT = models.CharField(max_length=10)
    Asset = models.CharField(max_length=20)
    Paid = models.CharField(max_length=20)
    Defeated = models.CharField(max_length=20)
    InMora = models.CharField(max_length=20)

    class Meta:
        db_table = 'PaymentStatus'

    def __str__(self):
        return self.codigoT
