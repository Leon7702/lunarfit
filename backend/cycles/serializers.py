from rest_framework import serializers

from .models import MenstrualCycle, Phase, Medication, MedicationCategory


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = "__all__"


class MenstrualCycleSerializer(serializers.ModelSerializer):
    phases = PhaseSerializer(many=True, read_only=True)

    class Meta:
        model = MenstrualCycle
        fields = "__all__"


class MedicationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationCategory
        fields = "__all__"


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
