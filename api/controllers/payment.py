from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from api.usecase.payment.serializer import PaymentSerializer, PaymentCreatedSerializer, PaymentGetSerializer
from api.models.payment import Payment

class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, actualizar o eliminar pagos.
    """
    queryset = Payment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer
    
    def get_serializer_class(self):
        """
        Devuelve la clase serializadora adecuada según la acción solicitada.
        """
        if self.action == 'create':
            return PaymentSerializer
        return PaymentGetSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo pago a partir de los datos proporcionados en la solicitud.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = serializer.save()
        response_serializer = PaymentCreatedSerializer(payment)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
