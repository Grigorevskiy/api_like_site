
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from api.serializers.comment import CommentSerializer
from api.models import Comment
from ..permissions import IsOwner


class JourneyCommentsCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     return Comment.objects.filter(journey_id=self.kwargs.get('pk', 0))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, journey_id=self.kwargs.get('pk', 0))


class JourneyCommentsListAPIView(ListAPIView):
    authentication_classes = [SessionAuthentication]

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(journey_id=self.kwargs.get('pk', 0))


class JourneyCommentsDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'com_pk'

    def get_queryset(self):
        return Comment.objects.filter(journey_id=self.kwargs.get('pk', 0))
