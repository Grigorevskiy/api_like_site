from rest_framework import viewsets
from api.serializers.client_company import ClientCompanySerializer
from api.models import ClientCompany


class ClientCompanyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ClientCompany.objects.all()
    serializer_class = ClientCompanySerializer
