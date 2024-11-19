from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from Apps.Utils.ResponseData import ResponseData
from Apps.Movimientos.PaymentStatus.Api_PayStatus.Serializer import PaymentStatusSerializer
from Apps.Movimientos.PaymentStatus.models import PaymentStatus
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class PaymentStatusViewSet(ModelViewSet):
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PaymentStatusSerializer(PaymentStatus.objects.all(), many=True)

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message='Se a listado correctamente',
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def retrieve(self, request, pk=int):
        try:
            searc = PaymentStatus.objects.get(pk=pk)
            serializer = PaymentStatusSerializer(searc)
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message='Se a buscado correctamente',
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except PaymentStatus.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def create(self, request):
        serializer = PaymentStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_201_CREATED,
            Message='Se a creada correctamente',
            Record=serializer.data
        )
        return Response(status=status.HTTP_200_OK, data=data.toResponse())

    def Update(self, request, pk=int):
        try:
            pyStatus = PaymentStatus.objects.get(pk=pk)
            serializer = PaymentStatusSerializer(instance=pyStatus, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = ResponseData(
                Success=True,
                Status=status.HTTP_200_OK,
                Message='Se a actualizada correctamente',
                Record=serializer.data
            )
            return Response(status=status.HTTP_200_OK, data=data.toResponse())

        except PaymentStatus.DoesNotExist:
            data = ResponseData(
                Success=False,
                Status=status.HTTP_404_NOT_FOUND,
                Message="No existe el registro",
                Record=None
            )
            return Response(status=status.HTTP_404_NOT_FOUND, data=data.toResponse())

    def destroy(self, request, pk=int):
        pyStatus = PaymentStatus.objects.get(pk=pk)
        serializer = PaymentStatusSerializer(pyStatus)
        pyStatus.delete()

        data = ResponseData(
            Success=True,
            Status=status.HTTP_200_OK,
            Message='Se a eliminada correctamente',
            Record=serializer.data
        )
        return Response(status=status.HTTP_204_NO_CONTENT, data=data.toResponse())

