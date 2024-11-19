from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.Loans.Api_Loans.Serializer import LoansSerializer
from Apps.Movimientos.Loans.models import Loans
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum

class LoansViewSet(ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = LoansSerializer(Loans.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Loans.objects.get(pk=pk)
            serializer = LoansSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a buscado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Loans.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = LoansSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = Loans.objects.filter(code_payment=serializer.validated_data['code_payment']).exists()
        if code:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="Ya existe ese prestamo",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message="Se a creado el registro",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk=int):
        try:
            loans = Loans.objects.get(pk=pk)
            serializer = LoansSerializer(loans, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se a actualizada correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Loans.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No se ha encontrado el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        try:
            pos = Loans.objects.get(pk=pk)
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
        except Loans.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea desactivar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    #Endpoints Propio
    @action(methods=['GET'], detail=False)
    def ActivoTotal(self, request):
        actsum = Loans.objects.aggregate(AmountLent=Sum('Total'))
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="La cantidad total del activo.",
            Record={"Dinero total":actsum}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def PrestamosImportante(self, request):
        grande = Loans.objects.filter(TotalAmountDue__gte="5000")
        serializer = LoansSerializer(grande, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="La cantidad total de los prestamos importante",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def PrestamosActivos(self, request):
        activo = Loans.objects.filter(Active=True)
        serializer = LoansSerializer(activo, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="La cantidad total de los prestamos activos",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())
