import requests
from ..fixtures.user_fixtures import URL_ADMIN_LOGIN

class TestLogin:
    def test_admin_status_code(self):
        assert requests.get(URL_ADMIN_LOGIN).status_code == 200