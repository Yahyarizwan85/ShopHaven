from django.db import models
from django.contrib.auth.models import AbstractUser
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    
    def __str__(self):
            return self.first_name
        


# models.py


class Customers(AbstractUser):  # or models.Model if you're not extending AbstractUser
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Add any other fields you want for the profile
