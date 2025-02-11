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
    
    @staticmethoddef get_customer_by_email(email):
        Customer.objects.filter(email=email).first()
    