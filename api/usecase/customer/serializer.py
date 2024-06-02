from rest_framework import serializers
from api.models.customer import Customer
from api.models.loan import Loan


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('external_id', 'score', 'status', 'preapproved_at')
        read_only_fields = ('created_at', 'status',)


class CustomerBalanceSerializer(serializers.ModelSerializer):
    total_debt: float = serializers.SerializerMethodField(
        'get_customer_total_debt')
    available_amount: float = serializers.SerializerMethodField('get_customer_amount')

    class Meta:
        model = Customer
        fields = ('external_id', 'score', 'total_debt', 'available_amount')

    def get_customer_total_debt(self, customer: Customer) -> float:
        sumOfAllLoans = 0.0
        listLoans = list(Loan.objects.filter(customer_id=customer.id).values('outstanding'))
        for loanSum in listLoans:
            sumOfAllLoans += float(loanSum['outstanding'])
        return sumOfAllLoans

    def get_customer_amount(self, customer: Customer) -> float:
        return float(customer.score) - self.get_customer_total_debt(customer)
