
from rest_framework import serializers
from ..models import Journey, JourneyPhoto


class JourneyImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JourneyPhoto
        fields = [
            'image',
        ]


class JourneySerializer(serializers.HyperlinkedModelSerializer):
    images = JourneyImageSerializer(many=True, source='photos', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='journey-detail')

    class Meta:
        model = Journey
        fields = [
            'id',
            'sku',
            'title',
            'description',
            'durations_days',
            'durations_night',
            'price',
            'sale_price',
            'category',
            'created_at',
            'updated_at',
            'images',
            'url',
        ]
