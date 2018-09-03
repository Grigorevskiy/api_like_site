from rest_framework import serializers
from ..models import Faq



class FaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faq
        fields = [
            'id',
            'question',
            'answer',
            'url',
        ]
