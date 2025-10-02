from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.base.models import BaseModel
from apps.user.managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email
