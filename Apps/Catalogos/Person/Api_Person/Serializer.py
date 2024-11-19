from Apps.Catalogos.Person.models import Person
from rest_framework.serializers import ModelSerializer


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'IdentityCard', 'Address', 'FirtsName', 'SecondName', 'FirsLastName', 'SecondLantName', 'Sexo',
                  'Age', 'phone', 'Email','Active']
