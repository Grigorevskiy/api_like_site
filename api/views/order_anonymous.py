from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers.order_anonymous import OrderAnonymousSerializer
from api.models import OrderAnonymous
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from like_api.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


class OrderAnonymousViewSet(viewsets.ModelViewSet):

    queryset = OrderAnonymous.objects.all()
    serializer_class = OrderAnonymousSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
