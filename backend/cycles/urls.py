from django.urls import path, include
from rest_framework import routers

from .views import MenstrualCycleViewSet, MedicationViewSet, MedicationCategoryViewSet, TrackingDataViewSet


router = routers.DefaultRouter()
router.register(r"", MenstrualCycleViewSet, "cycles")
router.register(r"medication", MedicationViewSet, "medication")
router.register(r"medication/category", MedicationCategoryViewSet, "medication-category")
router.register(r"log", TrackingDataViewSet, "log")

urlpatterns = [
    path("", include(router.urls)),
]
