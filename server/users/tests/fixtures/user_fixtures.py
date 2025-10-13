import pytest, requests
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

BASE_URL = "http://127.0.0.1:8000/"
URL_ADMIN_LOGIN = f'{BASE_URL}/admin/'


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def users_get_response():
    return requests.get(f"{BASE_URL}users/api/v1/").json()


@pytest.fixture
def users_login_data():
    return {
        'email': 'test@user.com',
        'password': 'test123',
        'full_name': 'Boris Isac',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False
    }
