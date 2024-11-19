from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Seguridad.Usuarios.models import Usuarios

@admin.register(Usuarios)
# Register your models here.
class UsuariosAdmin(UserAdmin):
    pass