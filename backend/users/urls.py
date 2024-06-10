from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, UserCreateView, UserListView, UserView


urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register_user"),
    path("", UserListView.as_view(), name="list_users"),
    path("<int:pk>", UserView.as_view(), name="retrieve_patch_delete_user"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
