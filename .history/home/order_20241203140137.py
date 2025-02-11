from django.db import models
from .models import Product
from .

class Order(models.Model):
    product = models.ForeignKey()