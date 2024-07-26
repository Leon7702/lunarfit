from django_filters.filterset import filterset_factory
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Sport, Trs, Workout
from .serializers import SportSerializer, TrsSerializer, WorkoutSerializer
from lunarfit.filters import DateRangeFilterSet
from users.views import UserModelViewSet


class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer
    http_method_names = ["get"]
    queryset = Sport.objects.all().order_by("name")
    permission_classes = [IsAuthenticated]


class TrsViewSet(UserModelViewSet):
    serializer_class = TrsSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = filterset_factory(Trs, DateRangeFilterSet, ["date"])


class WorkoutViewSet(UserModelViewSet):
    serializer_class = WorkoutSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = filterset_factory(Workout, DateRangeFilterSet, ["date"])
