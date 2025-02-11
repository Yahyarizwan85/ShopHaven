from django.db import models
from home.category import Category

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=150)
    date = models.DateField()
    
    def __str__(self):
            return self.name
        


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE, default=2)
    desc = models.TextField(max_length=150, default="", null=True, blank=True)
    image = models.ImageField(upload_to='productimage/')
    
    def __str__(self):
            return self.name
        

    @staticmethod
    def get_all_Product():
        return Product.objects.all()

    @staticmethod
    def get_all_Product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_Product()


# models.py

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Add other profile-related fields
