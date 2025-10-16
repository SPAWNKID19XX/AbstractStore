from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import pytest

class TestUpdate:
    @pytest.mark.django_db
    def test_patch_logged_user(self, auth_client):
        client, user = auth_client

        response = client.patch(
            f"/users/api/v1/{user.id}/",
            data={"full_name": "Patched Name"},
            format="json"
        )

        assert response.status_code == 200
        assert response.json()['full_name'] == "Patched Name"

    @pytest.mark.django_db
    def test_put_logged_user(self, auth_client):
        client, user = auth_client

        response = client.put(
            f"/users/api/v1/{user.id}/",
            data={
                "email":user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )
        User = get_user_model()
        assert User.objects.filter(id=user.id).exists()


    @pytest.mark.django_db
    def test_patch_not_logged_user(self, users_test_data):
        user = get_user_model().objects.create_user(
            **users_test_data
        )

        client = APIClient()
        response = client.patch(
            f"/users/api/v1/{user.id}/",
            data={"full_name": "Patched Name"},
            format="json"
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_put_not_logged_user(self, users_test_data):
        user = get_user_model().objects.create_user(
            **users_test_data
        )

        client = APIClient()

        response = client.put(
            f"/users/api/v1/{user.id}/",
            data={
                "email":user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_delete_not_logged_user(self, users_test_data):
        user = get_user_model().objects.create_user(
            **users_test_data
        )

        client = APIClient()

        response = client.delete(
            f"/users/api/v1/{user.id}/",
            data={
                "email": user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )

        print(response.json())
        assert response.status_code == 401

    @pytest.mark.django_db
    def test_delete_logged_user(self, auth_client):
        client, user = auth_client

        response = client.delete(
            f"/users/api/v1/{user.id}/",
            data={
                "email":user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )

        User = get_user_model()
        user_exists =  User.objects.filter(id=user.id).exists()

        assert response.status_code in (200, 204)
        assert not user_exists


    @pytest.mark.django_db
    def test_patch_superuser(self, auth_client_superuser):
        client, user = auth_client_superuser

        response = client.patch(
            f"/users/api/v1/{user.id}/",
            data={"full_name": "SU Patched Name"},
            format="json"
        )

        assert response.status_code == 200
        assert response.json()['full_name'] == "SU Patched Name"

    @pytest.mark.django_db
    def test_put_superuser(self, auth_client_superuser):
        client, user = auth_client_superuser

        response = client.put(
            f"/users/api/v1/{user.id}/",
            data={
                "email": user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )
        User = get_user_model()
        assert User.objects.filter(id=user.id).exists()


    @pytest.mark.django_db
    def test_delete_su_user(self, auth_client_superuser):
        client, user = auth_client_superuser

        response = client.delete(
            f"/users/api/v1/{user.id}/",
            data={
                "email": user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )

        User = get_user_model()
        user_exists = User.objects.filter(id=user.id).exists()

        assert response.status_code in (200, 204)
        assert not user_exists



