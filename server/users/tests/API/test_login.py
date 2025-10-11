import requests
from ..fixtures.user_fixtures import URL_ADMIN_LOGIN, BASE_URL

class TestLogin:
    def test_admin_status_code(self):
        assert requests.get(URL_ADMIN_LOGIN).status_code == 200

    def test_base_url(self):
        assert BASE_URL == 'http://127.0.0.1:8000/'

    def test_users_endpoint_is_exist(self):
        assert requests.get(f"{BASE_URL}users/api/v1/").status_code == 200
