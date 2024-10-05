from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from dj_rest_auth.app_settings import api_settings
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailAddress
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from startup.users.models import User

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class PasswordResetView(GenericAPIView):
    serializer_class = api_settings.PASSWORD_RESET_SERIALIZER
    permission_classes = (AllowAny,)
    throttle_scope = "dj_rest_auth"

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            EmailAddress.objects.get(**serializer.validated_data)
        except EmailAddress.DoesNotExist:
            return Response(
                {"detail": "Account does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save()
        return Response(
            {"detail": "Password reset e-mail has been sent."},
            status=status.HTTP_200_OK,
        )

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({"error": "A user with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
