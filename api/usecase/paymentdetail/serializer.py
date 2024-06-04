from rest_framework import serializers
from api.models.paymentdetail import PaymentDetail


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ('id','created_at', 'updated_at',
                  'amount', 'loan_id', 'payment_id',)
        read_only_fields = ('id','created_at',)


class PaymentDetailObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ('id','created_at', 'updated_at', 'amount', 'loan_id',)
        read_only_fields = ('id','created_at', 'payment_id')