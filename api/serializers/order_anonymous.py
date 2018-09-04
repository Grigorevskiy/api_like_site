
from rest_framework import serializers
from ..models import OrderAnonymous


class OrderAnonymousSerializer(serializers.HyperlinkedModelSerializer):

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
            'contacted',
            'url',
        ]
