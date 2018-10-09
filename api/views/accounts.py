
from coreapi.compat import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from django.contrib.auth import get_user_model
from django.db.models import Q
from api.serializers.accounts import RegistrationSerializer, ChangePasswordSerializer, LoginSerializer, \
    AccountActivationTokenGenerator
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login, logout


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'Already logged in'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()

        if qs.count() == 1:
            user_obj = qs.first()

            if not user_obj.is_active:
                return Response({'detail': 'Please, confirm your registration first!'}, status=400)

            if user_obj. check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                login(request, user_obj)
                return Response({"token": token})

        return Response({'detail': 'Invalid credentials'}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def activate(request, uidb64, token):
    account_activation_token = AccountActivationTokenGenerator()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

    return Response({"message": "You have activated account, now you can Log In!"})


class ChangePasswordAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_pass = serializer.validated_data.get('new_password', "")

        self.request.user.set_password(new_pass)
        self.request.user.save()
        return Response({"detail": "Password was changed"}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=200)
