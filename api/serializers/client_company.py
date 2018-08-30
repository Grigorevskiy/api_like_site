from rest_framework import serializers
from ..models import ClientCompany


class ClientCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientCompany
        fields = [
            'id',
            'title',
            'logo',
            'site',
            'url',
        ]
