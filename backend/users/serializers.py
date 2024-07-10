from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import (
    Medication,
    MedicationCategory,
    MenstrualCycle,
    Note,
    Phase,
    Profile,
    SymptomCategory,
    Symptom,
    User,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "profile"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
            "profile": {"read_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict):
        for key in validated_data.keys():
            setattr(instance, key, validated_data.get(key))

        instance.set_password(validated_data.get("password", instance.password))
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        credentials = {"email": attrs.get("email"), "password": attrs.get("password")}

        user = authenticate(**credentials)

        if user:

            data = {}
            refresh = self.get_token(user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data
        else:
            raise exceptions.AuthenticationFailed(
                "No active account found with the given credentials"
            )


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = "__all__"


class MenstrualCycleSerializer(serializers.ModelSerializer):
    phases = PhaseSerializer(many=True, read_only=True)

    class Meta:
        model = MenstrualCycle
        fields = "__all__"


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = "__all__"


class SymptomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomCategory
        fields = "__all__"


class MedicationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationCategory
        fields = "__all__"


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
