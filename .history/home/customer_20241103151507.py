from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Model for Signup Data Collection (Separate from the Auth System)
class Customer(models.Model):
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
        verbose_name="