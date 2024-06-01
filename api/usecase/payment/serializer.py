from rest_framework import serializers
from api.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('created_at', 'updated_at', 'external_id',
                  'total_amount', 'status', 'paid_at', 'customer_id',)
        read_only_fields = ('created_at',)
        # fields = '__all__'
