from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # related_name-ni o'zgartiramiz
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # related_name-ni o'zgartiramiz
        blank=True,
    )
    # Boshqa qo'shimcha maydonlar:
    age = models.IntegerField(blank=True, null=True)
