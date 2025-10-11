from selenium import webdriver
import pytest, requests
from selenium.webdriver.support.ui import WebDriverWait


class TestDjangoInit:

    def test_django_is_installed(self):
        #Checking if Django is installed
        try:
            #try to import
            import django
        except ImportError:
            #information about non installation Django
            assert False, "Django is not installed"

    def test_django_is_runed(self, chrome_driver):

        try:
            r = requests.get("http://127.0.0.1:8000/")
            assert r.status_code == 200
        except requests.ConnectionError:
            assert False, "Django server not running"


    def test_selenium_is_install(self):
        # Checking if selenium is installed
        try:
            # try to import
            import selenium
        except ImportError:
            # information about non installation selenium
            assert False, "Selenium is not installed"

    def test_simpleJWT_isinstalled(self):
        try:
            import rest_framework_simplejwt
        except ImportError:
            assert False, "rest_framework_simplejwt is not installed"

