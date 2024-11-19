from django.db import models

# Create your models here.

class Person (models.Model):
    IdentityCard = models.CharField(max_length=16)
    Address = models.CharField(max_length=200)
    FirtsName = models.CharField(max_length=50)
    SecondName = models.CharField(max_length=50)
    FirsLastName = models.CharField(max_length=50)
    SecondLantName = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Age = models.IntegerField(null= False)
    phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=200)
    Active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Person'

    def __str__(self):
        return self.IdentityCard
