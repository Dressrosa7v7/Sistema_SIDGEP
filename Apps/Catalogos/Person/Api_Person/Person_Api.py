from django.db.models import Count

from Apps.Catalogos.Person.Api_Person.Serializer import PersonSerializer
from Apps.Catalogos.Person.models import Person

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from Apps.Utils.PermisionAPI import CustomPermission
from Apps.Utils.ResponseData import ResponseData
from rest_framework.permissions import IsAuthenticated


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated, CustomPermission]

    def list(self, request):
        serializer = PersonSerializer(Person.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record= serializer.data
        )

        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk= int):
        try:
            serch = Person.objects.get(pk=pk)
            serializer = PersonSerializer(serch)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Person.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el numero de cedula",
                Record=None
            )
            return Response(data, status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #Validamos ci la cedula existe
        identiticard = Person.objects.filter(IdentityCard=serializer.validated_data['IdentityCard']).exists()

        if identiticard:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="ya existe",
                Record=None
            )
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.toResponse())

        serializer.save()

        data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a creado el nuevo registro",
                Record= serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk= int):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(instance=person, data= request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="El registro se actualizo correctamente",
                Record= serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Person.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha podido actualizar el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk= int):
        try:
            pos = Person.objects.get(pk=pk)
            if not pos.Active:
                data = ResponseData(
                    Success=False,
                    Status=status.HTTP_404_NOT_FOUND,
                    Message="El registro esta desactivado",
                    Record=None
                )
                return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
            # Si esta Activo
            pos.Active = False
            pos.save()
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha Desactivado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())
        except Person.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea desactivar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

        # Listar las personas mayores de edad
    @action(methods=['GET'], detail=False)
    def GetListarMayores(self, request):
        edad = Person.objects.all().order_by('Age')
        serializer = PersonSerializer(edad, many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado los mayores de edad",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

        # Filtrar a los clientes de masaya
    @action(methods=['GET'], detail=False)
    def MasayaFiltro(self, request):
        persona = Person.objects.filter(IdentityCard__contains='401')
        serializer = PersonSerializer(persona, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Todo los clientes que viven son del departamento de masaya",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

        # Contar la cantidad de personas Existente
    @action(methods=['GET'], detail=False)
    def ContarPersonas(self, request):
        Contar = Person.objects.count()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Todos los registros que existen",
            Record={"Cantidad de personas": Contar}
            )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

