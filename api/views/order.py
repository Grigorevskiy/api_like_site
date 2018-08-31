from django.contrib.auth.models import User
from rest_framework.generics import *
from api.serializers.order import OrderSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Journey, Order
from api.permissions import IsAdminUser


class OrderAPIView(ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(journey_id=self.kwargs.get('pk', 0)).select_related('user')

    def create(self, request, *args, **kwargs):
        order, created = Order.objects.get_or_create(user=request.user, journey_id=self.kwargs.get('pk', 0),
                                                     email_address=request.data['email_address'],
                                                     contact_phone=request.data['contact_phone'],
                                                     total=request.data['total'],)
        order.save()

        return Response()



class OrderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_pk'

    def get_queryset(self):
        return Order.objects.filter(journey_id=self.kwargs.get('pk', 0))
