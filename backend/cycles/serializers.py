from rest_framework import serializers

from .models import MenstrualCycle, Phase


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = "__all__"


class MenstrualCycleSerializer(serializers.ModelSerializer):
    phases = PhaseSerializer(many=True, read_only=True)

    class Meta:
        model = MenstrualCycle
        fields = "__all__"
