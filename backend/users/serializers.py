#!/usr/bin/env python3

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from .models import CustomUser
from rest_framework import exceptions, serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

        def create(self, validated_data):
            user = CustomUser.objects.create_user(**validated_data)
            return user

        def to_representation(self, instance):
            """Overriding to remove Password Field when returning Data"""
            ret = super().to_representation(instance)
            ret.pop("password", None)
            return ret


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        credentials = {
            "email": attrs.get("email"),
            "password": attrs.get("password")
        }

        user = authenticate(**credentials)

        if user:
            
            data = {}
            refresh = self.get_token(user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data
        else:
            raise exceptions.AuthenticationFailed("No active account found with the given credentials")

