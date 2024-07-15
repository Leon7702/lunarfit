import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .models import Note
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


@pytest.fixture()
def notes1(user1) -> list[Note]:
    return [
        Note.objects.create(user=user1, content="note 1", date="2024-07-14"),
        Note.objects.create(user=user1, content="note 2", date="2024-07-15"),
    ]


@pytest.fixture()
def notes2(user2) -> list[Note]:
    return Note.objects.create(
        user=user2, content="note 3, from user2", date="2024-07-15"
    )


@pytest.mark.django_db
def test_create_note(api_client, user1) -> None:
    api_client.force_authenticate(user1)
    data = {"date": "2024-07-14", "content": "This is a test note!"}
    response = api_client.post("/api/notes/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_list_notes(api_client, notes1, user1):
    api_client.force_authenticate(user1)
    response = api_client.get("/api/notes/")
    assert response.status_code == status.HTTP_200_OK
    assert Note.objects.count() == len(notes1)


@pytest.mark.django_db
def test_list_only_logged_in_users_notes(api_client, notes1, notes2, user1):
    """Only list the logged-in users notes."""

    api_client.force_authenticate(user1)
    response = api_client.get("/api/notes/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == len(notes1)


@pytest.mark.django_db
def test_anonymous_cant_read_note(api_client, notes1):
    """Can access single note object by id, that belongs to authenticated user."""

    id = notes1[0].id
    response = api_client.get(f"/api/notes/{id}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_authenticated_can_read_own_note(api_client, user1, notes1):
    """Can access single note object by id, that belongs to authenticated user."""

    api_client.force_authenticate(user1)
    id = notes1[0].id
    response = api_client.get(f"/api/notes/{id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["content"] == notes1[0].content


@pytest.mark.django_db
def test_authenticated_cant_read_others_note(api_client, user1, notes2):
    """Can access single note object by id, that belongs to authenticated user."""

    api_client.force_authenticate(user1)
    id = notes2.id
    response = api_client.get(f"/api/notes/{id}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
