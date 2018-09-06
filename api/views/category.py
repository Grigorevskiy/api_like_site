
from api.serializers.category import CategorySerializer
from api.models import Category
from api.permissions import IsAdminOrReadOnly

from rest_framework.generics import *


class CategoryCreateListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    queryset = Category.objects.all()


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs.get('pk', 0))
