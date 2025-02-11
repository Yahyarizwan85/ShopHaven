from django.db import models
from .models import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    