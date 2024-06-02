from rest_framework import serializers
from django.db import transaction
from api.models.loan import Loan
from api.models.customer import Customer
from utils.functions.helpers import extract_customer_id


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('external_id', 'customer_id', 'maximum_payment_date',
                  'amount', 'outstanding', 'status',)
        read_only_fields = ('created_at', 'status', 'outstanding',)

    @transaction.atomic
    def validate(self, data):
        customer_id_str = str(data.get('customer_id'))
        amount = data.get('amount')

        # Extraer el ID del cliente del string
        customer_id = extract_customer_id(customer_id_str)
        # Obtener el cliente
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("El cliente no existe.")
        total_debt = 0
        for operator_loan in Loan.objects.filter(customer_id=customer_id, status=2):
            total_debt += float(operator_loan.outstanding)

        # Calcular el available_amount del cliente
        available_amount = float(customer.score) - float(total_debt)

        # Validar que el monto solicitado más la deuda total no supere el available_amount
        if (float(amount) + total_debt) > available_amount:
            raise serializers.ValidationError(
                f"El monto solicitado más la deuda total no pueden superar el monto disponible. Actualmente este es tu monto disponible: {available_amount}")
        return data

    @transaction.atomic
    def create(self, validated_data):
        # Igualar el monto por pagar al monto solicitado
        validated_data['outstanding'] = validated_data['amount']
        return super().create(validated_data)


class LoanCreatedSerializer(serializers.ModelSerializer):
    customer_external_id: str = serializers.SerializerMethodField(
        'get_customer_external_id')

    class Meta:
        model = Loan
        fields = ('external_id', 'customer_external_id',
                  'amount', 'outstanding', 'status')
        read_only_fields = ('external_id', 'customer_external_id',
                  'amount', 'outstanding', 'status',)

    def get_customer_external_id(self, loan: Loan) -> str:
        return loan.customer_id.external_id

    def save(self, **kwargs):
        # Si necesitas manejar argumentos adicionales, hazlo aquí
        return super().save(**kwargs)


class LoansByCustomerSerializer(serializers.ModelSerializer):
    customer_external_id: str = serializers.SerializerMethodField(
        'get_customer_external_id')

    class Meta:
        model = Loan
        fields = ('external_id', 'customer_external_id',
                  'amount', 'outstanding', 'status')
        read_only_fields = ('created_at', 'status',)

    def get_customer_external_id(self, loan: Loan) -> str:
        return loan.customer_id.external_id
