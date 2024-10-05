from rest_framework import serializers

from startup.users.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer

class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }

class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(
        style={"input_type": "password"},
        required=True,
        allow_blank=False,
    )


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    