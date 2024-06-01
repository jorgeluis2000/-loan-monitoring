from rest_framework import viewsets, permissions
from api.usecase.customer.serializer import CustomerSerializer
from api.models.customer import Customer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer