import pytest
import requests
from ..fixtures.user_fixtures import URL_ADMIN_LOGIN, BASE_URL
from django.contrib.auth import get_user_model


class TestGet:
    def test_users_get_endpoint_results_is_returns(self, users_response):
        assert 'results' in users_response, "result does not exist in returns data"

    def test_users_get_endpoint_is_list(self, users_response):
        assert isinstance(users_response['results'], list)

    #@pytest.mark.django_db
    def test_fields_get_users_respons_structure(self, users_response):
        assert 'count' in users_response and isinstance(users_response['count'], int)
        assert 'next' in users_response
        assert 'previous' in users_response
        assert 'results' in users_response
        for user in users_response['results']:
            assert 'id' in user and isinstance(users_response['results'][0]['id'], int)
            assert 'email' in user and user['email'].strip() != '' and isinstance(user['email'], str)
            assert 'full_name' in user and isinstance(user['email'], str)
            assert 'is_active' in user and isinstance(user['is_active'], bool)
            assert 'is_staff' in user and isinstance(user['is_staff'], bool)
            assert 'is_superuser' in user and isinstance(user['is_superuser'], bool)

