from rest_framework import serializers
from ..models import News, NewsPhoto


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsPhoto
        fields = ('image',)


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    images = NewsImageSerializer(source='news_image', many=True, read_only=True)

    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'short_description',
            'body',
            'created_at',
            'published',
            'images',
            'url',
        ]
