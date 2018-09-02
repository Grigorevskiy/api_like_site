from rest_framework import viewsets
from api.serializers.journey import JourneySerializer
from api.models import Journey


class JourneyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
