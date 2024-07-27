from django.urls import path, include
from rest_framework import routers

from .views import MenstrualCycleViewSet, MedicationViewSet, MedicationCategoryViewSet, TrackingDataViewSet, TypeViewSet


router = routers.DefaultRouter()
router.register(r"phases", MenstrualCycleViewSet, "cycles")
router.register(r"log/type", TypeViewSet, "log-type")
router.register(r"log", TrackingDataViewSet, "log")
router.register(r"medication/category", MedicationCategoryViewSet, "medication-category")
router.register(r"medication", MedicationViewSet, "medication")


urlpatterns = [
    path("", include(router.urls)),
]
