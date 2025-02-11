# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models

# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=13)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=500)
    
#     def register(self):
#         self.save()
        
#         @staticmethod
#         def get_customer_by_email(email):
#             return Customer.objects.filter(email = email)
            
        
        
#     def isExist(self):
#         if Customer.objects.filter(email = self.email):
#             return True
#         return False    


from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)

    def register(self):
        # Hash the password before saving
        self.password = make_password(self.password)
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def is_exist(self):
        return Customer.objects.filter(email=self.email).exists()

    def check_password(self, raw_password):
        # Check if the raw password matches the hashed password
        return check_password(raw_password, self.password)

        
        