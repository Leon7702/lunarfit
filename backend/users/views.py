from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import (
    Medication,
    MedicationCategory,
    Note,
    Profile,
    SymptomCategory,
    Symptom,
    User,
    Contraceptive,
)
from .permissions import UserPermission
from .serializers import (
    CustomTokenObtainPairSerializer,
    MedicationCategorySerializer,
    MedicationSerializer,
    NoteSerializer,
    ProfileSerializer,
    SymptomSerializer,
    SymptomCategorySerializer,
    UserSerializer,
    ContraceptiveSerializer,
)


class UserCreateView(CreateAPIView):
    """Endpoint for creating a new User"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListView(ListAPIView):
    """Endpoint for listing all Users"""

    queryset = User.objects.all().order_by("email")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "patch"]


@extend_schema(
    parameters=[OpenApiParameter(name="id", type=int, location=OpenApiParameter.PATH)]
)
class SymptomViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer
    # queryset = Symptom.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SymptomFilterSet

    def get_queryset(self):
        # schema generation see https://drf-spectacular.readthedocs.io/en/latest/faq.html#my-get-queryset-depends-on-some-attributes-not-available-at-schema-generation-time
        if getattr(self, "swagger_fake_view", False):  # drf-yasg comp
            return Symptom.objects.none()

        return Symptom.objects.all().filter(user=self.request.user)


class SymptomCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SymptomCategorySerializer
    queryset = SymptomCategory.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]


class MedicationFilterSet(FilterSet):

    start = DateFromToRangeFilter()
    end = DateFromToRangeFilter()

    class Meta:
        model = Medication
        fields = ["start", "end"]


class MedicationViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    # queryset = Medication.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MedicationFilterSet

    def get_queryset(self):
        return Medication.objects.all().filter(user=self.request.user)


class MedicationCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationCategorySerializer
    queryset = MedicationCategory.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]


class NoteFilterSet(FilterSet):

    start = DateFromToRangeFilter()
    end = DateFromToRangeFilter()

    class Meta:
        model = Note
        fields = ["start", "end"]


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NoteFilterSet


class ContraceptiveViewSet(viewsets.ModelViewSet):
    serializer_class = ContraceptiveSerializer
    queryset = Contraceptive.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
