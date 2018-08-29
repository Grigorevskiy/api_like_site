from rest_framework import viewsets
from api.serializers.faq import FaqSerializer
from api.models import Faq


class FaqViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
