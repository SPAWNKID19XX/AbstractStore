import pytest
from ..models import CustomUser

@pytest.fixture
def users():
    return CustomUser()