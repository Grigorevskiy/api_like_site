
from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField(required=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'email_address',
            'contact_phone',
            'persons',
            'journey',
            'user',
            'created_at',
            'updated_at',
        ]

        read_only_fields = ['status', 'total']
