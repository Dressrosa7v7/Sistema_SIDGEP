from pickle import FALSE

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.db.models import Sum
from Apps.Catalogos.Person.models import Person
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.Customer.Api_Customer.Serializer import CustomerSerializer
from Apps.Movimientos.Customer.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CustomerSerializer(Customer.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Customer.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="Se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer = Customer.objects.filter(codigo=serializer.validated_data['codigo']).exists()
        if customer:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="El registro ya existe",
                Record=None
            )
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.toResponse())

        serializer.save()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message="Se ha creado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk=int):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(instance=customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="El registro se actualizo correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Customer.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )

    def destroy(self, request, pk=int):
        try:
            pos = Customer.objects.get(pk=pk)
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
        except Customer.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea desactivar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())


    @action(methods=['GET'],detail=False)
    def ListCustomer(self, request):
        orden = Customer.objects.all().order_by('codigo')
        serializer = CustomerSerializer(orden, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha ordenado deacuerdo a los datos",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'],detail=False)
    def LimiteInicio(self, request):
        credito = Customer.objects.filter(CreditLimit='2000').count()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message='Los cliente con credito inicial',
            Record={"Cantidad": credito}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'],detail=False)
    def Suma_Creditos(self, request):
        sum = Customer.objects.aggregate(CreditLimit=Sum('CreditLimit'))
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message='Se ha agregado la suma de la cuenta',
            Record={"Cantidad": sum}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())


