from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from api.usecase.customer.serializer import CustomerSerializer, CustomerBalanceSerializer
from api.models.customer import Customer
from api.models.loan import Loan
from api.usecase.loan.serializer import LoansByCustomerSerializer


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    
    @action(methods=['GET'], detail=True,
            url_path='balance', url_name='get_balance')
    def get_customer_balance(self, request, pk):
        customer = Customer.objects.get(id=pk)
        serializer = CustomerBalanceSerializer(customer, many=False)
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=True,
        url_path='loans', url_name='get_loans_by_customer')
    def get_loans_by_customer(self, request, pk):
        loans = Loan.objects.filter(customer_id=pk)
        serializer = LoansByCustomerSerializer(loans, many=True)
        return Response(serializer.data)