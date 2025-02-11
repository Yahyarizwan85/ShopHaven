from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)  # Ensure emails are unique
    password = models.CharField(max_length=500)  # Store hashed passwords

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email).first()

        except Customer.DoesNotExist:
            return None  # Return None if customer is not found
