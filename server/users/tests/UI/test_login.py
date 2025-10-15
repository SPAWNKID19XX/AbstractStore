import pytest, requests
from selenium import webdriver
from ..fixtures.user_fixtures import URL_ADMIN_LOGIN

class TestLoginUI:

    def test_admin_email_field_exist(self):
        driver = webdriver.Chrome()

        driver.get(URL_ADMIN_LOGIN)

        lbl_username=driver.find_element('xpath', "//label[@for='id_username']").text

        assert lbl_username[:-1] == "Email"
