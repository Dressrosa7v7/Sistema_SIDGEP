from django.db import models
from Apps.Movimientos.Loans.models import Loans

# Create your models here.
class Alerts(models.Model):
    CodeAlerts = models.IntegerField(null= False)
    AlertDate = models.DateTimeField(null=True)
    MessegaAlert = models.CharField(max_length=225)
    Active = models.BooleanField(default=True)
    id_Loans = models.ForeignKey(Loans, on_delete=models.RESTRICT)


    class Meta:
        db_table = 'Alerts'

    def __str__(self):
        return self.CodeAlerts

