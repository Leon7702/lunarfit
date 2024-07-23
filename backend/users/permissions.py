from django.db import models
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request


class UserPermission(permissions.BasePermission):
    """
    Custom Permission for the User Viewset, allowing everthing for admins,
    but limiting access to objects that belong to the user.
    In that case the objects model has to have a foreign key `user`.
    """

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if hasattr(obj, "user"):
            return obj.user == request.user

        return obj == request.user or request.user.is_staff
