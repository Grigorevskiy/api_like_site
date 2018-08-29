from rest_framework import viewsets
from api.serializers.document import DocumentSerializer
from api.models import Document


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
