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

    def test_add_product_to_wishlist(self, auth_client, auth_client_superuser, product_data):
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

    def test_add_duplicate_product_to_wishlist(self, auth_client, auth_client_superuser, product_data):
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

        assert new_product_to_wishlist2.status_code == 400
        assert "detail" in new_product_to_wishlist2.json()
        assert new_product_to_wishlist2.json()[
                   "detail"] == f"Rec with user {user.id} and {new_product['id']} already exists"

    def test_get_my_wishlist(self, auth_client, auth_client_superuser, product_data):
        """
        tesst if get will return just my wishlist
        :return: list
        """
        client, user = auth_client
        su_client, su_user = auth_client_superuser

        # create a products
        pr1 = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )

        pr2 = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )

        pr3 = su_client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )

        client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': pr1.data['id']
            },
            format='json'
        )
        client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': pr2.data['id']
            },
            format='json'
        )
        client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': pr3.data['id']
            },
            format='json'
        )
        su_client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': pr1.data['id']
            },
            format='json'
        )
        su_client.post(
            "/wishlists/api/v1/",
            data={
                'user': user.id,
                'product': pr3.data['id']
            },
            format='json'
        )

        response = client.get(
            "/wishlists/api/v1/",
        )

        assert  response.status_code == 200
        for item in response.data['results']:
            print(item)
            assert item['user'] == user.id


        print('>>>>',response.data['results'])
