from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserModelSerializer,
)


class UserCreateView(CreateAPIView):
    """Endpoint for creating a new User"""

    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]


class UserListView(ListAPIView):
    """Endpoint for listing all Users"""

    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAdminUser]


class UserView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    serializer_class = UserModelSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
