from django.db import models
from .models import Product
from .C

class Order(models.Model):
    product = models.ForeignKey()