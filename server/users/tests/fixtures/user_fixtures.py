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
def users_test_data():
    return {
        'email': 'test@user.com',
        'password': 'test123',
        'full_name': 'Authorized User',
        'is_active': True,
        'is_staff': False,
        'is_superuser': False
    }

@pytest.fixture
def auth_client(db, users_test_data):
    User = get_user_model()
    users_test_data=users_test_data
    user = User.objects.create_user(
       **users_test_data
    )

    client = APIClient()
    response = client.post(
        "/users/api/v1/token/",
        data={
            'email':users_test_data['email'],
            'password': users_test_data['password'],
        },
        format="json"
    )

    assert response.status_code == 200, response.json()
    token = response.json().get("access")


    # добавляем токен в хедер
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    return client, user