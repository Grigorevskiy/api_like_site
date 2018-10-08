
import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
from api.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(User.is_active)
        )


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
        ]

        extra_kwargs = {'password': {'write_only': True}}

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exist")
        return value

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exist")
        return value

    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        account_activation_token = AccountActivationTokenGenerator()
        user_obj = User(username=validated_data.get('username'),
                        email=validated_data.get('email'))
        user_obj.set_password(validated_data.pop('password'))
        user_obj.is_active = False
        user_obj.save()

        Token.objects.create(user=user_obj, token=account_activation_token.make_token(user_obj))

        current_site = "http://127.0.0.1:8000"
        # current_site = get_current_site(request)

        message = render_to_string('acc_active_email.html', {
            'user': user_obj,
            'domain': current_site,
            # 'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user_obj.id)).decode(),
            'token': account_activation_token.make_token(user_obj),
        })
        mail_subject = 'Activate your blog account.'
        to_email = [validated_data['email']]
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return user_obj


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, data):
        if not self.context['request'].user.check_password(data['old_password']):
            raise serializers.ValidationError("Old Password is not correct")
        return data


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
