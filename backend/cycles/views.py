from django_filters import DateFromToRangeFilter, FilterSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MenstrualCycle, Phase
from .serializers import MenstrualCycleSerializer, PhaseSerializer


class CycleFilterSet(FilterSet):
    start = DateFromToRangeFilter()
    end = DateFromToRangeFilter()

    class Meta:
        model = MenstrualCycle
        fields = ["start", "end"]


class MenstrualCycleViewSet(viewsets.ModelViewSet):
    """Endpoint to list users' menstrual cycle(s) in the specified date range.
    For receiving only cycle of current day 'start_after' is current date."""

    serializer_class = MenstrualCycleSerializer
    queryset = MenstrualCycle.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    filterset_class = CycleFilterSet


class PhaseViewSet(viewsets.ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()
    permission_classes = [IsAuthenticated]
