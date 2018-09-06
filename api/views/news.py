
from rest_framework import viewsets
from api.serializers.news import NewsSerializer
from api.models import News
from rest_framework import permissions


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = NewsSerializer

    queryset = News.objects.all()
