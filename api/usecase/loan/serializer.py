from rest_framework import serializers
from api.models.loan import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('external_id', 'amount', 'score', 'status', 'contract_version',
                  'maximum_payment_date', 'customer_id', 'take_at', 'updated_at', 'created_at')
        read_only_fields = ('created_at',)
        # fields = '__all__'
