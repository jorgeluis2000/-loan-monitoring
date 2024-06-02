from rest_framework import viewsets, permissions
from api.usecase.paymentdetail.serializer import PaymentDetailSerializer
from api.models.paymentdetail import PaymentDetail

class PaymentDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, actualizar o eliminar detalles de pagos.
    """
    queryset = PaymentDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentDetailSerializer
