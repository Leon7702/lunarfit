from django_filters import DateFromToRangeFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import MenstrualCycle, Phase, Profile, User
from .permissions import UserPermission
from .serializers import (CustomTokenObtainPairSerializer,
                          MenstrualCycleSerializer, PhaseSerializer,
                          ProfileSerializer, UserSerializer)


class UserCreateView(CreateAPIView):
    """Endpoint for creating a new User"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListView(ListAPIView):
    """Endpoint for listing all Users"""

    queryset = User.objects.all().order_by("email")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "patch"]


class CycleFilterSet(FilterSet):
    
    start = DateFromToRangeFilter()
    end = DateFromToRangeFilter()

    class Meta:
        model = MenstrualCycle
        fields = ['start', 'end']


class MenstrualCycleViewSet(viewsets.ModelViewSet):
    """Endpoint to list users' menstrual cycle(s) in the specified date range.
    For receiving only cycle of current day 'start_after' is current date."""
    serializer_class = MenstrualCycleSerializer
    queryset = MenstrualCycle.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CycleFilterSet






class PhaseViewSet(viewsets.ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
