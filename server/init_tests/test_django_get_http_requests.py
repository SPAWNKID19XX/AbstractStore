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
            r = requests.get("http://localhost:8000")
            assert r.status_code == 200
        except requests.ConnectionError:
            assert False, "Django server not running"

        # Открываем страницу в браузере
        chrome_driver.get("http://localhost:8000")
        WebDriverWait(chrome_driver, 10).until(lambda d: d.title != "")
        assert "The install worked successfully! Congratulations!" == chrome_driver.title, f"Title is: {chrome_driver.title}"

