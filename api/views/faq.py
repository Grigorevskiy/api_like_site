
from rest_framework import viewsets
from api.serializers.faq import FaqSerializer
from api.models import Faq
from rest_framework import permissions


class FaqViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = FaqSerializer

    queryset = Faq.objects.all()

