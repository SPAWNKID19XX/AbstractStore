import requests
from ..fixtures.user_fixtures import URL_ADMIN_LOGIN, BASE_URL

class TestGet:
    def test_users_get_endpoint_results_is_returns(self, users_response):
        assert 'results' in users_response, "result does not exist in returns data"


    def test_users_get_endpoint_is_list(self,users_response):
        assert isinstance(users_response['results'], list)