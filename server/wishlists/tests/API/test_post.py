import pytest
from django.db import connection
from products.models import CustomProduct
from wishlists.models import Wishlist

@pytest.mark.django_db
class TestWishlists:
    def test_wishlist_table_exist_in_DB(self):
        table = Wishlist._meta.db_table
        tables = set(connection.introspection.table_names())
        assert table in tables