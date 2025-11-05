from time import sleep

import pytest
from django.db import connection
from reviews.models import Reviews


@pytest.mark.django_db
class TestReviews:
    def test_reviews_table_exist_in_DB(self):
        table = Reviews._meta.db_table
        tables = set(connection.introspection.table_names())
        assert table in tables

