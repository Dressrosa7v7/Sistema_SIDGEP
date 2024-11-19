from django.db import models
# Create your models here.

class PaymentFrequency(models.Model):
    codigoP = models.CharField(max_length=10)
    Monthly = models.CharField(max_length=200)
    Weekly = models.CharField(max_length=200)

    class Meta:
        db_table = 'PaymentFrecuency'

    def __str__(self):
        return self.codigoP