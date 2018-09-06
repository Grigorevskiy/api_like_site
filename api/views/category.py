
from api.serializers.category import CategorySerializer
from api.models import Category

from rest_framework.generics import *
from rest_framework import permissions


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    queryset = Category.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    queryset = Category.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs.get('pk', 0))
