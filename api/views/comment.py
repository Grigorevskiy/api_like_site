
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers.comment import CommentSerializer
from api.models import Comment
from ..permissions import IsOwner
from rest_framework import permissions, status, viewsets
from django_redis import cache
from django.core.cache import cache


class JourneyCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    queryset = Comment.objects.all()

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):

        comment = get_object_or_404(self.get_queryset().filter(pk=pk))

        redis_key_for_comment = 'likers-{}'.format(comment.pk)

        if not cache.has_key(redis_key_for_comment):
            cache.set(redis_key_for_comment, comment.liked_by)

        cached_likers = cache.get(redis_key_for_comment)

        if request.user.id not in cached_likers:
            cached_likers.append(request.user.id)
            cache.set(redis_key_for_comment, cached_likers)

        if len(cache.get(redis_key_for_comment)) % 10 == 0:
            comment.liked_by = cached_likers
            comment.save()

        return Response(status=status.HTTP_200_OK)

    @action(methods=['DELETE'], detail=True)
    def dislike(self, request, pk, *args, **kwargs):

        comment = get_object_or_404(self.get_queryset().filter(pk=pk))
        cached_likers = cache.get('likers-{}'.format(comment.pk))

        if request.user.id in cached_likers:
            cached_likers.remove(request.user.id)
            cache.set('likers-{}'.format(comment.pk), cached_likers)

        return Response(status=status.HTTP_200_OK)

    # @action(methods=['GET', 'DELETE'], detail=True)
    # def like(self, request, pk, *args, **kwargs):
    #
    #     comment = get_object_or_404(self.get_queryset().filter(pk=pk))
    #
    #     if not cache.has_key('likers-{}'.format(comment.pk)):
    #         cache.set('likers-{}'.format(comment.pk), comment.liked_by)
    #
    #     cached_likers = cache.get('likers-{}'.format(comment.pk))
    #
    #     if request.method == 'GET':
    #         if request.user.id not in cached_likers:
    #             cached_likers.append(request.user.id)
    #             cache.set('likers-{}'.format(comment.pk), cached_likers)
    #
    #         if len(cache.get('likers-{}'.format(comment.pk))) % 10 == 0:
    #             comment.liked_by = cached_likers
    #             comment.save()
    #
    #     else:
    #         if request.user.id in cached_likers:
    #             cached_likers.remove(request.user.id)
    #             cache.set('likers-{}'.format(comment.pk), cached_likers)
    #
    #     return Response(status=status.HTTP_200_OK)
