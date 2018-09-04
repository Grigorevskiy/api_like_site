
from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'category_logo',
            'url',
        ]