
from api.serializers.journey import JourneySerializer
from api.models import Journey
from rest_framework.generics import *
from rest_framework import permissions


class JourneyCreateAPIView(CreateAPIView):
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAdminUser]


class JourneyListAPIViews(ListAPIView):
    serializer_class = JourneySerializer

    queryset = Journey.objects.all()


class JourneyRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Journey.objects.filter(id=self.kwargs.get('pk', 0))


