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


# Main User Model for Authentication and Profile Access
class Customer(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username  # Using username from AbstractUser
