from time import sleep
import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class TestPost:
    @pytest.mark.django_db
    def test_create_user(self, users_login_data):
        response = APIClient().post(
            "/users/api/v1/",
            data=users_login_data,
            format='json'
        )
        assert response.status_code in (200,201)

    @pytest.mark.django_db
    def test_login(self, users_login_data):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            email=users_login_data["email"],
            password=users_login_data["password"],
            full_name=users_login_data["full_name"]
        )

        client = APIClient()
        r = client.post(
            "/users/api/v1/token/",
            data={
                "email": users_login_data["email"],
                "password": users_login_data["password"]
            },
            format="json"
        )
        assert r.status_code in [200, 201]
        assert 'access' in r.json()
        assert 'refresh' in r.json()





