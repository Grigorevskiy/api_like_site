from rest_framework.generics import *
from api.serializers.order import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import Journey, Order
from rest_framework.permissions import IsAdminUser


class OrderAPIView(ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(journey_id=self.kwargs.get('pk', 0)).select_related('user')

    def perform_create(self, serializer):
        journey = Journey.objects.get(pk=self.kwargs.get('pk'))
        persons = serializer.validated_data['persons']

        if journey.sale_price:
            total = int(persons) * journey.sale_price
        else:
            total = int(persons) * journey.price

        serializer.save(user=self.request.user, journey_id=self.kwargs.get('pk'), total=total)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_pk'

    def get_queryset(self):
        return Order.objects.filter(journey_id=self.kwargs.get('pk', 0))
