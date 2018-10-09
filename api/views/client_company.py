
from rest_framework import viewsets
from api.serializers.client_company import ClientCompanySerializer
from api.models import ClientCompany
from api.permissions import IsAdminOrReadOnly


class ClientCompanyViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCompanySerializer
    permission_classes = (IsAdminOrReadOnly,)

    queryset = ClientCompany.objects.all()
