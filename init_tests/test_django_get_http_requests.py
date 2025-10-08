from selenium import webdriver
import pytest, requests

from selenium.webdriver.support.ui import WebDriverWait



def test_django_is_installed():
    try:
        import django
    except:
        assert False, "Django doesn't installed"


def test_django_is_runed_crome(crome_driver):
    crome_driver.get("http://localhost:8000")
    assert "Django" in crome_driver.title

