from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    
    def register(self):
        self.save()
        
        # @staticmethod
        # def get_customer_by_email(email):
        #     return Customer.objects.get(email = email)
         
         @classmethod
         def get_customer_by_email(cls, email):
             try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None

        
        def isExist(self):
            if Customer.objects.filter(email = self.email):
                return True
            return False    
