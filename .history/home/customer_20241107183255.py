from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None
    
    @staticmethod
    def isExist(email):
        return Customer.objects.filter(email=email).exists()
