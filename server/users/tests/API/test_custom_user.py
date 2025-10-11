import pytest
from django.contrib.auth import get_user_model


def test_custom_user_model_exist(user_model):
    user = user_model
    assert user is not None, "User model doesnt find"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password, full_name, is_active, is_staff, is_superuser, expected",
    [
        ("admin1@example.com", "admin", "Admin One", True, True, True, True),
        ("admin1@example.com", "admin", "", True, True, True, True),
        ("admin1@example.com", "admin", " ", True, True, True, True),
        ("admin1@example.com", "", "Admin One", True, True, False, ValueError),
        ("admin1@example.com", " ", "Admin One", True, True, False, ValueError),
        ("admin1@example.com", "admin", "Admin One", True, False, True, ValueError),
        ("admin1@example.com", "admin", "Admin One", False, True, True, ValueError),
        ("", "admin", "Admin One", True, True, True, ValueError),
        (" ", "admin", "Admin One", True, True, True, ValueError),
    ]
)
def test_create_superuser(user_model, email, password, full_name, is_active, is_staff, is_superuser,
                                            expected):
    '''
    create superuser test
    :param user_model:
    :param email:
    :param password:
    :param full_name:
    :param is_active:
    :param is_staff:
    :param is_superuser:
    :param expected:
    :return: assert
    '''
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            user_model.objects.create_superuser(
                email=email,
                password=password,
                full_name=full_name,
                is_active=is_active,
                is_staff=is_staff,
                is_superuser=is_superuser
            )
    else:

        new_superuser = user_model.objects.create_superuser(
            email=email,
            password=password,
            full_name=full_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        assert new_superuser.email == email
        assert new_superuser.full_name == full_name
        assert new_superuser.is_active == is_active
        assert new_superuser.is_staff == is_staff
        assert new_superuser.is_superuser == is_superuser
        assert user_model.objects.filter(email=email).exists() == expected


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password, full_name, is_active, is_staff,  expected",
    [
        ("user1@example.com", "user", "User One", True, True, True),
        ("user1@example.com", "user", "", True, True,  True),
        ("user1@example.com", "user", " ", True, True,  True),
        ("user1@example.com", "", "User One", True, True,  ValueError),
        ("user1@example.com", " ", "User One", True, True,  ValueError),
        ("user1@example.com", "user", "User One", True, False, True),
        ("user1@example.com", "user", "User One", False, True,  True),
        ("", "user", "User One", True, True,  ValueError),
        (" ", "user", "User One", True, True,  ValueError),
    ]
)
def test_create_custom_user(user_model, email, password, full_name, is_active, is_staff,
                                            expected):
    '''
    Create user test

    :param user_model:
    :param email:
    :param password:
    :param full_name:
    :param is_active:
    :param is_staff:
    :param is_superuser:
    :param expected:
    :return: assert
    '''
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            user_model.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                is_active=is_active,
                is_staff=is_staff,
            )
    else:

        new_user = user_model.objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
            is_active=is_active,
            is_staff=is_staff,

        )

        assert new_user.email == email
        assert new_user.full_name == full_name
        assert new_user.is_active == is_active
        assert new_user.is_staff == is_staff
        assert new_user.is_superuser == False
        assert user_model.objects.filter(email=email).exists() == expected