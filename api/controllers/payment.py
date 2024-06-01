from rest_framework import viewsets, permissions
from api.usecase.payment.serializer import PaymentSerializer
from api.models.payment import Payment
# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer