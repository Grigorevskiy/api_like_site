
from rest_framework import viewsets
from api.serializers.document import DocumentSerializer
from api.models import Document
from rest_framework import permissions


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DocumentSerializer

    queryset = Document.objects.all()

