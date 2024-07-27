from django.urls import path, include
from rest_framework import routers

from .views import SportViewSet, TrsViewSet, WorkoutViewSet


router = routers.DefaultRouter()
router.register(r"sports", SportViewSet, "sports")
router.register(r"trs", TrsViewSet, "trs")
router.register(r"workouts", WorkoutViewSet, "workouts")

urlpatterns = [
    path("", include(router.urls)),
]
