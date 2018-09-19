from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers.comment import CommentSerializer
from api.models import Comment
from ..permissions import IsOwner
from rest_framework import permissions, status, viewsets


class JourneyCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # def get_permissions(self):
    #     if self.action in ["list", "create"]:
    #         return self.permission_classes(permissions.IsAuthenticatedOrReadOnly,)
    #
    #     return self.permission_classes(IsOwner,)

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

    @action(methods=['post'], detail=False, url_path='(?P<pk>[0-9]+)/like')
    def add_like(self, request, **kwargs):

        comment = get_object_or_404(Comment, pk=kwargs.get('pk', 0))

        if request.user.id not in comment.liked_by:
            comment.liked_by.append(request.user.id)
            comment.likes += 1
            comment.save()

        return Response(status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False, url_path='(?P<pk>[0-9]+)/unlike')
    def delete_like(self, request, **kwargs):

        comment = get_object_or_404(Comment, pk=kwargs.get('pk', 0))

        if request.user.id in comment.liked_by:
            comment = get_object_or_404(Comment, pk=kwargs.get('pk', 0))
            comment.liked_by.remove(request.user.id)
            comment.likes -= 1
            comment.save()

        return Response(status=status.HTTP_200_OK)
