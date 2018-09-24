
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

    @action(methods=['GET', 'DELETE'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(self.get_queryset().filter(pk=pk))

        if request.method == 'GET':
            if request.user.id not in comment.liked_by:
                comment.liked_by.append(request.user.id)
                comment.likes += 1
        else:
            if request.user.id in comment.liked_by:
                comment.liked_by.remove(request.user.id)
                comment.likes -= 1

        comment.save()
        return Response(status=status.HTTP_200_OK)

    # ACTION WITH CHACHE
    # @action(methods=['GET', 'DELETE'], detail=True)
    # def like(self, request, pk, *args, **kwargs):
    #     comment = get_object_or_404(self.get_queryset().filter(pk=pk))
    #     cached_likers = cache
    #
    #     if request.method == 'GET':
    #         if request.user.id not in comment.liked_by:
    #             if cached_likers < 2:
    #                 likers_to_cache = []
    #                 likers_to_cache.append(request.user.id)
    #                 cached_likers.set("likers", likers_to_cache)
    #                 comment.likes += 1
    #             else:
    #                 comment.liked_by.append(request.user.id)
    #                 comment.likes += 1
    #     else:
    #         if request.user.id in comment.liked_by:
    #             comment.liked_by.remove(request.user.id)
    #             comment.likes -= 1
    #
    #     comment.save()
    #     return Response(status=status.HTTP_200_OK)



    # @action(methods=['post'], detail=False, url_path='(?P<pk>[0-9]+)/like')
    # def add_like(self, request, **kwargs):
    #
    #     comment = get_object_or_404(Comment, pk=kwargs.get('pk', 0))
    #
    #     if request.user.id not in comment.liked_by:
    #         comment.liked_by.append(request.user.id)
    #         comment.likes += 1
    #         comment.save()
    #
    #     return Response(status=status.HTTP_200_OK)
    #
    # @action(methods=['delete'], detail=False, url_path='(?P<pk>[0-9]+)/unlike')
    # def delete_like(self, request, **kwargs):
    #
    #     comment = get_object_or_404(Comment, pk=kwargs.get('pk', 0))
    #
    #     if request.user.id in comment.liked_by:
    #         comment.liked_by.remove(request.user.id)
    #         comment.likes -= 1
    #         comment.save()
    #
    #     return Response(status=status.HTTP_200_OK)
