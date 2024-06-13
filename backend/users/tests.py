from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from .models import CustomUser


class RegisterTest(APITestCase):
    def test_register_success(self):

        url = "/api/users/register/"
        data = {"email": "user@example.com", "password": "string"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, "user@example.com")

    def test_register_fail_duplicate_email(self):

        url = "/api/users/register/"
        data = {"email": "user@example.com", "password": "string"}

        self.client.post(url, data)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserPermissionsTest(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            email="user1@example.com", password="string"
        )
        self.user2 = CustomUser.objects.create_user(
            email="user2@example.com", password="string"
        )
        self.superuser = CustomUser.objects.create_superuser(
            email="superuser@example.com", password="string"
        )

    def tearDown(self):
        pass

    def test_admin_can_list_users(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_list_users(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_access_own_data(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(f"/api/users/{self.user2.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_access_other_user_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/{self.user2.id}")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
