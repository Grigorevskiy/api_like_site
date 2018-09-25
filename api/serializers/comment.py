
from rest_framework import serializers
from ..models import Comment
from django_redis import cache
from django.core.cache import cache


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'journey',
            'user',
            'body',
            'likes',
            'created_at',
        ]

        read_only_fields = ['user', 'likes',]

    def get_likes(self, obj):
        if not cache.has_key('likers-{}'.format(obj.pk)):
            cache.set('likers-{}'.format(obj.pk), obj.liked_by)

        likes = len(cache.get('likers-{}'.format(obj.pk)))
        return likes
