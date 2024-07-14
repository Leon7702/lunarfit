from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    UserCreateView,
    UserListView,
    UserView,
    ProfileViewSet,
    MenstrualCycleViewSet,
    SymptomViewSet,
    SymptomCategoryViewSet,
    NoteViewSet,
    MedicationViewSet,
    MedicationCategoryViewSet,
    ContraceptiveViewSet
)


router = routers.DefaultRouter()
router.register(r"profile", ProfileViewSet, "profile")
router.register(r"cycle", MenstrualCycleViewSet, "cycle")
router.register(r"symptoms", SymptomViewSet, "symptoms")
router.register(r"symptoms/categories", SymptomCategoryViewSet, "symptom-categories")
router.register(r"notes", NoteViewSet, "notes")
router.register(r"medication", MedicationViewSet, "medication")
router.register(r"medication/categories", MedicationCategoryViewSet, "medication-categories")
router.register(r"contraceptives", ContraceptiveViewSet, "contraceptives")


urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("<int:pk>", UserView.as_view(), name="user-detail"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
