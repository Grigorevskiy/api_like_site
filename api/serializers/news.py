
from rest_framework import serializers
from ..models import News, NewsPhoto


class NewsImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NewsPhoto
        exclude = ("news",)


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    images = NewsImageSerializer(read_only=True)

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
