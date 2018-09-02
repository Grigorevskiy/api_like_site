from rest_framework import viewsets
from api.serializers.order_anonymous import OrderAnonymousSerializer
from api.models import OrderAnonymous
from django.core.mail import send_mail
from like_api.settings import EMAIL_HOST_USER


class OrderAnonymousViewSet(viewsets.ModelViewSet):
    queryset = OrderAnonymous.objects.all()
    serializer_class = OrderAnonymousSerializer

    def perform_create(self, serializer):
        send_mail('Here will be title of email!',
                  'Here is a text for email!!',
                  EMAIL_HOST_USER,
                  [serializer.validated_data['email']],
                  html_message='<html><body><h1>Hello, world</h1></body></html>',
                  fail_silently=False)

        serializer.save()
