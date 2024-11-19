from django.db import models

from Apps.Catalogos.Person.models import Person


# Create your models here.
class Lender(models.Model):
    codigoL = models.CharField(max_length=10)
    HiringDate = models.DateTimeField(auto_now_add=True)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Active = models.BooleanField(default=True)
    id_person = models.ForeignKey(Person, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'Lender'

    def __str__(self):
        return self.codigoL
