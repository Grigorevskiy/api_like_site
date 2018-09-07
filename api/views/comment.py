
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from api.serializers.comment import CommentSerializer
from api.models import Comment
from ..permissions import IsOwner
from rest_framework import permissions


class JourneyCommentsView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(journey_id=self.kwargs.get('pk', 0)).select_related('user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, journey_id=self.kwargs.get('pk', 0))


class JourneyCommentsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'com_pk'

    def get_queryset(self):
        return Comment.objects.filter(journey_id=self.kwargs.get('pk', 0))