
from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'category_logo',
            'url',
        ]
