from rest_framework import serializers

from .models import Note, SymptomCategory, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class SymptomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomCategory
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
