from time import sleep

import pytest
from django.db import connection
from products.models import CustomProduct
from pytest_django.fixtures import client
from wishlists.models import Wishlist


@pytest.mark.django_db
class TestWishlists:
    def test_wishlist_table_exist_in_DB(self):
        table = Wishlist._meta.db_table
        tables = set(connection.introspection.table_names())
        assert table in tables


    def test_add_product_to_wishlist(self, auth_client, auth_client_superuser ,product_data):
        '''
        add a product to wishlist db
        :param auth_client:
        :param auth_client_superuser:
        :param product_data:
        :return: bool
        '''
        client, user = auth_client
        su_client, su_user = auth_client_superuser

        new_product = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        ).json()

        new_product_to_wishlist = client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': new_product['id']
            },
            format='json'
        )

        assert new_product_to_wishlist.status_code in [200, 201]
        assert new_product_to_wishlist.json()['user'] == user.id
        assert new_product_to_wishlist.json()['product'] == new_product['id']


    def test_add_duplicate_product_to_wishlist(self, auth_client, auth_client_superuser ,product_data):
        '''
        add a product to wishlist db
        :param auth_client:
        :param auth_client_superuser:
        :param product_data:
        :return: bool
        '''
        client, user = auth_client
        su_client, su_user = auth_client_superuser

        new_product = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        ).json()

        new_product_to_wishlist = client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': new_product['id']
            },
            format='json'
        )

        new_product_to_wishlist2 = client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': new_product['id']
            },
            format='json'
        )


        #sleep(500)

        assert new_product_to_wishlist2.status_code == 400
        assert "detail" in new_product_to_wishlist2.json()
        assert new_product_to_wishlist2.json()["detail"] == f"Rec with user {user.id} and {new_product['id']} already exists"




