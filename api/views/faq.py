
from rest_framework import viewsets
from api.serializers.faq import FaqSerializer
from api.models import Faq
from api.permissions import IsAdminOrReadOnly


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Faq.objects.all()
