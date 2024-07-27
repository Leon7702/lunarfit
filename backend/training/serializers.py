from rest_framework import serializers

from .models import Sport, Trs, Workout


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class TrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trs
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data: dict):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
