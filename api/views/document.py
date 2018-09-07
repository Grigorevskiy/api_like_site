
from rest_framework import viewsets
from api.serializers.document import DocumentSerializer
from api.models import Document
from api.permissions import IsAdminOrReadOnly


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Document.objects.all()
