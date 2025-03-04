# Django Imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from django.db import models

# Module Imports
from autentication_module.managers import UserManager

# User Class 
class User(AbstractBaseUser, PermissionsMixin):

    # User Fields
    user_name = models.CharField(_("Name of User"), max_length=255, null=False)
    user_email = models.EmailField(_("Email of User"), max_length=255, null=False)
    user_cpf = models.CharField(_("CPF User"), max_length=14, null=False, unique=True)
    password = models.CharField(_("Password of User"), max_length=255, null=False)

    # Access and permission data
    is_staff = models.BooleanField(_("Admin?"), default=False)
    is_active = models.BooleanField(_("Active?"), default=True)
    is_trusty = models.BooleanField(_("Trusty?"), default=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    # Authentication field
    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_cpf"]

    # Manager for create operations
    objects = UserManager()

    # Default return
    def __str__(self):

        return self.user_email

    class Meta:

        db_table = "autentication_module"
        app_label = "autentication_module"
        constraints = [
            models.UniqueConstraint(fields=['user_cpf'], name='unique_cpf'),
            models.UniqueConstraint(fields=['user_email'], name='unique_email')
        ]
