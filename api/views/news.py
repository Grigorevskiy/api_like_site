
from api.serializers.news import NewsSerializer
from api.models import News
from api.permissions import IsAdminOrReadOnly
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)

    queryset = News.objects.all()
