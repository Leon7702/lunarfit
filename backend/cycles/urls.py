from django.urls import path, include
from rest_framework import routers

from .views import MenstrualCycleViewSet


router = routers.DefaultRouter()
router.register(r"cycles", MenstrualCycleViewSet, "cycles")

urlpatterns = [
    path("", include(router.urls)),
]
