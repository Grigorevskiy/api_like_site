
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from api.serializers.journey import JourneySerializer
from api.models import Journey
from api.permissions import IsAdminOrReadOnly


class JourneyViewSet(viewsets.ModelViewSet):
    serializer_class = JourneySerializer
    permission_classes = (IsAdminOrReadOnly,)

    filter_backends = (SearchFilter,)
    search_fields = ('title',)

    queryset = Journey.objects.all()
