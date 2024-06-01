from rest_framework import serializers
from api.models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('score', 'external_id', 'status',
                  'updated_at', 'created_at', 'preapproved_at')
        read_only_fields = ('created_at',)