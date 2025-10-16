import pytest

@pytest.mark.django_db
class TestProduct:
    def test_post_new_product(self, auth_client_superuser ,product_data):
        client = auth_client_superuser

        response = client.post(
            '/products/api/v1/',
            data=product_data
        )

        assert response.status_code == 201
