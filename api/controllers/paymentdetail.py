from rest_framework import viewsets, permissions
from api.usecase.paymentdetail.serializer import PaymentDetailSerializer
from api.models.paymentdetail import PaymentDetail
# Create your views here.


class PaymentDetailViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentDetailSerializer
