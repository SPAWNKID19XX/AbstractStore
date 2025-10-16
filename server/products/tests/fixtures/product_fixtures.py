import pytest
from django.template.defaultfilters import title


@pytest.fixture
def product_data():
    new_product = {
        "title": "Test Title"
    }

    return new_product