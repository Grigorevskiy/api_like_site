from rest_framework import viewsets
from api.serializers.news import NewsSerializer
from api.models import News


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
