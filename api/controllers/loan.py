from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from api.usecase.loan.serializer import LoanSerializer, LoanCreatedSerializer, LoansByCustomerSerializer
from api.models.loan import Loan


class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, actualizar o eliminar préstamos.
    """
    queryset = Loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo préstamo a partir de los datos proporcionados en la solicitud.
        """
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            loan_saved = serializer.instance
            new_serializer = LoanCreatedSerializer(loan_saved)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_loans_by_customer(request, pk_customer):
    """
    Obtiene todos los préstamos asociados a un cliente específico.
    """
    loans = Loan.objects.filter(customer_id=pk_customer)
    serializer = LoansByCustomerSerializer(loans, many=True)
    return Response(serializer.data)
