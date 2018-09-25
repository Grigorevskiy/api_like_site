
from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # liked_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'journey',
            'user',
            'body',
            'likes',
            'created_at',
            # 'liked_by_me',
        ]

        read_only_fields = ['user', 'likes', 'is_liked_by_me',]
    # def get_liked_by_me(self, obj):
    #     if self.context['request'].user.id in obj.liked_by:
    #         return True
    #     return False
