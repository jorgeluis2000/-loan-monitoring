from rest_framework import serializers
from api.models.loan import Loan


class LoanSerializer(serializers.ModelSerializer):
    customer_external_id = serializers.SerializerMethodField(
        'get_customer_external_id')
    class Meta:
        model = Loan
        fields = ('external_id', 'customer_id', 'customer_external_id', 'maximum_payment_date' 'amount', 'outstanding', 'status')
        read_only_fields = ('created_at', 'status',)
        
    def get_customer_external_id(self, loan):
        return loan.external_id