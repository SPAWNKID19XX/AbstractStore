from django.contrib.auth.models import AbstractUser, PermissionsMixin,AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager
    """

    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("user should has email")

        email = self.normalize_email(email).strip()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        email = self.normalize_email(email).strip()
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is should be is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser should be is_staff=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser should be is_active=True.')

        return self.create_user(email, password, **extra_fields)



# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    #username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    full_name = models.CharField(max_length=256, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name