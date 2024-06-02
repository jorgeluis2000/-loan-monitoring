from rest_framework import serializers
from django.db import transaction
from api.models.payment import Payment
from api.models.paymentdetail import PaymentDetail
from api.models.loan import Loan
from api.usecase.paymentdetail.serializer import PaymentDetailObjectSerializer, PaymentDetailSerializer
from utils.functions.helpers import extract_customer_id


class PaymentSerializer(serializers.ModelSerializer):
    payments_loan_detail = PaymentDetailObjectSerializer(many=True)

    class Meta:
        model = Payment
        fields = ('external_id', 'customer_id', 'payments_loan_detail',
                  'created_at', 'updated_at', 'status', 'paid_at', 'total_amount')
        read_only_fields = ('created_at', 'status', 'total_amount')

    @transaction.atomic
    def create(self, validated_data):
        total_amount = 0
        customer = extract_customer_id(str(validated_data['customer_id']))
        payment_details_data: list[PaymentDetail] = validated_data.pop(
            'payments_loan_detail')
        loans = Loan.objects.filter(customer_id=customer, status=2)
        rejected = False

        # Crear los detalles del pago
        for payment_detail_data in payment_details_data:
            total_amount += float(payment_detail_data['amount'])
        validated_data['total_amount'] = total_amount
        # Calcular la suma de todos los préstamos del cliente
        total_loans_amount = 0
        for active_loan in loans:
            total_loans_amount += float(active_loan.outstanding)

        for payment_detail_data in payment_details_data:
            loan_compared = Loan.objects.get(
                id=extract_customer_id(str(payment_detail_data['loan_id'])))
            if float(payment_detail_data['amount']) > loan_compared.outstanding:
                rejected = True
        # Verificar si el total_amount del payment supera la suma de los préstamos
        if total_amount > total_loans_amount or rejected != False:
            # Establecer el estado en 2 (rechazado)
            validated_data['status'] = 2
        else:
            # Establecer el estado en 1 (Completado)
            validated_data['status'] = 1
        # Crear el pago

        payment = Payment.objects.create(**validated_data)
        payment.save()
        for payment_detail_data in payment_details_data:
            payment_detail = PaymentDetail.objects.create(
                payment_id=payment, **payment_detail_data)
            payment_detail.save()
            if (rejected != True):
                loan_updated = Loan.objects.get(
                    id=extract_customer_id(str(payment_detail_data['loan_id'])))
                if int(loan_updated.customer_id.pk) != customer:
                    raise serializers.ValidationError(
                        f'El cliente {str(payment_detail_data["loan_id"])} no cuenta con la deuda {str(payment_detail_data["loan_id"])}')
                loan_updated.outstanding -= payment_detail.amount
                if loan_updated.outstanding < 0:
                    loan_updated.outstanding = 0
                if loan_updated.outstanding == 0:
                    loan_updated.status = 4
                loan_updated.save()
        return payment


class PaymentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('external_id', 'customer_id', 'status', 'paid_at',
                  'total_amount', 'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'status', 'total_amount')


class PaymentCreatedSerializer(serializers.ModelSerializer):
    customer_external_id = serializers.SerializerMethodField()
    loan_external_id = serializers.SerializerMethodField()
    payment_amount = serializers.SerializerMethodField()
    payment_date = serializers.DateTimeField(source='created_at')
    payments_details = PaymentDetailSerializer(
        many=True, source='paymentdetail_set')

    class Meta:
        model = Payment
        fields = ('external_id', 'customer_external_id', 'loan_external_id',
                  'payment_date', 'status', 'total_amount', 'payment_amount', 'payments_details')
        read_only_fields = ('external_id', 'customer_external_id', 'loan_external_id',
                            'payment_date', 'status', 'total_amount', 'payment_amount',)

    def get_customer_external_id(self, payment):
        return payment.customer_id.external_id

    def get_loan_external_id(self, payment):
        payment_detail = PaymentDetail.objects.filter(
            payment_id=payment.id).first()
        if payment_detail:
            return payment_detail.loan_id.external_id
        return None

    def get_payment_amount(self, payment):
        payment_detail = PaymentDetail.objects.filter(
            payment_id=payment.id).first()
        if payment_detail:
            return payment_detail.amount
        return None
