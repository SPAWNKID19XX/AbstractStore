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

    def test_add_product_to_wishlist(self, auth_client ,product_data):
        client, user = auth_client

        print('««««???', user)
        new_product = client.post(
            "/products/api/v1/",
            data=product_data,
            format='json'
        )

        print('prod', new_product)

