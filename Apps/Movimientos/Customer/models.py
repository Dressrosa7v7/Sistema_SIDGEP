from django.db import models

from Apps.Catalogos.Person.models import Person


# Create your models here.

class Customer(models.Model):
    codigo = models.CharField(max_length=10)
    DateRegistration = models.DateTimeField(auto_now_add=True)
    MonthlyIncome = models.DecimalField(max_digits=10, decimal_places=2)
    CreditLimit = models.IntegerField(null= False)
    Active = models.BooleanField(default=True)
    id_person = models.ForeignKey(Person, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Customer'

    def __int__(self):
        return self.codigo
