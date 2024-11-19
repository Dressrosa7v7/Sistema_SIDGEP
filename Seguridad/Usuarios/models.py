from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuarios(AbstractUser):
    pass


    class Meta:
        db_table = 'Usuario'