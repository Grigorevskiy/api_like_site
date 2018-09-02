from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    class Meta:
        model = Order
        fields = [
            'id',
            'email_address',
            'contact_phone',
            'total',
            'persons',
            'journey',
            'user',
            'status',
            'created_at',
            'updated_at',
        ]

