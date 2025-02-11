from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Model for Signup Data Collection (Separate from the Auth System)
class CustomerProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)  # Ensure emails are unique
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

class Customer(AbstractUser):
    # Add your custom fields here, if any
    phone = models.CharField(max_length=15, blank=True, null=True)
    # Other fields...

    # Add unique related_name for groups and permissions to resolve conflict
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Custom related name for groups
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Custom related name for user permissions
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
