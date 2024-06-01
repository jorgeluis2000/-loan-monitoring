from rest_framework import viewsets, permissions
from api.usecase.loan.serializer import LoanSerializer
from api.models.loan import Loan
# Create your views here.

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer