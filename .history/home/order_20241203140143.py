from django.db import models
from .models import Product
from .custo

class Order(models.Model):
    product = models.ForeignKey()