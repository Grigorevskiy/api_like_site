
from rest_framework.serializers import HyperlinkedModelSerializer
from api.models import Feedback


class FeedBackSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = [
            'id',
            'name',
            'body_text',
            'created_at',
            'url',
        ]

        read_only_fields = ('is_published',)
