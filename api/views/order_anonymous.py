
from api.serializers.order_anonymous import OrderAnonymousSerializer
from api.models import OrderAnonymous
from django.core.mail import send_mail
from like_api.settings import EMAIL_HOST_USER
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser


class OrderAnonymousCreateAPIView(CreateAPIView):
    serializer_class = OrderAnonymousSerializer

    queryset = OrderAnonymous.objects.all()

    def perform_create(self, serializer):
        send_mail('Here will be title of email!',
                  'Here is a text for email!!',
                  EMAIL_HOST_USER,
                  [serializer.validated_data['email']],
                  html_message='<html><body><h1>Hello, world</h1></body></html>',
                  fail_silently=False)

        serializer.save()


class OrderAnonymousListAPIView(ListAPIView):
    serializer_class = OrderAnonymousSerializer
    permission_classes = (IsAdminUser,)

    queryset = OrderAnonymous.objects.all()


class OrderAnonymousDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderAnonymousSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return OrderAnonymous.objects.filter(orderanonymous_id=self.kwargs.get('pk', 0))
