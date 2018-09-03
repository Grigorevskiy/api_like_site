from rest_framework import serializers
from ..models import Journey, JourneyPhoto


class JourneyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = JourneyPhoto
        fields = ('image',)


class JourneySerializer(serializers.HyperlinkedModelSerializer):
    images = JourneyImageSerializer(source='photos', many=True, read_only=True)

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
