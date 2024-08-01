import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .models import Trs, Workout
from users.models import User


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def user1() -> User:
    return User.objects.create_user(email="user1@example.com", password="string")


@pytest.fixture()
def user2() -> User:
    return User.objects.create_user(email="user2@example.com", password="string")


# @pytest.mark.django_db
# def test_create_note(api_client, user1) -> None:
#     api_client.force_authenticate(user1)
#     data = {"date": "2024-07-14", "content": "This is a test note!"}
#     response = api_client.post("/api/notes/", data, format="json")
#     assert response.status_code == status.HTTP_201_CREATED
