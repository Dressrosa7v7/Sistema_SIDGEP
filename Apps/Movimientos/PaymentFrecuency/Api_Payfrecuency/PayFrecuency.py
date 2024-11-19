from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.PaymentFrecuency.Api_Payfrecuency.Serializer import PaymentFrequencySerializer
from Apps.Movimientos.PaymentFrecuency.models import PaymentFrequency
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class PayFrequencyViewSet(ModelViewSet):
    queryset = PaymentFrequency.objects.all()
    serializer_class = PaymentFrequencySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PaymentFrequencySerializer(PaymentFrequency.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message='Se ha listado correctamente',
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            search = PaymentFrequency.objects.get(pk=pk)
            serializer = PaymentFrequencySerializer(search)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message='Se ha encontrado el registro',
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except PaymentFrequency.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message='No existe el registro',
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = PaymentFrequencySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message='Se ha creado correctamente',
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def update(self, request, pk=int):
        try:
            payF = PaymentFrequency.objects.get(pk=pk)
            serializer = PaymentFrequencySerializer(instance=payF, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message='Se ha actualizado correctamente',
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except PaymentFrequency.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message='No existe el registro',
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        payF = PaymentFrequency.objects.get(pk=pk)
        serializer = PaymentFrequencySerializer(payF)
        payF.delete()
        data = ResponseData(
            Success=True,
            Status=status.HTTP_204_NO_CONTENT,
            Message="Se ha eliminado existosamente",
            Record=serializer.data
        )
        return Response(status=status.HTTP_204_NO_CONTENT, data=data.toResponse())


