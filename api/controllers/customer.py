import json
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from api.usecase.customer.serializer import CustomerSerializer, CustomerBalanceSerializer
from api.models.customer import Customer
from api.models.loan import Loan
from api.models.payment import Payment
from api.models.paymentdetail import PaymentDetail
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
    def get_loans_by_customer(self, _, pk):
        loans = Loan.objects.filter(customer_id=pk)
        serializer = LoansByCustomerSerializer(loans, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True,
            url_path='payments', url_name='get_payments_by_customer')
    def get_payments_by_customer(self, _, pk):
        customer = Customer.objects.get(id=pk)
        payments = Payment.objects.filter(customer_id=pk)

        object_list_payments_detail: list = []
        serialized_payments = []
        for payment in payments:
            payments_detail = PaymentDetail.objects.filter(
                payment_id=payment.pk)
            for payment_detail in payments_detail:
                payment_by_customer = {"external_id": payment.external_id, "customer_external_id": customer.external_id, "loan_external_id": str(
                    payment_detail.loan_id), "payment_date": str(payment.paid_at), "status": payment.status, "total_amount": float(payment.total_amount), "payment_amount": float(payment_detail.amount)}
                object_list_payments_detail.append(payment_by_customer)
        serialized_payments.extend(object_list_payments_detail)
        return Response(serialized_payments, status=status.HTTP_200_OK)
