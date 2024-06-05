from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (
    CustomTokenObtainPairSerializer,
    GroupSerializer,
    UserModelSerializer,
    UserSerializer,
)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """

#     queryset = Group.objects.all().order_by("name")
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class UserProfileListCreateView(ListCreateAPIView):
    """Generic View for Listing and Creating User Profiles"""

    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
