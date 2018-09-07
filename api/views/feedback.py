
from rest_framework import viewsets
from api.models import Feedback
from rest_framework.permissions import IsAuthenticated
from api.serializers.feedback import FeedBackSerializer


class FeedBackViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FeedBackSerializer

    queryset = Feedback.objects.all()
