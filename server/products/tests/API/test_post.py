import pytest
from django.template.defaultfilters import title
from pytest_django.fixtures import client
from products.models import CustomProduct, ProductComments


from server.users.tests.fixtures.user_fixtures import auth_client


@pytest.mark.django_db
class TestProduct:
    def test_post_new_product_by_superuser(self, auth_client_superuser, product_data):
        client, user = auth_client_superuser
        response = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        assert response.status_code == 201
        assert response.json()['title'] == product_data['title']
        assert response.json()['description'] == product_data['description']

    def test_patch_product_by_superuser(self, auth_client_superuser, product_data):
        client, user = auth_client_superuser
        new_product = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        product_data_patched = {
            "title": "patched title"
        }
        response = client.patch(
            f"/products/api/v1/{product_id}/",
            data=product_data_patched,
            format='json'
        )
        assert response.status_code in (200, 201)
        assert response.json()['title'] == "patched title"
        assert response.json()['description'] == product_data['description']

    def test_put_product_by_superuser(self, auth_client_superuser, product_data):
        client, user = auth_client_superuser
        new_product = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        product_data_patched = {
            "title": "putted title",
            'description': "putted description"
        }
        response = client.put(
            f"/products/api/v1/{product_id}/",
            data=product_data_patched,
            format='json'
        )
        assert response.status_code in (200, 201)
        assert response.json()['title'] == "putted title"
        assert response.json()['description'] == "putted description"

    def test_distroy_product_by_superuser(self, auth_client_superuser, product_data):
        client, user = auth_client_superuser
        new_product = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        response = client.delete(
            f"/products/api/v1/{product_id}/",
        )
        product_exists = CustomProduct.objects.filter(id=product_id).exists()
        assert not product_exists

    def test_post_new_product_by_none_superuser(self, auth_client, product_data):
        client, user = auth_client
        response = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        assert response.status_code in [401, 403]

    def test_patch_product_by_none_superuser(self, auth_client_superuser, auth_client, product_data):
        su_client, su_user = auth_client_superuser
        client, user = auth_client
        new_product = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        product_data_patched = {
            "title": "patched title"
        }
        response = client.patch(
            f"/products/api/v1/{product_id}/",
            data=product_data_patched,
            format='json'
        )
        assert response.status_code in [401, 403]

    def test_put_product_by_none_superuser(self, auth_client, auth_client_superuser, product_data):
        client, user = auth_client
        su_client, su_user = auth_client_superuser
        new_product = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        product_data_patched = {
            "title": "putted title",
            'description': "putted description"
        }
        response = client.put(
            f"/products/api/v1/{product_id}/",
            data=product_data_patched,
            format='json'
        )
        assert response.status_code in (401, 403)

    def test_distroy_product_by_none_superuser(self, auth_client, auth_client_superuser, product_data):
        client, user = auth_client
        su_client, su_user = auth_client_superuser
        new_product = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )
        product_id = new_product.json()['id']
        response = client.delete(
            f"/products/api/v1/{product_id}/",
        )
        product_exists = CustomProduct.objects.filter(id=product_id).exists()
        assert product_exists


class TestProductComments:
    def test_exists_column_user_in_products_table(self):
        print()
        fields = [field.name for field in ProductComments._meta.get_fields()]
        assert 'user' in fields
        assert 'product' in fields
        assert 'comment' in fields

    def test_create_new_comment_by_loged_user(self, auth_client_superuser, auth_client, products, comment_data):
        client, user = auth_client
        su_client, su_user = auth_client_superuser
        product1, product2, product3 = products

        new_comment1 = su_client.post(
            f"/products/api/v1/{product1.id}/comments/",
            data={
                **comment_data,
                'product': product1.id,
                'user': user.id,
                'rating': ProductComments.RAITING_VALUES.FIVE
            },
            format='json'
        )
        comm1_id = new_comment1.json()['id']

        new_comment2 = su_client.post(
            f"/products/api/v1/{product2.id}/comments/",
            data={
                **comment_data,
                'product': product2.id,
                'user': user.id,
                'rating': ProductComments.RAITING_VALUES.THREE
            },
            format='json'
        )
        comm2_id = new_comment2.json()['id']

        assert ProductComments.objects.filter(id=comm1_id).exists()
        assert ProductComments.objects.filter(id=comm2_id).exists()


