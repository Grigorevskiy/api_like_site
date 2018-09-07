
from api.serializers.journey import JourneySerializer
from api.models import Journey
from rest_framework.generics import *
from api.permissions import IsAdminOrReadOnly


class JourneyCreateListAPIView(ListCreateAPIView):
    serializer_class = JourneySerializer
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Journey.objects.all()


class JourneyDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JourneySerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        return Journey.objects.filter(id=self.kwargs.get('pk', 0))
