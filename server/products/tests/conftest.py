import pytest


@pytest.fixture
def product_data():
    return {
        "title": "Test Title"
    }

@pytest.fixture
def aaa():
    return "BumBum"