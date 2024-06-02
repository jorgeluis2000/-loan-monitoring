from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.usecase.customer.serializer import CustomerSerializer, CustomerBalanceSerializer
from api.models.customer import Customer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    
    
@api_view(['GET'])
def get_customer_balance(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerBalanceSerializer(customer, many=False)
    return Response(serializer.data)