from django.db import models
from .models import Product
from .customer 

class Order(models.Model):
    product = models.ForeignKey()