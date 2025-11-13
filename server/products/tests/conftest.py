import pytest
from products.models import CustomProduct


@pytest.fixture
def product_data():
    return {
        "title": "Test Title",
        "description": "Description Test"
    }


@pytest.fixture
def comment_data():
    return {
        "comment": "Comment Test"
    }


@pytest.fixture
def products(db, product_data):
    p1 = CustomProduct.objects.create(**product_data)
    p2 = CustomProduct.objects.create(**product_data)
    p3 = CustomProduct.objects.create(**product_data)
    return [p1, p2, p3]