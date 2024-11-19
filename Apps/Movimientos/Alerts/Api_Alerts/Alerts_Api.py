from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from Apps.Movimientos.Loans.Api_Loans.Serializer import LoansSerializer
from Apps.Movimientos.Loans.models import Loans
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.Alerts.Api_Alerts.Serializer import AlertsSerializer
from Apps.Movimientos.Alerts.models import Alerts
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class AlertsViewSet(ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = AlertsSerializer(Alerts.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha lisdatos las alertas correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK,data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = Alerts.objects.get(pk=pk)
            serializer = AlertsSerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha encontrado Correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Alerts.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro buscado"
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = AlertsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #Validamos si el codigo de la alerta ya existe

        codealerts = Alerts.objects.filter(CodeAlerts=serializer.validated_data['CodeAlerts']).exists()
        if codealerts:
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
        return Response(status=status.HTTP_2000_OK, data=data.toResponse())

    def update(self, request, pk=int):
        try:
            alert = Alerts.objects.get(pk=pk)
            serializer = AlertsSerializer(instance=alert, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se ha actualizado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())
        except Alerts.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea actualizar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        try:
            pos = Alerts.objects.get(pk=pk)
            if not pos.Active:
                data = ResponseData(
                    Success=True,
                    Status=status.HTTP_200_OK,
                    Message="El registro esta desactivado",
                    Record=None
                )
                return Response(status=status.HTTP_204_NO_CONTENT, data=data.toResponse())
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
        except Alerts.DoesNotExists:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro que desea desactivar",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    @action(methods=['GET'],detail=False)
    def ContarAlertas(self, request):
        contar = Alerts.objects.count()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Todas las alertas existente",
            Record={"La cantidad de alertasd son": contar}
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'],detail=True)
    def Alertas_Proxima(self, request):
        lista = Alerts.objects.all().order_by('-AlertDate')
        serializer = AlertsSerializer(lista, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="La proximas alertas",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'],detail=False)
    def AlertasSercana(self, request):
        alerta = Alerts.objects.all().order_by('-AlertDate')
        serializer = LoansSerializer(alerta, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha encontrado correctamente",
            Record=serializer.data
        )
        Response(status=status.HTTP_200_OK, data=data.toResponse())