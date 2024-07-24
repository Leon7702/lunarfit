import pytest
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class RegisterTest(APITestCase):
    def test_register_success(self):

        url = "/api/users/register/"
        data = {"email": "user@example.com", "password": "string"}

        response = self.client.post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().email == "user@example.com"

    def test_register_fail_duplicate_email(self):

        url = "/api/users/register/"
        data = {"email": "user@example.com", "password": "string"}

        self.client.post(url, data)
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class UserProfileTest(APITestCase):
    # loads the users/fixtures/contraceptives.yaml
    fixtures = ["contraceptives"]

    def setUp(self):
        self.user1 = User.objects.create_user(
            email="user1@example.com", password="string"
        )
        self.user2 = User.objects.create_user(
            email="user2@example.com", password="string"
        )
        self.superuser = User.objects.create_superuser(
            email="superuser@example.com", password="string"
        )

    def tearDown(self):
        pass

    def test_admin_can_list_users(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get("/api/users/")
        assert response.status_code == status.HTTP_200_OK

    def test_admin_can_delete_user(self):
        id = self.user2.id
        self.client.force_authenticate(user=self.superuser)
        assert User.objects.count() == 3
        self.client.delete(f"/api/users/{id}/")
        assert User.objects.count() == 2
        response = self.client.get(f"/api/users/{id}/")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_user_cannot_list_users(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/users/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_can_read_own_data(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(f"/api/users/{self.user2.id}/")
        assert response.status_code == status.HTTP_200_OK

    def test_user_can_change_own_email(self):
        """
        Changing the email should provide the same valiadation as creating a new user.
        Since emails are used as username they have to be valid emails and unique.
        """
        id = self.user2.id
        new_email = "new_email@example.com"
        self.client.force_authenticate(user=self.user2)

        response = self.client.patch(
            f"/api/users/{self.user2.id}/", {"email": new_email}
        )

        user = User.objects.get(pk=id)
        assert response.status_code == status.HTTP_200_OK
        assert user.email == new_email

    def test_user_cannot_change_to_invalid_email(self):
        """
        Changing the email should provide the same valiadation as creating a new user.
        Since emails are used as username they have to stay valid.
        """
        id = self.user2.id
        new_email = "invalid"
        self.client.force_authenticate(user=self.user2)

        response = self.client.patch(
            f"/api/users/{self.user2.id}/", {"email": new_email}
        )

        user = User.objects.get(pk=id)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert user.email != new_email

    def test_user_cannot_change_to_existing_email(self):
        """
        Changing the email should provide the same validation as creating a new user.
        Since emails are used as username they have to stay unique.
        """
        id = self.user2.id
        new_email = self.superuser.email
        self.client.force_authenticate(user=self.user2)

        response = self.client.patch(
            f"/api/users/{self.user2.id}/", {"email": new_email}
        )

        user = User.objects.get(pk=id)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert user.email != new_email

    def test_user_can_change_own_password(self):
        """
        Setting a new password has to be done using the users set.password(raw_password) method.
        Otherwise the raw password will be stored in the database.
        """
        id = self.user2.id
        new_password = "definitely_safe"
        self.client.force_authenticate(user=self.user2)

        response = self.client.patch(
            f"/api/users/{self.user2.id}/", {"password": new_password}
        )
        assert response.status_code == status.HTTP_200_OK

        # Don't store the raw password!
        user = User.objects.get(pk=id)
        assert user.password != new_password
        assert user.check_password(new_password) == True

    def test_user_can_delete_own_data(self):
        id = self.user2.id
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f"/api/users/{id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(User.DoesNotExist):
            assert User.objects.get(pk=id)

    def test_user_cannot_read_other_user_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/{self.user2.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_cannot_change_other_user_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(
            f"/api/users/{self.user2.id}/", {"email": "new_email@example.com"}
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_cannot_delete_other_user_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(f"/api/users/{self.user2.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_profile_onboarding_status_updated(self):
        """After a user completed the onboarding, profile.onboarding_finished should be true."""

        assert self.user1.profile.onboarding_finished == False

        data = {
            "user": self.user1.id,
            "workout_frequency": 3,
            "workout_duration": 30,
            "workout_intensity": 5,
            "cycle_duration": 29,
            "menstruation_duration": 4,
        }
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(f"/api/users/onboarding/", data)
        self.user1.refresh_from_db()
        assert response.status_code == status.HTTP_201_CREATED
        assert self.user1.profile.onboarding_finished == True

    def test_user_cannot_read_other_profile_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/profile/{self.user2.id}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_user_can_read_own_profile_data(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/profile/{self.user1.id}/")
        assert response.status_code == status.HTTP_200_OK

    def test_admin_can_read_all_profile_data(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(f"/api/users/profile/")
        assert response.status_code == status.HTTP_200_OK

    def test_user_can_change_own_profile_data(self):
        self.client.force_authenticate(user=self.user1)
        new_name = "Jonathan"
        data = {"first_name": new_name}
        response = self.client.patch(f"/api/users/profile/{self.user1.id}/", data)
        self.user1.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert self.user1.profile.first_name == new_name

    def test_user_cant_move_profile_to_other_user(self):
        """
        The user Foreign key should not be exposed, so users can't change who their profile belongs to.
        When it is set to read_only a user key can be included in the patch request,
        but it should be ignored and not change anything.
        """
        self.client.force_authenticate(user=self.user1)
        new_name = "Jonathan"
        data = {"user": self.user2.id,
                "first_name": new_name}
        response = self.client.patch(f"/api/users/profile/{self.user1.id}/", data)
        self.user1.refresh_from_db()
        self.user2.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert self.user1.profile.first_name == new_name
        assert self.user2.profile.first_name != new_name

    def test_user_can_unset_profile_contraceptive_with_empty_string(self):
        self.client.force_authenticate(user=self.user1)
        data = {"contraceptive": ""}
        response = self.client.patch(f"/api/users/profile/{self.user1.id}/", data)
        self.user1.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert self.user1.profile.contraceptive == None

    def test_user_can_unset_profile_contraceptive_with_json_null(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(
            f"/api/users/profile/{self.user1.id}/",
            b'{"contraceptive": null}',
            content_type="application/json",
        )
        self.user1.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert self.user1.profile.contraceptive == None

    def test_get_contraceptives_list_404_regression(self):
        """
        Regression test for the contraceptive routes.
        The router shadowed the profile/contraceptive route when it was added after /profile.
        The endpoint was still shown in the schema, but resulted in a 404 when trying to retrieve the list.
        Routing profile/contraceptive before profile resolved that.
        """
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/profile/contraceptive/")
        assert response.status_code == status.HTTP_200_OK

    def test_get_contraceptives_list_fixture(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(f"/api/users/profile/contraceptive/")
        # 5 is the number of hormonal contraceptives currently provided by the default fixture
        assert response.data["count"] >= 5
