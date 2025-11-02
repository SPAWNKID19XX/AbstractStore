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
        )

        product_id = new_product.json()['id']

        new_product_to_wishlist = client.post(
            "/wishlist/api/v1/items/",
            data={
                'user': user.id,
                'product': product_id
            },
            format='json'
        )

        new_wishlist_rec = new_product_to_wishlist
        print(new_wishlist_rec)

    #todo check if it will be create second rec for same product in wishlist


