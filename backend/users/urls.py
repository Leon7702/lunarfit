from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    UserCreateView,
    UserListView,
    UserView,
    ProfileViewSet,
    OnboardingViewSet,
    ContraceptiveViewSet,
)


router = routers.DefaultRouter()
# The order of routing seems to matter here.
# If profile is registerd before profile/contraceptive the schema picks up the endpoint, but the route returns 404
router.register(r"profile/contraceptive", ContraceptiveViewSet, "contraceptive")
router.register(r"profile", ProfileViewSet, "profile")
router.register(r"onboarding", OnboardingViewSet, "onboarding")

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("<int:pk>/", UserView.as_view(), name="user-detail"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
