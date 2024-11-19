from Seguridad.Usuarios.models import Usuarios
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuarios
        fields = ('username', 'email', 'password', 'password2', 'email', 'first_name', 'last_name')

    #Validacion de las contreñas
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'Password': "Las Contraseña no coinsiden."})
        return attrs

    def create(self, validated_data):
        usuarios = Usuarios(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        usuarios.set_password(validated_data['password'])
        usuarios.save()
        return usuarios