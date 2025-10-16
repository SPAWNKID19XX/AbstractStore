import pytest
from pytest_django.fixtures import client

from server.users.tests.fixtures.user_fixtures import auth_client


@pytest.mark.django_db
class TestProduct:
    def test_post_new_product(self,auth_client_superuser ,product_data):
        client, user = auth_client_superuser
        response = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        print(response.json())
        assert response.status_code == 201
        assert response.json()['title'] == product_data['title']
