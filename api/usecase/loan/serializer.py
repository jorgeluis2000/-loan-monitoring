from rest_framework import serializers
from django.db import transaction
from api.models.loan import Loan
from api.models.customer import Customer
from utils.functions.helpers import extract_customer_id


class LoanSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Loan.

    Campos:
        - external_id: El identificador externo del préstamo.
        - customer_id: El ID del cliente asociado al préstamo.
        - maximum_payment_date: La fecha máxima de pago del préstamo.
        - amount: El monto del préstamo.
        - outstanding: El saldo pendiente del préstamo.
        - status: El estado del préstamo.
    """
    class Meta:
        model = Loan
        fields = ('id', 'external_id', 'customer_id', 'maximum_payment_date',
                  'amount', 'outstanding', 'status',)
        read_only_fields = ('id', 'created_at', 'status', 'outstanding',)

    @transaction.atomic
    def validate(self, data):
        """
        Método para validar los datos del préstamo.

        Realiza una validación personalizada para garantizar que el monto solicitado no exceda el saldo disponible del cliente.

        Args:
            data (dict): Los datos del préstamo.

        Returns:
            dict: Los datos validados del préstamo.

        Raises:
            serializers.ValidationError: Si el monto solicitado más la deuda total del cliente supera el monto disponible.
        """
        customer_id_str = str(data.get('customer_id'))
        amount = data.get('amount')

        # Extraer el ID del cliente del string
        customer_id = extract_customer_id(customer_id_str)
        # Obtener el cliente
        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("El cliente no existe.")
        total_debt = 0
        for operator_loan in Loan.objects.filter(customer_id=customer_id, status=2):
            total_debt += float(operator_loan.outstanding)

        # Calcular el available_amount del cliente
        available_amount = float(customer.score) - float(total_debt)

        # Validar que el monto solicitado más la deuda total no supere el available_amount
        if float(amount) > available_amount:
            raise serializers.ValidationError(
                f"El monto solicitado más la deuda total no pueden superar el monto disponible. Actualmente este es tu monto disponible: {available_amount}")
        return data

    @transaction.atomic
    def create(self, validated_data):
        """
        Método para crear un nuevo préstamo.

        Realiza una lógica personalizada para crear un nuevo préstamo y guarda los datos en la base de datos.

        Args:
            validated_data (dict): Los datos validados del préstamo.

        Returns:
            Loan: La instancia del préstamo creado.
        """
        # Igualar el monto por pagar al monto solicitado
        validated_data['outstanding'] = validated_data['amount']
        return super().create(validated_data)


class LoanCreatedSerializer(serializers.ModelSerializer):
    """
    Serializador para mostrar los detalles del préstamo creado.

    Campos:
        - external_id: El identificador externo del préstamo.
        - customer_external_id: El identificador externo del cliente asociado al préstamo.
        - amount: El monto del préstamo.
        - outstanding: El saldo pendiente del préstamo.
        - status: El estado del préstamo.
    """
    customer_external_id: str = serializers.SerializerMethodField(
        'get_customer_external_id')

    class Meta:
        model = Loan
        fields = ('id', 'external_id', 'customer_external_id',
                  'amount', 'outstanding', 'status')
        read_only_fields = ('id', 'external_id', 'customer_external_id',
                            'amount', 'outstanding', 'status',)

    def get_customer_external_id(self, loan: Loan) -> str:
        """
        Método para obtener el identificador externo del cliente asociado al préstamo.

        Args:
            loan (Loan): La instancia del préstamo.

        Returns:
            str: El identificador externo del cliente.
        """
        return loan.customer_id.external_id

    def save(self, **kwargs):
        """
        Método para guardar los datos del préstamo.

        Realiza la operación de guardado de los datos del préstamo en la base de datos.

        Args:
            **kwargs: Argumentos adicionales.

        Returns:
            Loan: La instancia del préstamo guardado.
        """
        # Si necesitas manejar argumentos adicionales, hazlo aquí
        return super().save(**kwargs)


class LoansByCustomerSerializer(serializers.ModelSerializer):
    """
    Serializador para mostrar los préstamos de un cliente específico.

    Campos:
        - external_id: El identificador externo del préstamo.
        - customer_external_id: El identificador externo del cliente asociado al préstamo.
        - amount: El monto del préstamo.
        - outstanding: El saldo pendiente del préstamo.
        - status: El estado del préstamo.
    """
    customer_external_id: str = serializers.SerializerMethodField(
        'get_customer_external_id')

    class Meta:
        model = Loan
        fields = ('id', 'external_id', 'customer_external_id',
                  'amount', 'outstanding', 'status')
        read_only_fields = ('id', 'created_at', 'status',)

    def get_customer_external_id(self, loan: Loan) -> str:
        """
        Método para obtener el identificador externo del cliente asociado al préstamo.

        Args:
            loan (Loan): La instancia del préstamo.

        Returns:
            str: El identificador externo del cliente.
        """
        return loan.customer_id.external_id
