
from rest_framework import serializers
from ..models import OrderAnonymous


class OrderAnonymousSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderAnonymous
        fields = [
            'id',
            'name',
            'description',
            'person',
            'duration',
            'email',
            'phone',
        ]

        read_only_fields = ['contacted']
