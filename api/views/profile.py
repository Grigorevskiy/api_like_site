
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from api.models import Profile
from api.permissions import IsOwner
from api.serializers.profile import ProfileSerializer


# class ProfileAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated, IsOwner)
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.select_related('user').all()
#     lookup_field = 'user_id'


class ProfileAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
