from django_filters import DateRangeFilter, DateFromToRangeFilter, FilterSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class DateFromToRangeFilterSet(FilterSet):
    """
    Generic filter for a date range from start to end. Takes a Django model as parameter.
    Allows filtering with before and after parameters for both start and end.
    """

    start = DateFromToRangeFilter()
    end = DateFromToRangeFilter()


class DateRangeFilterSet(FilterSet):
    """
    Generic filter for a date range. Takes a Django model as parameter.
    Allows filtering with before and after parameters, instead of just one date.
    """

    date = DateFromToRangeFilter(label="Inclusive")
    date_keyword = DateRangeFilter(field_name="date")

