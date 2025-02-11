from django.db import models
from .models import Product


class Order(models.Model):
    product = models.ForeignKey()