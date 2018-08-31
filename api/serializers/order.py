from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'email_address',
            'contact_phone',
            'total',
            'persons',
            'journey', 'user', 'status', 'created_at', 'updated_at',
        ]
