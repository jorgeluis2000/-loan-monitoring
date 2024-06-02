from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from api.usecase.loan.serializer import LoanSerializer
from api.models.loan import Loan
# Create your views here.

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)