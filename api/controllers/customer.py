from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from api.usecase.customer.serializer import CustomerSerializer, CustomerBalanceSerializer
from api.models.customer import Customer
from api.models.loan import Loan
from api.models.payment import Payment
from api.models.paymentdetail import PaymentDetail
from api.usecase.loan.serializer import LoansByCustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, actualizar o eliminar clientes.
    """
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer

    @action(methods=['GET'], detail=True,
            url_path='balance', url_name='get_balance')
    def get_customer_balance(self, request, pk):
        """
        Obtiene el saldo del cliente especificado por su ID.
        """
        customer = Customer.objects.get(id=pk)
        serializer = CustomerBalanceSerializer(customer, many=False)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True,
            url_path='loans', url_name='get_loans_by_customer')
    def get_loans_by_customer(self, _, pk):
        """
        Obtiene los préstamos asociados a un cliente especificado por su ID.
        """
        loans = Loan.objects.filter(customer_id=pk)
        serializer = LoansByCustomerSerializer(loans, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True,
            url_path='payments', url_name='get_payments_by_customer')
    def get_payments_by_customer(self, _, pk):
        """
        Obtiene los pagos asociados a un cliente especificado por su ID.
        """
        customer = Customer.objects.get(id=pk)
        payments = Payment.objects.filter(customer_id=pk)

        object_list_payments_detail = []
        serialized_payments = []
        for payment in payments:
            payments_detail = PaymentDetail.objects.filter(
                payment_id=payment.pk)
            for payment_detail in payments_detail:
                payment_by_customer = {
                    "external_id": payment.external_id,
                    "customer_external_id": customer.external_id,
                    "loan_external_id": str(payment_detail.loan_id),
                    "payment_date": str(payment.paid_at),
                    "status": payment.status,
                    "total_amount": float(payment.total_amount),
                    "payment_amount": float(payment_detail.amount)
                }
                object_list_payments_detail.append(payment_by_customer)
        serialized_payments.extend(object_list_payments_detail)
        return Response(serialized_payments, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_customers_from_txt(request):
    """
    Crea clientes a partir de un archivo de texto enviado mediante una solicitud POST.
    """
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            for line in file:
                external_id, score = line.decode('utf-8').strip().split(',')
                customer_data = {
                    'external_id': external_id,
                    'score': score
                }
                serializer = CustomerSerializer(data=customer_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
            return Response({'message': 'Customers created successfully'}, status=201)
        except:
            return Response({'message': 'File not provided'}, status=400)
    else:
        return Response({'error': 'File not provided'}, status=400)
