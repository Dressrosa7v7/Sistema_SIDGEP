from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.Payment.Api_Payment.Serializer import PaymentSerializer
from Apps.Movimientos.Payment.models import Payment
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PaymentSerializer(Payment.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se a listado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            serch = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(serch)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se he realizada la busqueda correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Payment.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No exite el regitro buscado",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        valida = Payment.objects.filter(N_Payment=serializer.validated_data['N_Payment']).exists()
        if valida:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_400_BAD_REQUEST,
                Message="Ya existe ese codigo",
                Record=None
            )
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data.toResponse())
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se he registrado correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())


    def update(self, request, pk=int):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(instance=payment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message="Se he actualizado correctamente",
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except Payment.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No exite el regitro buscado",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        payment.delete()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Se ha eliminados correctamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_204_NO_CONTENT,data=data.toResponse())

    #Endpoint Propios
    @action(methods=['GET'], detail=False)
    def MontosPrioridad(self, request):
        p = Payment.obsjects.filter(AmountPerPayment__gt=4000)
        serializer = PaymentSerializer(p, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Los pagos mas importantes",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def ordenpagos(self, request):
        orden = Payment.objects.all().order_by('AmountPerPayment')
        serializer = PaymentSerializer(orden, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Pagos del menor al mayor",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def montoscasiterminados(self, request):
        mon = Payment.objects.filter(AmountPaid__gte=2)
        serializer = PaymentSerializer(mon, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Los pagos por terminar",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    @action(methods=['GET'], detail=False)
    def primerosMontos(self, request):
        mon = Payment.objects.filter(AmountPaid__gt=1)
        serializer = PaymentSerializer(mon, many=True)
        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message="Los pagos por terminar",
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())