
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers.comment import CommentSerializer
from api.models import Comment
from ..permissions import IsOwner
from rest_framework import permissions, status, viewsets
# from django_redis import cache
from django.core.cache import cache


class JourneyCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)

    queryset = Comment.objects.all()

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    # @action(methods=['GET', 'DELETE'], detail=True)
    # def like(self, request, pk, *args, **kwargs):
    #     comment = get_object_or_404(self.get_queryset().filter(pk=pk))
    #
    #     if request.method == 'GET':
    #         if request.user.id not in comment.liked_by:
    #             comment.liked_by.append(request.user.id)
    #             comment.likes += 1
    #     else:
    #         if request.user.id in comment.liked_by:
    #             comment.liked_by.remove(request.user.id)
    #             comment.likes -= 1
    #
    #     comment.save()
    #     return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'DELETE'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(self.get_queryset().filter(pk=pk))

        cached_likers = cache.get('likers{}'.format(comment.pk))

        if request.method == 'GET':
            if request.user.id not in comment.liked_by:
                if cached_likers is None:
                    cached_likers = [request.user.id]
                    cache.set('likers{}'.format(comment.pk), cached_likers)
                    comment.likes += 1
                    comment.save()

                elif request.user.id not in cached_likers:
                    if len(cache.get('likers{}'.format(comment.pk))) < 10:
                        cached_likers.append(request.user.id)
                        cache.set('likers{}'.format(comment.pk), cached_likers)
                        comment.likes += 1
                        comment.save()
                    else:
                        comment.likes += 1
                        for i in cached_likers:
                            comment.liked_by.append(i)
                            comment.save()

                        cache.delete('likers{}'.format(comment.pk))
        else:
            if request.user.id in comment.liked_by:
                comment.liked_by.remove(request.user.id)
                comment.likes -= 1
                comment.save()

            elif request.user.id in cached_likers:
                cached_likers.remove(request.user.id)
                cache.set('likers{}'.format(comment.pk), cached_likers)
                comment.likes -= 1
                comment.save()

        return Response(status=status.HTTP_200_OK)
