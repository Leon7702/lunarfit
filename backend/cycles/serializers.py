from rest_framework import serializers

from .models import MenstrualCycle, Phase, Medication, MedicationCategory, TrackingData, Type


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = "__all__"


class MenstrualCycleSerializer(serializers.ModelSerializer):
    phases = PhaseSerializer(many=True, read_only=True)

    class Meta:
        model = MenstrualCycle
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class MedicationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationCategory
        fields = "__all__"


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }
    
    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class TrackingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingData
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
