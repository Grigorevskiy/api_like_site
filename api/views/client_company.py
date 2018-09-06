
from rest_framework import viewsets
from api.serializers.client_company import ClientCompanySerializer
from api.models import ClientCompany
from rest_framework import permissions


class ClientCompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ClientCompanySerializer

    queryset = ClientCompany.objects.all()
