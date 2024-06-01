from rest_framework import serializers
from api.models.paymentdetail import PaymentDetail


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ('created_at', 'updated_at',
                  'amount', 'loan_id', 'payment_id',)
        read_only_fields = ('created_at',)
        # fields = '__all__'
