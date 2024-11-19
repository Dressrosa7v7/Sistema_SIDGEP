from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.db.models import Sum
from rest_framework.decorators import action
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.Lender.Api_Lender.Serializer import LenderSerializer
from Apps.Movimientos.Lender.models import Lender
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class LenderViewSet(ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = LenderSerializer(Lender.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Lender.objects.get(pk=pk)
            serializer = LenderSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha buscado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Lender.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = LenderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lender = Lender.objects.filter(codigoL=serializer.validated_data['codigoL']).exists()
        if lender:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="El Codigo ya existe",
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
            lender = Lender.objects.get(pk=pk)
            serializer = LenderSerializer(instance=lender, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha actualizado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Lender.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        try:
            pos = Lender.objects.get(pk=pk)
            if not pos.Active:
                data = ResponseData(
                    Success=False,
                    Status=status.HTTP_404_NOT_FOUND,
                    Message="No existe esta desactivado",
                    Record=None
                )
                return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
            #Si esta activo
            pos.Active = False
            pos.save()
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha desactivado correctamente",
                Record=None
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())
        except  Lender.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())


    #Endpoint Propios
    @action(methods=['GET'], detail=False)
    def MasViejo(self, request):
        ultimo = Lender.objects.all().order_by('-pk')
        serializer = LenderSerializer(ultimo, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Los tarbajadores con mas experiencia",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def SalariosMayores(self, request):
        alto = Lender.objects.filter(Salary__gte=3690)#Solo si el salario excede los 100 dolares
        serializer = LenderSerializer(alto, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Salarios mas alto",
            Record={"Los prestamista con salarios altos son :": serializer}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def TotalSalarios(self, request):
        sum = Lender.objects.aggregate(Salary=Sum('Salary'))
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Salarios total",
            Record={"Cantidad: ":sum}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())
