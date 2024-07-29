from django_filters.filterset import filterset_factory
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Note, Symptom, SymptomCategory
from .serializers import NoteSerializer, SymptomSerializer, SymptomCategorySerializer
from lunarfit.filters import DateRangeFilterSet
from users.views import UserModelViewSet


class SymptomViewSet(UserModelViewSet):
    serializer_class = SymptomSerializer
    http_method_names = ["get", "post" ,"delete", "patch"]
    filterset_class = filterset_factory(Symptom, DateRangeFilterSet, ["date"])


class SymptomCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomCategorySerializer
    queryset = SymptomCategory.objects.all()
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]


class NoteViewSet(UserModelViewSet):
    serializer_class = NoteSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    # filterset_fields = {"date": ["lt", "gt"]}
    filterset_class = filterset_factory(Note, DateRangeFilterSet, ["date"])
