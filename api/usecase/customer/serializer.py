from rest_framework import serializers
from api.models.customer import Customer
from api.models.loan import Loan


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Customer.

    Campos:
        - external_id: El identificador externo del cliente.
        - score: La puntuación del cliente.
        - status: El estado del cliente.
        - preapproved_at: La fecha de preaprobación del cliente.
    """
    class Meta:
        model = Customer
        fields = ('external_id', 'score', 'status', 'preapproved_at')
        read_only_fields = ('created_at', 'status',)


class CustomerBalanceSerializer(serializers.ModelSerializer):
    """
    Serializador para calcular el balance del cliente.

    Campos:
        - external_id: El identificador externo del cliente.
        - score: La puntuación del cliente.
        - total_debt: La deuda total del cliente.
        - available_amount: El monto disponible para el cliente.
    """
    total_debt = serializers.SerializerMethodField()
    available_amount = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('external_id', 'score', 'total_debt', 'available_amount')

    def get_customer_total_debt(self, customer: Customer) -> float:
        """Calcula la deuda total del cliente."""
        total_debt = sum(float(loan.outstanding) for loan in Loan.objects.filter(customer_id=customer.id, status=2))
        return total_debt

    def get_customer_amount(self, customer: Customer) -> float:
        """Calcula el monto disponible para el cliente."""
        available_amount = float(customer.score) - self.get_customer_total_debt(customer)
        return available_amount
