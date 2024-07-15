from django_filters.filterset import filterset_factory
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import MenstrualCycle, Phase, MedicationCategory
from .serializers import (
    MenstrualCycleSerializer,
    PhaseSerializer,
    MedicationSerializer,
    MedicationCategorySerializer,
)
from lunarfit.filters import DateFromToRangeFilterSet
from users.views import UserModelViewSet


class MenstrualCycleViewSet(ModelViewSet):
    """Endpoint to list users' menstrual cycle(s) in the specified date range.
    For receiving only cycle of current day 'start_after' is current date."""

    serializer_class = MenstrualCycleSerializer
    queryset = MenstrualCycle.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    filterset_class = filterset_factory(
        MenstrualCycle, DateFromToRangeFilterSet, ["user", "start", "end"]
    )
    # filterset_fields = ["start", "end"]


class PhaseViewSet(ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]


class MedicationViewSet(UserModelViewSet):
    serializer_class = MedicationSerializer
    http_method_names = ["get", "post", "patch", "delete"]


class MedicationCategoryViewSet(ModelViewSet):
    serializer_class = MedicationCategorySerializer
    queryset = MedicationCategory.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
