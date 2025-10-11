import pytest
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