from django.db import models
from .models import Product
from .cust

class Order(models.Model):
    product = models.ForeignKey()