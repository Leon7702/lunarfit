from django.urls import path, include
from rest_framework import routers

from .views import SymptomViewSet, SymptomCategoryViewSet, NoteViewSet


router = routers.DefaultRouter()
router.register(r"notes", NoteViewSet, "notes")
router.register(r"symptoms", SymptomViewSet, "symptoms")
router.register(r"symptoms/categories", SymptomCategoryViewSet, "symptom_categories")

urlpatterns = [
    path("", include(router.urls)),
]
