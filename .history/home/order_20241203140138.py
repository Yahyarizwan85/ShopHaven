from django.db import models
from .models import Product
from .c

class Order(models.Model):
    product = models.ForeignKey()