from django.db import models
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request


class UserPermission(permissions.BasePermission):
    """
    Custom Permissions for the User Viewset, allowing registration with POST for everyone,
    limiting listing of all Users to admins and everything else to the object owner / admins.
    source: https://ctrlzblog.com/user-registration-with-django-rest-framework
            https://stackoverflow.com/questions/19313314/django-rest-framework-viewset-per-action-permissions
    """

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        return obj == request.user or request.user.is_staff
