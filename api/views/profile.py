
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from api.serializers.profile import ProfileSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).select_related('profile')

    def update(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        user.profile.first_name = 'Lorem'
        user.save()
